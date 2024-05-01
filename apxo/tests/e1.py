from apxo.tests.infrastructure import *

startfile(__file__, "climbs")

# Climbs

# Sustained Climbs

starttestsetup()
A1 = aircraft("A1", "AF", "F-80C", "A1-1815", "N", 20, 4.0, "CL")
A2 = aircraft("A2", "AF", "F-80C", "A1-2015", "N", 10, 4.0, "CL")
A3 = aircraft("A3", "AF", "F-84E", "A1-2215", "N", 1, 5.0, "CL")
A4 = aircraft("A4", "AF", "F-80C", "A1-2415", "N", 45, 5.0, "CL")
endtestsetup()

startgameturn()
A4.move("SC", "M", "H,H,C,C,C")
asserterror("attempt to climb above ceiling in SC.")
startgameturn()
A1.move("SC", "M", "H,H,H,C")
A1._assert("A1-1812       N    20", 4.0)
A2.move("SC", "M", "H,H,H,C")
A2._assert("A1-2012       N    11", 4.0)
A3.move("SC", "M", "H,H,C,C,C")
A3._assert("A1-2213       N     3", 5.0)
A4.move("SC", "M", "H,H,H,H,C")
A4._assert("A1-2411       N    45", 4.0)
endgameturn()

startgameturn()
A4.move("SC", "M", "H,H,H,C")
asserterror("attempt to climb above ceiling in SC.")
startgameturn()
A1.move("SC", "M", "H,H,H,C")
A1._assert("A1-1809       N    21", 4.0)
A2.move("SC", "M", "H,H,H,C")
A2._assert("A1-2009       N    12", 4.0)
A3.move("SC", "M", "H,H,C,C,C")
A3._assert("A1-2211       N     6", 4.5)
A4.move("LVL", "M", "H,H,H,H")
A4._assert("A1-2407       N    45", 4.0)
endgameturn()

# Zoom Climbs

starttestsetup()
A1 = aircraft("A1", "AF", "F-80C", "A1-1815", "N", 1, 5.5, "CL")
A2 = aircraft("A2", "AF", "F-80C", "A1-2015", "N", 45, 4.0, "CL")
endtestsetup()

startgameturn()
A1.move("ZC", "M", "H,C,C,C,C")
asserterror("too few HFPs.")
startgameturn()
A1.move("ZC", "M", "H,H,H,H,C2")
asserterror("invalid altitude change in climb.")
startgameturn()
A1.move("ZC", "M", "H,H,C,C,C")
A1._assert("A1-1813       N     4", 5.0)
A2.move("ZC", "M", "H,C,C,C")
A2._assert("A1-2014       N    48", 3.5)
endgameturn()

startgameturn()
A1.move("ZC", "M", "H,H,C,C,C")
A1._assert("A1-1811       N     7", 4.5)
A2.move("ZC", "M", "H,C,C")
A2._assert("A1-2013       N    50", 3.0)
endgameturn()

startgameturn()
A1.move("ZC", "M", "H,H,C,C,C")
A1._assert("A1-1809       N    10", 3.5)
A2.move("ZC", "M", "H,C,C")
A2._assert("A1-2012       N    52", 2.5)
endgameturn()

startgameturn()
A1.move("ZC", "M", "H,C,C")
A1._assert("A1-1808       N    12", 3.0)
A2.move("ZC", "M", "H,C,C")
A2._assert("A1-2011       N    54", 1.5)
endgameturn()

startgameturn()
A1.move("ZC", "M", "H,C,C")
A1._assert("A1-1807       N    14", 2.5)
A2.move("ST", "M", "")
A2._assert("A1-2011       N    52", 1.5)
endgameturn()

startgameturn()
A1.move("ZC", "M", "H,C,C")
A1._assert("A1-1806       N    16", 2.0)
A2.move("ST", "M", "")
A2._assert("A1-2011       N    49", 2.5)
endgameturn()

startgameturn()
A1.move("ZC", "M", "H,C")
A1._assert("A1-1805       N    17", 2.0)
A2.move("LVL", "M", "H,H")
A2._assert("A1-2009       N    49", 2.5)
endgameturn()

startgameturn()
A1.move("ZC", "M", "H,C")
A1._assert("A1-1804       N    18", 1.5)
A2.move("LVL", "M", "H,H,H")
A2._assert("A1-2006       N    49", 3.0)
endgameturn()

starttestsetup(variants=["use version 2.4 rules"])
A1 = aircraft("A1", "AF", "F-104A", "A1-1815", "N", 1, 4.5, "CL")
endtestsetup()

startgameturn()
A1.move("ZC", "M", "H,C3,H,H")
asserterror("invalid altitude change in climb.")
startgameturn()
A1.move("ZC", "AB", "H,C2,H,H")
A1._assert("A1-1812       N    3", 4.5)
endgameturn()

starttestsetup(variants=["use version 2.4 rules"])
A1 = aircraft("A1", "AF", "F-104A", "A1-1815", "N", 1, 4.5, "CL")
endtestsetup()

startgameturn()
A1.move("ZC", "M", "H,C3,H,H")
asserterror("invalid altitude change in climb.")
startgameturn()
A1.move("ZC", "AB", "H,C3,C3,H")
asserterror("invalid altitude change in climb.")
startgameturn()
A1.move("ZC", "AB", "H,C3,C2,H")
A1._assert("A1-1813       N    6", 4.5)
endgameturn()

# Vertical Climbs

starttestsetup()
A1 = aircraft("A1", "AF", "F-80C", "A1-1815", "N", 1, 5.5, "CL")
A2 = aircraft("A2", "AF", "F-80C", "A1-2015", "N", 45, 4.0, "CL")
endtestsetup()

startgameturn()
A1.move("VC", "M", "H,C,C,C,C")
asserterror("flight type immediately after LVL cannot be VC.")
startgameturn()
A1.move("ZC", "M", "H,H,C,C,C")
A1._assert("A1-1813       N     4", 5.0)
A2.move("ZC", "M", "H,H,H,C")
A2._assert("A1-2012       N    46", 4.0)
endgameturn()

startgameturn()
A1.move("VC", "M", "H,C2,C2,C2,C2")
asserterror("too few HFPs.")
startgameturn()
A1.move("VC", "M", "H,H,H,C2,C2")
asserterror("too many HFPs.")
startgameturn()
A1.move("VC", "M", "H,H,C2,C2,C2")
A1._assert("A1-1811       N    10", 2.5)
A2.move("VC", "M", "H,C2,C2,C2")
A2._assert("A1-2011       N    52", 1.0)
endgameturn()

startgameturn()
A1.move("SD", "M", "H,D,D")
asserterror("flight type immediately after VC cannot be SD (without a HRD).")
startgameturn()
A1.move("UD", "M", "H,D,D")
asserterror("flight type immediately after VC cannot be UD.")
startgameturn()
A1.move("VD", "M", "H,D,D")
asserterror("flight type immediately after VC cannot be VD.")
startgameturn()
A1.move("VC", "M", "C2,C2,C2")
A1._assert("A1-1811       N    16", 0.0)
A2.move("ST", "M", "")
A2._assert("A1-2011       N    51", 1.0)
endgameturn()

endfile(__file__)
