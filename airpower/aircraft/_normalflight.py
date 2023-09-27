"""
Normal flight for the aircraft class.
"""

import math

import airpower.altitude as apaltitude
import airpower.data     as apdata
import airpower.hex      as aphex
import airpower.speed    as apspeed

def _A(self, weapon):

  """
  Declare an attack with the specified weapon.
  """

  self._logevent("attack with %s." % weapon)

def _C(self, altitudechange):

  """
  Climb.
  """

  if not self._flighttype in ["ZC", "SC", "VC"]:
    raise ValueError("attempt to climb while flight type is %s." % self._flighttype)

  initialaltitude = self._altitude    
  self._altitude, self._altitudecarry = apaltitude.adjustaltitude(self._altitude, self._altitudecarry, +altitudechange)
  self._altitudeband  = apaltitude.altitudeband(self._altitude)
  altitudechange = self._altitude - initialaltitude

  if self._flighttype == "ZC":
    if self._lastflighttype == "ZC":
      self._altitudeap -= 1.5 * altitudechange
    else:
      self._altitudeap -= 1.0 * altitudechange
  elif self._flighttype == "SC":
    # TODO: deceleration for climb in excess of CC
    self._altitudeap -= 0.5 * altitudechange
  elif self._flighttype == "VC":
    self._altitudeap -= 2.0 * altitudechange

def _D(self, altitudechange):

  """
  Dive.
  """

  if not self._flighttype in ["LVL", "SD", "UD", "VD"]:
    raise ValueError("attempt to dive while flight type is %s." % self._flighttype)

  initialaltitude = self._altitude    
  self._altitude, self._altitudecarry = apaltitude.adjustaltitude(self._altitude, self._altitudecarry, -altitudechange)
  self._altitudeband = apaltitude.altitudeband(self._altitude)
  altitudechange = initialaltitude - self._altitude

  if self._flighttype == "LVL":
    pass
  elif self._flighttype == "SD":
    if self._lastflighttype == "SD":
      self._altitudeap += 1.0 * altitudechange
    else:
      self._altitudeap += 0.5 * altitudechange
  elif self._flighttype == "UD":
    if self._lastflighttype == "UD":
      self._altitudeap += 1.0 * altitudechange
    else:
      self._altitudeap += 0.5 * altitudechange
  elif self._flighttype == "VD":
    self._altitudeap += 1.0 * altitudechange

def _H(self):

  """
  Move horizontally.
  """

  self._x, self._y = aphex.nextposition(self._x, self._y, self._facing)

def _J(self, configuration):

  """
  Jetison stores to achieve the specified configuration.
  """

  # See rule 4.4. 
  
  # We implement the delay of 1 FP by making this an epilog element.

  if self._configuration == configuration:
    raise ValueError("configuration is already %s." % configuration)
  if self._configuration == "CL" or configuration == "DT":
    raise ValueError("attempt to change from configuration %s to %s." % (self._configuration, configuration))
  self._logevent("jettisoned stores.")
  self._logevent("configuration changed from %s to %s." % (self._configuration, configuration))
  self._configuration = configuration

def _K(self):

  """
  Declare that the aircraft has been killed.
  """

  self._logevent("aircraft has been killed.")
  self._destroyed = True

def _S(self, spbrfp):

  """
  Use the speedbrakes.
  """

  # See rule 6.5 and the "Supersonic Speeds" section of rule 6.6.

  if self._spbrfp != 0:
    raise ValueError("speedbrakes can only be used once per turn.")

  maxspbrfp = self._fp - self._hfp - self._vfp
  if spbrfp > maxspbrfp:
    raise ValueError("only %s FPs are remaining." % maxspbrfp)
    
  maxspbrfp = self._aircrafttype.SPBR(self._configuration)
  if self._speed > apspeed.m1speed(self._altitudeband):
    maxspbrfp += 0.5
  if spbrfp > maxspbrfp:
    raise ValueError("speedbrake capability is only %.1f FPs." % maxspbrfp)

  self._spbrfp = spbrfp

  self._spbrap = -spbrfp / 0.5

def _TD(self, bank, turnrate):

  """
  Start a turn in the specified direction and rate.
  """
  
  turnrates = ["EZ", "TT", "HT", "BT", "ET"]
  assert turnrate in turnrates
  self._bank = bank
  self._turnrate = turnrate

def _TL(self, facingchange):

  """
  Turn left.
  """

  if self._bank == "R":
    self._turnfp -= 1
  minturnrate = apdata.determineturnrate(self._altitudeband, self._speed, self._turnfp, facingchange)
  if minturnrate == None:
    raise ValueError("attempt to turn faster than the maximum turn rate.")

  self._turnfp = 0
  self._bank = "L"

  # Implicitly declare turn rates.
  self._turnrate = minturnrate

  if self._maxturnrate == None:
    self._maxturnrate = self._turnrate
  else:
    turnrates = ["EZ", "TT", "HT", "BT", "ET"]
    self._maxturnrate = turnrates[max(turnrates.index(self._turnrate), turnrates.index(self._maxturnrate))]

  if self._maxturnrate == "EZ":
    self._turnrateap = 0.0
  else:
    self._turnrateap = -self._aircrafttype.turndrag(self._configuration, self._maxturnrate)

  # See the "Supersonic Speeds" section of rule 6.6.
  if self._speed >= apspeed.m1speed(self._altitudeband):
    self._turnrateap += 1

  # Change facing.
  if aphex.isedgeposition(self._x, self._y):
    self._x, self._y = aphex.centertoleft(self._x, self._y, self._facing)
  self._facing = (self._facing + facingchange) % 360

  self._turns += 1
  if self._turns > 1:
    # Apply the sustained turn drag penalty.
    # TODO: drag for HBR and LBR aircraft.
    self._sustainedturnap -= facingchange // 30
    
def _TR(self, facingchange):

  """
  Turn right.
  """

  if self._bank == "L":
    self._turnfp -= 1
  minturnrate = apdata.determineturnrate(self._altitudeband, self._speed, self._turnfp, facingchange)
  if minturnrate == None:
    raise ValueError("attempt to turn faster than the maximum turn rate.")

  self._turnfp = 0
  self._bank = "R"

  # Implicitly declare turn rates.
  self._turnrate = minturnrate

  if self._maxturnrate == None:
    self._maxturnrate = self._turnrate
  else:
    turnrates = ["EZ", "TT", "HT", "BT", "ET"]
    self._maxturnrate = turnrates[max(turnrates.index(self._turnrate), turnrates.index(self._maxturnrate))]

  if self._maxturnrate == "EZ":
    self._turnrateap = 0.0
  else:
    self._turnrateap = -self._aircrafttype.turndrag(self._configuration, self._maxturnrate)

  # See the "Supersonic Speeds" section of rule 6.6.
  if self._speed >= apspeed.m1speed(self._altitudeband):
    self._turnrateap += 1

  # Change facing.
  if aphex.isedgeposition(self._x, self._y):
    self._x, self._y = aphex.centertoright(self._x, self._y, self._facing)
  self._facing = (self._facing - facingchange) % 360
  
  self._turns += 1
  if self._turns > 1:
    # Apply the sustained turn drag penalty.
    # TODO: drag for HBR and LBR aircraft.
    self._sustainedturnap -= facingchange // 30
    
def _getelementdispatchlist(self):

  return [

    # This table is searched in order, so put longer elements before shorter 
    # ones that are prefixes (e.g., put C2 before C and D3/4 before D3).

    # [0] is the element code.
    # [1] is the procedure for movement elements.
    # [2] is the procedure for other (non-movement) elements.

    ["H"   , lambda : None               , lambda : self._H()          , lambda: None],

    ["C1/8", lambda : None               , lambda : self._C(1/8)       , lambda: None],
    ["C1/4", lambda : None               , lambda : self._C(1/4)       , lambda: None],
    ["C3/8", lambda : None               , lambda : self._C(3/8)       , lambda: None],
    ["C1/2", lambda : None               , lambda : self._C(1/2)       , lambda: None],
    ["C5/8", lambda : None               , lambda : self._C(5/8)       , lambda: None],
    ["C3/4", lambda : None               , lambda : self._C(3/4)       , lambda: None],
    ["C7/8", lambda : None               , lambda : self._C(7/8)       , lambda: None],
    ["C1"  , lambda : None               , lambda : self._C(1)         , lambda: None],
    ["C2"  , lambda : None               , lambda : self._C(2)         , lambda: None],
    ["CC"  , lambda : None               , lambda : self._C(2)         , lambda: None],
    ["C"   , lambda : None               , lambda : self._C(1)         , lambda: None],

    ["D1/8", lambda : None               , lambda : self._D(1/8)       , lambda: None],
    ["D1/4", lambda : None               , lambda : self._D(1/4)       , lambda: None],
    ["D3/8", lambda : None               , lambda : self._D(3/8)       , lambda: None],
    ["D1/2", lambda : None               , lambda : self._D(1/2)       , lambda: None],
    ["D5/8", lambda : None               , lambda : self._D(5/8)       , lambda: None],
    ["D3/4", lambda : None               , lambda : self._D(3/4)       , lambda: None],
    ["D7/8", lambda : None               , lambda : self._D(7/8)       , lambda: None],
    ["D1"  , lambda : None               , lambda : self._D(1)         , lambda: None],
    ["D2"  , lambda : None               , lambda : self._D(2)         , lambda: None],
    ["D3"  , lambda : None               , lambda : self._D(3)         , lambda: None],
    ["DDD" , lambda : None               , lambda : self._D(3)         , lambda: None],
    ["DD"  , lambda : None               , lambda : self._D(2)         , lambda: None],
    ["D"   , lambda : None               , lambda : self._D(1)         , lambda: None],

    ["LEZ" , lambda : self._TD("L", "EZ"), lambda : None               , lambda: None],
    ["LTT" , lambda : self._TD("L", "TT"), lambda : None               , lambda: None],
    ["LHT" , lambda : self._TD("L", "HT"), lambda : None               , lambda: None],
    ["LBT" , lambda : self._TD("L", "BT"), lambda : None               , lambda: None],
    ["LET" , lambda : self._TD("L", "ET"), lambda : None               , lambda: None],
    
    ["REZ" , lambda : self._TD("R", "EZ"), lambda : None               , lambda: None],
    ["RTT" , lambda : self._TD("R", "TT"), lambda : None               , lambda: None],
    ["RHT" , lambda : self._TD("R", "HT"), lambda : None               , lambda: None],
    ["RBT" , lambda : self._TD("R", "BT"), lambda : None               , lambda: None],
    ["RET" , lambda : self._TD("R", "ET"), lambda : None               , lambda: None],

    ["L90" , lambda : None               , lambda : self._TL(90)       , lambda: None],
    ["L60" , lambda : None               , lambda : self._TL(60)       , lambda: None],
    ["L30" , lambda : None               , lambda : self._TL(30)       , lambda: None],
    ["LLL" , lambda : None               , lambda : self._TL(90)       , lambda: None],
    ["LL"  , lambda : None               , lambda : self._TL(60)       , lambda: None],
    ["L"   , lambda : None               , lambda : self._TL(30)       , lambda: None],

    ["R90" , lambda : None               , lambda : self._TR(90)       , lambda: None],
    ["R60" , lambda : None               , lambda : self._TR(60)       , lambda: None],
    ["R30" , lambda : None               , lambda : self._TR(30)       , lambda: None],
    ["RRR" , lambda : None               , lambda : self._TR(90)       , lambda: None],
    ["RR"  , lambda : None               , lambda : self._TR(60)       , lambda: None],
    ["R"   , lambda : None               , lambda : self._TR(30)       , lambda: None],

    ["S1/2", lambda : None               , lambda: self._S(1/2)        , lambda: None],
    ["S1"  , lambda : None               , lambda: self._S(1)          , lambda: None],
    ["S3/2", lambda : None               , lambda: self._S(3/2)        , lambda: None],
    ["S2"  , lambda : None               , lambda: self._S(2)          , lambda: None],
    ["SSSS", lambda : None               , lambda: self._S(2)          , lambda: None],
    ["SSS" , lambda : None               , lambda: self._S(3/2)        , lambda: None],
    ["SS"  , lambda : None               , lambda: self._S(1)          , lambda: None],
    ["S"   , lambda : None               , lambda: self._S(1/2)        , lambda: None],

    ["/"   , lambda : None               , lambda : None               , lambda: None],

    ["AGN" , lambda : None               , lambda : None               , lambda: self._A("guns")],
    ["AGP" , lambda : None               , lambda : None               , lambda: self._A("gun pod")],
    ["ARK" , lambda : None               , lambda : None               , lambda: self._A("rockets")],
    ["ARP" , lambda : None               , lambda : None               , lambda: self._A("rocket pods")],

    ["J1/2", lambda : None               , lambda : None               , lambda: self._J("1/2")],
    ["JCL" , lambda : None               , lambda : None               , lambda: self._J("CL") ],

    ["K"   , lambda : None               , lambda : None               , lambda: self._K()],

  ]

def _doaction(self, action):

  """
  Carry out an action for normal flight.
  """

  if self._hfp + self._vfp + self._spbrfp + 1 > self._fp:
    raise ValueError("only %.1f FPs are available." % self._fp)
      
  if action[0] == 'H':
    self._hfp += 1
  elif action[0] == 'D' or action[0] == 'C':
    self._vfp += 1
  else:
    raise ValueError("action %s does not begin with H, D, or C." % action)
    
  self._turnfp += 1

  lastx = self._x
  lasty = self._y

  elementdispatchlist = self._getelementdispatchlist()

  initialaltitudeband = self._altitudeband

  # Prolog elements.
  a = action
  while a != "":
    for element in elementdispatchlist:
      if element[0] == a[:len(element[0])]:
        element[1]()
        a = a[len(element[0]):]
        break
    else:
      raise ValueError("invalid element %r in action %r." % (a, action))

  # Movement elements.
  a = action
  while a != "":
    for element in elementdispatchlist:
      if element[0] == a[:len(element[0])]:
        element[2]()
        a = a[len(element[0]):]
        break
    else:
      raise ValueError("invalid element %r in action %r." % (a, action))

  assert aphex.isvalidposition(self._x, self._y)
  assert aphex.isvalidfacing(self._x, self._y, self._facing)
  assert apaltitude.isvalidaltitude(self._altitude)
  
  self._logposition("FP %d" % (self._hfp + self._vfp), action)
  self._drawflightpath(lastx, lasty)

  if initialaltitudeband != self._altitudeband:
    self._logevent("altitude band changed from %s to %s." % (initialaltitudeband, self._altitudeband))
      
  self.checkforterraincollision()
  self.checkforleavingmap()
  if self._destroyed or self._leftmap:
    return

  # Other elements.
  a = action
  while a != "":
    for element in elementdispatchlist:
      if element[0] == a[:len(element[0])]:
        element[3]()
        a = a[len(element[0]):]
        break
    else:
      raise ValueError("invalid element %r in action %r." % (a, action))

def _donormalflight(self, actions):

  """
  Carry out normal flight.
  """

  if actions != "":
    for action in actions.split(","):
      if not self._destroyed and not self._leftmap:
        self._doaction(action)

  fp = self._hfp + self._vfp + self._spbrfp
  assert fp <= self._fp

  if fp + 1 > self._fp or self._destroyed or self._leftmap:

    self._drawaircraft("end")
    self._log("---")
    self._endmove()
    
  else:
    
    self._drawaircraft("next")

################################################################################

def _isdiving(flighttype):

  """
  Return True if the flight type is SD, UD, or VD. Otherwise return False.
  """

  return flighttype == "SD" or flighttype == "UD" or flighttype == "VD"

def _isclimbing(flighttype):

  """
  Return True if the flight type is ZC, SC, or VC. Otherwise return False.
  """
  
  return flighttype == "ZC" or flighttype == "SC" or flighttype == "VC"

################################################################################

