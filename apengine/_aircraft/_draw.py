"""
Drawing for the aircraft class.
"""

import apengine._draw as apdraw

flightpathcolor     = ( 0.00, 0.00, 0.00 )
flightpathlinewidth = 2.0
flightpathlinestyle = "dotted"
flightpathdotsize   = 0.05
linecolor           = ( 0.00, 0.00, 0.00 )
textsize            = 10
textcolor           = ( 0.00, 0.00, 0.00 )
counterlinewidth    = 2

def _startflightpath(self):
  self._flightpathx = [self._x]
  self._flightpathy = [self._y]

def _continueflightpath(self):
  self._flightpathx.append(self._x)
  self._flightpathy.append(self._y)

def _drawflightpath(self):
  x = self._flightpathx
  y = self._flightpathy
  if x != [] and y != []:
    apdraw.drawdot(x[0], y[0], color=flightpathcolor, size=flightpathdotsize, zorder=0.5)
    apdraw.drawlines(x, y, color=flightpathcolor, linewidth=flightpathlinewidth, linestyle=flightpathlinestyle, zorder=0.5)

def _drawaircraft(self):
  if self._leftmap:
    return
  if self._destroyed:
    fillcolor = "black"
    altitude  = "--"
  else:
    fillcolor = self._color
    altitude  = "%2d" % self._altitude
  x = self._x
  y = self._y
  facing = self._facing
  if self._counter:
    apdraw.drawsquare(x, y, facing=facing, size=1, linecolor="black", linewidth=counterlinewidth, fillcolor=self._color, zorder=1)
    apdraw.drawdart(x, y, facing, size=0.4, fillcolor="black", linewidth=1, linecolor="black", zorder=1)
  else:
    apdraw.drawdart(x, y, facing, dy=-0.02, size=0.4, fillcolor=fillcolor, linewidth=1, linecolor=linecolor, zorder=1)
    apdraw.drawtext(x, y, facing, self._name, dx=-0.25, dy=0.0, size=textsize, color=textcolor, zorder=1)
    apdraw.drawtext(x, y, facing, altitude  , dx=+0.25, dy=0.0, size=textsize, color=textcolor, zorder=1)
