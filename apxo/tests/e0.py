from apxo.tests.infrastructure import *

startfile(__file__, "initial HFPs")

# Required HFPs. Here we check enforcement of rule 5.4 on the number of initial
# HFPs required when transitioning from level to climbing/diving flight, between
# climbing and diving flight, and between diving and climbing flight.

starttestsetup()
A1 = aircraft("A1", "AF", "F-80C", "A1-1815", "N", 10, 4.0, "CL")
A2 = aircraft("A2", "AF", "F-80C", "A1-2015", "N", 10, 4.0, "CL")
A3 = aircraft("A3", "AF", "F-80C", "A1-2215", "N", 10, 4.0, "CL")
A4 = aircraft("A4", "AF", "F-80C", "A1-2415", "N", 10, 4.0, "CL")
endtestsetup()

startgameturn()
A1.move("ZC", "M", "C,H,H,H")
asserterror("insufficient initial HFPs.")
startgameturn()
A1.move("ZC", "M", "H,H,H,C")
A1._assert("A1-1812       N    11", 4.0)
A2.move("ZC", "M", "H,C,H,H")
A2._assert("A1-2012       N    11", 4.0)
A3.move("ZC", "M", "H,H,H,C")
A3._assert("A1-2212       N    11", 4.0)
A4.move("ZC", "M", "H,H,H,C")
A4._assert("A1-2412       N    11", 4.0)
endgameturn()

startgameturn()
A1.move("SD", "N", "D,H,H,H")
asserterror("insufficient initial HFPs.")
startgameturn()
A2.move("SD", "N", "H,D,H,H")
asserterror("insufficient initial HFPs.")
startgameturn()
A1.move("SD", "N", "H,H,H,D")
A1._assert("A1-1809       N    10", 4.0)
A2.move("SD", "N", "H,H,H,D")
A2._assert("A1-2009       N    10", 4.0)
A3.move("SD", "N", "H,H,D,H")
A3._assert("A1-2209       N    10", 4.0)
A4.move("ZC", "M", "C,H,H,H")
A4._assert("A1-2409       N    12", 4.0)
endgameturn()

starttestsetup()
A1 = aircraft("A1", "AF", "F-80C", "A1-1815", "N", 10, 4.0, "CL")
A2 = aircraft("A2", "AF", "F-80C", "A1-2015", "N", 10, 4.0, "CL")
A3 = aircraft("A3", "AF", "F-80C", "A1-2215", "N", 10, 4.0, "CL")
A4 = aircraft("A4", "AF", "F-80C", "A1-2415", "N", 10, 4.0, "CL")
endtestsetup()

startgameturn()
A1.move("SD", "N", "D,H,H,H")
asserterror("insufficient initial HFPs.")
startgameturn()
A1.move("SD", "N", "H,H,H,D")
A1._assert("A1-1812       N     9", 4.0)
A2.move("SD", "N", "H,D,H,H")
A2._assert("A1-2012       N     9", 4.0)
A3.move("SD", "N", "H,H,H,D")
A3._assert("A1-2212       N     9", 4.0)
A4.move("SD", "N", "H,H,H,D")
A4._assert("A1-2412       N     9", 4.0)
endgameturn()


startgameturn()
A1.move("ZC", "M", "C,H,H,H")
asserterror("insufficient initial HFPs.")
startgameturn()
A2.move("ZC", "M", "H,C,H,H")
asserterror("insufficient initial HFPs.")
startgameturn()
A1.move("ZC", "M", "H,H,H,C")
A1._assert("A1-1809       N    10", 4.0)
A2.move("ZC", "M", "H,H,H,C")
A2._assert("A1-2009       N    10", 4.0)
A3.move("ZC", "M", "H,H,C,H")
A3._assert("A1-2209       N    10", 4.0)
A4.move("SD", "N", "D,H,H,H")
A4._assert("A1-2409       N     8", 4.5)
endgameturn()

endfile(__file__)
