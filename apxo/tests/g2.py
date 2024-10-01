from apxo.tests.infrastructure import *

startfile(__file__, "lag rolls")


# Lag Rolls

# Check the position after lag rolls.

starttestsetup(sheets=[["A1"]], verbose=False)
A1 = aircraft("A1", "AF", "F-80C", "A1-1708", "E", 10, 2.0, "CL")
A2 = aircraft("A2", "AF", "F-80C", "A1-2308", "E", 10, 2.0, "CL")
endtestsetup()
startgameturn()
A1.move("LVL", "M", "LRL/H,H/L")
A1._assert("A1-1808       ESE  10", 2.0)
A2.move("LVL", "M", "LRR/H,H/R")
A2._assert("A1-2409       ENE  10", 2.0)
endgameturn()

starttestsetup(sheets=[["A1"]])
A1 = aircraft("A1", "AF", "F-80C", "A1-1708", "ENE", 10, 2.0, "CL")
A2 = aircraft("A2", "AF", "F-80C", "A1-2308", "ENE", 10, 2.0, "CL")
endtestsetup()
startgameturn()
A1.move("LVL", "M", "LRL/H,H/L")
A1._assert("A1-1807       E    10", 2.0)
A2.move("LVL", "M", "LRR/H,H/R")
A2._assert("A1-2508       NNE  10", 2.0)
endgameturn()

starttestsetup(sheets=[["A1"]])
A1 = aircraft("A1", "AF", "F-80C", "A1-1708", "NNE", 10, 2.0, "CL")
A2 = aircraft("A2", "AF", "F-80C", "A1-2308", "NNE", 10, 2.0, "CL")
endtestsetup()
startgameturn()
A1.move("LVL", "M", "LRL/H,H/L")
A1._assert("A1-1707       ENE  10", 2.0)
A2.move("LVL", "M", "LRR/H,H/R")
A2._assert("A1-2408       N    10", 2.0)
endgameturn()

starttestsetup(sheets=[["A1"]])
A1 = aircraft("A1", "AF", "F-80C", "A1-1708", "N", 10, 2.0, "CL")
A2 = aircraft("A2", "AF", "F-80C", "A1-2308", "N", 10, 2.0, "CL")
endtestsetup()
startgameturn()
A1.move("LVL", "M", "LRL/H,H/L")
A1._assert("A1-1607       NNE  10", 2.0)
A2.move("LVL", "M", "LRR/H,H/R")
A2._assert("A1-2407       NNW  10", 2.0)
endgameturn()

starttestsetup(sheets=[["A1"]])
A1 = aircraft("A1", "AF", "F-80C", "A1-1708", "NNW", 10, 2.0, "CL")
A2 = aircraft("A2", "AF", "F-80C", "A1-2308", "NNW", 10, 2.0, "CL")
endtestsetup()
startgameturn()
A1.move("LVL", "M", "LRL/H,H/L")
A1._assert("A1-1608       N    10", 2.0)
A2.move("LVL", "M", "LRR/H,H/R")
A2._assert("A1-2307       WNW  10", 2.0)
endgameturn()

starttestsetup(sheets=[["A1"]])
A1 = aircraft("A1", "AF", "F-80C", "A1-1708", "WNW", 10, 2.0, "CL")
A2 = aircraft("A2", "AF", "F-80C", "A1-2308", "WNW", 10, 2.0, "CL")
endtestsetup()
startgameturn()
A1.move("LVL", "M", "LRL/H,H/L")
A1._assert("A1-1508       NNW  10", 2.0)
A2.move("LVL", "M", "LRR/H,H/R")
A2._assert("A1-2207       W    10", 2.0)
endgameturn()

starttestsetup(sheets=[["A1"]])
A1 = aircraft("A1", "AF", "F-80C", "A1-1708", "W", 10, 2.0, "CL")
A2 = aircraft("A2", "AF", "F-80C", "A1-2308", "W", 10, 2.0, "CL")
endtestsetup()
startgameturn()
A1.move("LVL", "M", "LRL/H,H/L")
A1._assert("A1-1609       WNW  10", 2.0)
A2.move("LVL", "M", "LRR/H,H/R")
A2._assert("A1-2208       WSW  10", 2.0)
endgameturn()

starttestsetup(sheets=[["A1"]])
A1 = aircraft("A1", "AF", "F-80C", "A1-1708", "WSW", 10, 2.0, "CL")
A2 = aircraft("A2", "AF", "F-80C", "A1-2308", "WSW", 10, 2.0, "CL")
endtestsetup()
startgameturn()
A1.move("LVL", "M", "LRL/H,H/L")
A1._assert("A1-1610       W    10", 2.0)
A2.move("LVL", "M", "LRR/H,H/R")
A2._assert("A1-2108       SSW  10", 2.0)
endgameturn()

starttestsetup(sheets=[["A1"]])
A1 = aircraft("A1", "AF", "F-80C", "A1-1708", "SSW", 10, 2.0, "CL")
A2 = aircraft("A2", "AF", "F-80C", "A1-2308", "SSW", 10, 2.0, "CL")
endtestsetup()
startgameturn()
A1.move("LVL", "M", "LRL/H,H/L")
A1._assert("A1-1709       WSW  10", 2.0)
A2.move("LVL", "M", "LRR/H,H/R")
A2._assert("A1-2209       S    10", 2.0)
endgameturn()

starttestsetup(sheets=[["A1"]])
A1 = aircraft("A1", "AF", "F-80C", "A1-1708", "S", 10, 2.0, "CL")
A2 = aircraft("A2", "AF", "F-80C", "A1-2308", "S", 10, 2.0, "CL")
endtestsetup()
startgameturn()
A1.move("LVL", "M", "LRL/H,H/L")
A1._assert("A1-1810       SSW  10", 2.0)
A2.move("LVL", "M", "LRR/H,H/R")
A2._assert("A1-2210       SSE  10", 2.0)
endgameturn()

starttestsetup(sheets=[["A1"]])
A1 = aircraft("A1", "AF", "F-80C", "A1-1708", "SSE", 10, 2.0, "CL")
A2 = aircraft("A2", "AF", "F-80C", "A1-2308", "SSE", 10, 2.0, "CL")
endtestsetup()
startgameturn()
A1.move("LVL", "M", "LRL/H,H/L")
A1._assert("A1-1809       S    10", 2.0)
A2.move("LVL", "M", "LRR/H,H/R")
A2._assert("A1-2309       ESE  10", 2.0)
endgameturn()

starttestsetup(sheets=[["A1"]])
A1 = aircraft("A1", "AF", "F-80C", "A1-1708", "ESE", 10, 2.0, "CL")
A2 = aircraft("A2", "AF", "F-80C", "A1-2308", "ESE", 10, 2.0, "CL")
endtestsetup()
startgameturn()
A1.move("LVL", "M", "LRL/H,H/L")
A1._assert("A1-1908       SSE  10", 2.0)
A2.move("LVL", "M", "LRR/H,H/R")
A2._assert("A1-2410       E    10", 2.0)
endgameturn()

# Check we can carry preparatory HFPs from one turn to the next.

starttestsetup(verbose=False)
A1 = aircraft("A1", "AF", "F-104A", "A1-1715", "N", 10, 7.0, "CL")
endtestsetup()
startgameturn()
A1.move("LVL", 0.5, "H,H,H,H,H,H,LRL/H")
A1._assert("A1-1708       N    10", 7.0)
endgameturn()

startgameturn()
A1.move("LVL", 0.5, "H,H/L,H,H,H,H,H")
A1._assert("A1-1803/1903 NNE 10", 7.0)
endgameturn()

# Check unloaded HFPs are not counted as preparatory HFPs.

starttestsetup(verbose=False)
A1 = aircraft("A1", "AF", "F-104A", "A1-1715", "N", 10, 7.0, "CL")
endtestsetup()
startgameturn()
A1.move("UD", "AB", "H,LRL/HU,H,H/L,H,H,H")
asserterror("attempt to roll without sufficient preparatory FPs.")
startgameturn()
A1.move("UD", "AB", "H,LRL/HU,HU,H,H/L,H,H")
asserterror("attempt to roll without sufficient preparatory FPs.")
startgameturn()
A1.move("UD", "AB", "H,LRL/H,HU,HU,H,H/L")
A1._assert("A1-1610 NNE 10", 7.0)

# Check VFPs are counted as preparatory HFPs.

starttestsetup(verbose=False)
A1 = aircraft("A1", "AF", "F-104A", "A1-1715", "N", 10, 7.0, "CL")
endtestsetup()
startgameturn()
A1.move("SD", "AB", "H,LRL/D,D,H/L,H,H,H")
A1._assert("A1-1711/1812 NNE 8", 8.0)
startgameturn()
A1.move("SD", "AB", "H,LRL/H,D,H/L,H,H,D")
A1._assert("A1-1711 NNE 8", 8.0)
startgameturn()
A1.move("SD", "AB", "H,LRL/H,H,D,H/L,D,D")
A1._assert("A1-1612       NNE   7", 8.5)
startgameturn()
A1.move("ZC", "AB", "H,LRL/C,H/L,H,H,H,H")
asserterror("attempt to roll without sufficient preparatory FPs.")
startgameturn()
A1.move("ZC", "AB", "H,LRL/H,C/L,H,H,H,H")
asserterror("attempt to roll without sufficient preparatory FPs.")
startgameturn()
A1.move("ZC", "AB", "H,LRL/H,H,C,H/L,C,C")
A1._assert("A1-1612       NNE  13", 7.0)
endgameturn()

startgameturn()
A1.move("ZC", "AB", "H,LRL/C,H,H/L,H,H")
A1._assert("A1-1908 ENE 14", 7.0)
startgameturn()
A1.move("LVL", "M", "H,H,H,H,H,H")
A1._assert("A1-1907       NNE  13", 7.0)
endgameturn()

# Check the required preparatory HFPs, both at subsonic and supersonic speeds.

starttestsetup(verbose=False)
A1 = aircraft("A1", "AF", "F-104A", "A1-1715", "N", 7, 7.0, "CL")
A2 = aircraft("A2", "AF", "F-104A", "A1-1915", "N", 7, 7.5, "CL")
A3 = aircraft("A3", "AF", "F-104A", "A1-2115", "N", 20, 6.5, "CL")
A4 = aircraft("A4", "AF", "F-104A", "A1-2315", "N", 20, 7.0, "CL")
endtestsetup()
startgameturn()
A1.move("LVL", "AB", "H,LRL/H,H/L,H,H,H,H")
asserterror("attempt to roll without sufficient preparatory FPs.")
startgameturn()
A2.move("LVL", "AB", "H,LRL/H,H,H/L,H,H,H")
asserterror("attempt to roll without sufficient preparatory FPs.")
startgameturn()
A3.move("LVL", "AB", "H,LRL/H,H/L,H,H,H")
asserterror("attempt to roll without sufficient preparatory FPs.")
startgameturn()
A4.move("LVL", "AB", "H,LRL/H,H,H/L,H,H,H")
asserterror("attempt to roll without sufficient preparatory FPs.")
startgameturn()
A1.move("LVL", "AB", "H,LRL/H,H,H/L,H,H,H")
A1._assert("A1-1709/1810 NNE 7", 7.5)
startgameturn()
A2.move("LVL", "AB", "H,LRL/H,H,H,H/L,H,H")
A2._assert("A1-1909 NNE 7", 7.5)
startgameturn()
A3.move("LVL", "AB", "H,LRL/H,H,H/L,H,H")
A3._assert("A1-2110 NNE 20", 7.0)
startgameturn()
A4.move("LVL", "AB", "H,LRL/H,H,H,H/L,H,H")
A4._assert("A1-2309 NNE 20", 7.0)
endgameturn()

# Check additional preparatory HFPs required at altitude.

starttestsetup(verbose=False)
A1 = aircraft("A1", "AF", "F-104A", "A1-1515", "N", 20, 12.0, "CL")
A2 = aircraft("A2", "AF", "F-104A", "A1-1715", "N", 30, 12.0, "CL")
A3 = aircraft("A3", "AF", "F-104A", "A1-1915", "N", 40, 12.0, "CL")
A4 = aircraft("A4", "AF", "F-104A", "A1-2115", "N", 50, 12.0, "CL")
A5 = aircraft("A5", "AF", "F-104A", "A1-2315", "N", 61, 12.0, "CL")

endtestsetup()
startgameturn()
A1.move("LVL", "AB", "H,LRL/H,H,H,H,H/L,H,H,H,H,H,H")
asserterror("attempt to roll without sufficient preparatory FPs.")
startgameturn()
A1.move("LVL", "AB", "H,LRL/H,H,H,H,H,H/L,H,H,H,H,H")
A1._assert("A1-1605/1705 NNE 20", 12.0)
startgameturn()
A2.move("LVL", "AB", "H,LRL/H,H,H,H,H,H/L,H,H,H,H,H")
asserterror("attempt to roll without sufficient preparatory FPs.")
startgameturn()
A2.move("LVL", "AB", "H,LRL/H,H,H,H,H,H,H/L,H,H,H,H")
A2._assert("A1-1805 NNE 30", 12.5)
startgameturn()
A3.move("LVL", "AB", "H,LRL/H,H,H,H,H,H,H/L,H,H,H,H")
asserterror("attempt to roll without sufficient preparatory FPs.")
startgameturn()
A3.move("LVL", "AB", "H,LRL/H,H,H,H,H,H,H,H/L,H,H,H")
A3._assert("A1-1904/2005 NNE 40", 12.0)
startgameturn()
A4.move("LVL", "AB", "H,LRL/H,H,H,H,H,H,H,H/L,H,H,H")
asserterror("attempt to roll without sufficient preparatory FPs.")
startgameturn()
A4.move("LVL", "AB", "H,LRL/H,H,H,H,H,H,H,H,H/L,H,H")
A4._assert("A1-2104 NNE 50", 12.0)
startgameturn()
A5.move("LVL", "AB", "H,LRL/H,H,H,H,H,H,H,H,H/L,H,H")
asserterror("attempt to roll without sufficient preparatory FPs.")
startgameturn()
A5.move("LVL", "AB", "H,LRL/H,H,H,H,H,H,H,H,H,H/L,H")
A5._assert("A1-2204/2304 NNE 61", 12.0)
endgameturn()


# Check allowed flight types.

starttestsetup()
A1 = aircraft("A1", "AF", "F-80C", "A1-1415", "N", 20, 4.0, "CL")
A2 = aircraft("A2", "AF", "F-80C", "A1-1615", "N", 20, 4.0, "CL")
endtestsetup()

startgameturn()
A1.move("SC", "M", "LRL/H,H,H,H")
asserterror("attempt to declare a lag roll while flight type is SC.")
startgameturn()
A2.move("SC", "M", "LRR/H,H,H,H")
asserterror("attempt to declare a lag roll while flight type is SC.")
startgameturn()
A1.move("SC", "M", "H,H,H,C")
A2.move("SC", "M", "H,H,H,C")
endgameturn()

startgameturn()
A1.move("VC", "M", "LRL/H,C2,C2,C2")
asserterror("attempt to declare a lag roll while flight type is VC.")
startgameturn()
A2.move("VC", "M", "LRR/H,C2,C2,C2")
asserterror("attempt to declare a lag roll while flight type is VC.")
startgameturn()
A1.move("SD", "M", "H,H,H,D")
A2.move("SD", "M", "H,H,H,D")
endgameturn()

startgameturn()
A1.move("VD", "M", "LRL/H,H,D2,D2,D2")
asserterror("attempt to declare a lag roll while flight type is VD.")
startgameturn()
A2.move("VD", "M", "LRR/H,H,D2,D2,D2")
asserterror("attempt to declare a lag roll while flight type is VD.")
startgameturn()
A1.move("SD", "M", "H,H,H,H")
A2.move("SD", "M", "H,H,H,H")
endgameturn()


# TODO: Check multiple rolls in one turn.

# The issue is the F-104A is GSSM.

# checkstarttestsetup(verbose=True)
# A1 = aircraft("A1", "AF", "F-104A", "A1-1715", "N", 20, 12.0, "CL")
# checkendtestsetup()
# checkstartgameturn()
# A1.move("LVL",  "AB", "LRL/H,H,H/L,LRR/H,H,H/R,LRL/H,H,H/L,LRR/H,H,H/R")
# A1._assert("A1-1906       N    20",  11.5)
# A1.move("LVL",  "AB", "LRL/H,H,H/L,H,H,H,H,H,H,LRR/H,H,H/R"          )
# A1._assert("A1-2106       N    20",  12.0)
# A1.move("ZC" ,  "AB", "LRL/H,H,H/L,H,C,C,C,C,H,LRR/H,H,H/R"          )
# A1._assert("A1-1909       N    24",  11.5)
# A1.move("SD" ,  "AB", "LRL/H,H,H/L,H,D,D,D,D,H,LRR/H,H,H/R"          )
# A1._assert("A1-1909       N    16",  10.5)
# checkendgameturn()

# Check we can select the bank after a DR.

starttestsetup(verbose=False)
A1 = aircraft("A1", "AF", "F-80C", "A1-1715", "N", 20, 4.0, "CL")

endtestsetup()
startgameturn()
A1.move("LVL", "M", "LRL/H,H/L/BL,EZR/H,H")
asserterror("attempt to declare a turn to R while banked to L.")
startgameturn()
A1.move("LVL", "M", "LRL/H,H/L/WL,EZR/H,H")
A1._assert("A1-1712       NNE  20", 4.0)
startgameturn()
A1.move("LVL", "M", "LRL/H,H/L/BR,EZR/H,H")
A1._assert("A1-1712       NNE  20", 4.0)
startgameturn()
A1.move("LVL", "M", "LRR/H,H/R/BL,EZR/H,H")
asserterror("attempt to declare a turn to R while banked to L.")
startgameturn()
A1.move("LVL", "M", "LRR/H,H/R/WL,EZR/H,H")
A1._assert("A1-1712       NNW  20", 4.0)
startgameturn()
A1.move("LVL", "M", "LRR/H,H/R/BR,EZR/H,H")
A1._assert("A1-1712       NNW  20", 4.0)
startgameturn()
A1.move("LVL", "M", "LRL/H,H/L/BR,EZL/H,H")
asserterror("attempt to declare a turn to L while banked to R.")
startgameturn()
A1.move("LVL", "M", "LRL/H,H/L/WL,EZL/H,H")
A1._assert("A1-1712       NNE  20", 4.0)
startgameturn()
A1.move("LVL", "M", "LRL/H,H/L/BL,EZL/H,H")
A1._assert("A1-1712       NNE  20", 4.0)
startgameturn()
A1.move("LVL", "M", "LRR/H,H/R/BR,EZL/H,H")
asserterror("attempt to declare a turn to L while banked to R.")
startgameturn()
A1.move("LVL", "M", "LRR/H,H/R/WL,EZL/H,H")
A1._assert("A1-1712       NNW  20", 4.0)
startgameturn()
A1.move("LVL", "M", "LRR/H,H/R/BL,EZL/H,H")
A1._assert("A1-1712       NNW  20", 4.0)
endgameturn()

# Rolls and GSSM/PSSM aircraft

# F-104A is GSSM, F-102A is PSSM, and F-100A is neither.

starttestsetup(verbose=False)
A1 = aircraft("A1", "AF", "F-104A", "A1-1215", "N", 20, 7.5, "CL")  # GSSM
A2 = aircraft("A2", "AF", "F-100A", "A1-1415", "N", 20, 7.5, "CL")
A3 = aircraft("A3", "AF", "F-102A", "A1-1615", "N", 20, 7.5, "CL")  # PSSM
endtestsetup()

startgameturn()

A1.move("LVL", "AB", "H,H,H,H,H,H,H")
A1._assert("A1-1208       N    20", 8.0)
A2.move("LVL", "AB", "H,H,H,H,H,H,H")
A2._assert("A1-1408       N    20", 7.5)
A3.move("LVL", "AB", "H,H,H,H,H,H,H")
A3._assert("A1-1608       N    20", 7.5)

startgameturn()

A1.move("LVL", "AB", "LRR/H,H,H,H/R,H,H,H")
A1._assert("A1-1109/1209 NNW 20", 8.0)
A2.move("LVL", "AB", "LRR/H,H,H,H/R,H,H,H")
A2._assert("A1-1309/1409 NNW 20", 7.5)
A3.move("LVL", "AB", "LRR/H,H,H,H/R,H,H,H")
A3._assert("A1-1509/1609 NNW 20", 7.5)

endgameturn()

# Additional prepatory FPs in version 2.4.

starttestsetup(verbose=False)
A1 = aircraft("A1", "AF", "F-104A", "A2-2025", "N", 20, 4.0, "CL")
A2 = aircraft("A2", "AF", "F-104A", "A2-2225", "N", 20, 5.0, "CL")
A3 = aircraft("A3", "AF", "F-104A", "A2-2425", "N", 20, 6.0, "CL")
endtestsetup()

startgameturn()
A1.move("LVL", "M", "LRR/H/R,H,H,H")
asserterror("attempt to roll without sufficient preparatory FPs.")
A2.move("LVL", "M", "LRR/H/R,H,H,H,H")
asserterror("attempt to roll without sufficient preparatory FPs.")
A3.move("LVL", "M", "LRR/H,H/R,H,H,H,H")
asserterror("attempt to roll without sufficient preparatory FPs.")

startgameturn()
A1.move("LVL", "M", "LRR/H,H/R,H,H")
A1._assert("A2-2022       NNW  20", 4.0)
A2.move("LVL", "M", "LRR/H,H/R,H,H,H")
A2._assert("A2-2121/2221 NNW 20", 5.0)
A3.move("LVL", "M", "LRR/H,H,H/R,H,H,H")
A3._assert("A2-2320/2420  NNW  20", 6.0)
endgameturn()

# In version 2.4, the preparatory FPs can be HFPs or VFPs, but the roll must
# be executed on an HFP.

starttestsetup()
A1 = aircraft("A1", "AF", "F-104A", "A2-2025", "N", 20, 6.0, "CL")
endtestsetup()

startgameturn()
A1.move("ZC", "M", "H,H,H,H,H,C")
endgameturn()

startgameturn()
A1.move("ZC", "M", "LRR/C,C,C/R")
asserterror("attempt to roll on a VFP.")

startgameturn()
A1.move("ZC", "M", "LRR/C,C,H/R,H,H,H")
A1._assert("A2-1917/2017 NNW 23", 6.0)
endgameturn()

endfile(__file__)
