from apxo.tests.infrastructure import *

startfile(__file__, "collision with terrain")

from apxo.tests.infrastructure import *

starttestsetup(sheets=[["C2"]])
A1 = aircraft("A1", "AF", "F-80C", "C2-6625", "WSW", 1, 4.0, "CL")
A2 = aircraft("A2", "AF", "F-80C", "C2-6624", "WSW", 1, 4.0, "CL")
A3 = aircraft("A3", "AF", "F-80C", "C2-6623", "WSW", 2, 4.0, "CL")
A4 = aircraft("A4", "AF", "F-80C", "C2-6628/6727", "NNW", 1, 4.0, "CL")
endtestsetup()

startgameturn()
A1.move("LVL", "M", "H,H,H,H")
A1._assert("C2-6227       WSW   1", 4.0)
A2.move("LVL", "M", "H,H,H,H")
A2._assert("C2-6425       WSW   1", 4.0)
A3.move("LVL", "M", "H,H,H,H")
A3._assert("C2-6225       WSW   2", 4.0)
A4.move("LVL", "M", "H,H,H,H")
A4._assert("C2-6526/6626  NNW   1", 4.0)
endgameturn()

starttestsetup(sheets=[["B2"]])
A1 = aircraft("A1", "AF", "F-80C", "B2-4228", "ENE", 2, 4.0, "CL")
A2 = aircraft("A2", "AF", "F-80C", "B2-4227", "ENE", 2, 4.0, "CL")
A3 = aircraft("A3", "AF", "F-80C", "B2-4226", "ENE", 3, 4.0, "CL")
A4 = aircraft("A4", "AF", "F-80C", "B2-4526/4627", "NNE", 2, 4.0, "CL")
endtestsetup()

startgameturn()
A1.move("LVL", "M", "H,H,H,H")
A1._assert("B2-4626       ENE   2", 4.0)
A2.move("LVL", "M", "H,H,H,H")
A2._assert("B2-4525       ENE   2", 4.0)
A3.move("LVL", "M", "H,H,H,H")
A3._assert("B2-4624       ENE   3", 4.0)
A4.move("LVL", "M", "H,H,H,H")
A4._assert("B2-4625/4725  NNE   2", 4.0)
endgameturn()

starttestsetup(sheets=[["B2"]], levelincrement=2)
A1 = aircraft("A1", "AF", "F-80C", "B2-4228", "ENE", 2, 4.0, "CL")
A2 = aircraft("A2", "AF", "F-80C", "B2-4227", "ENE", 2, 4.0, "CL")
A3 = aircraft("A3", "AF", "F-80C", "B2-4226", "ENE", 3, 4.0, "CL")
A4 = aircraft("A4", "AF", "F-80C", "B2-4526/4627", "NNE", 2, 4.0, "CL")
endtestsetup()

startgameturn()
A1.move("LVL", "M", "H,H,H,H")
A1._assert("B2-4327 ENE 2", 4.0)
A2.move("LVL", "M", "H,H,H,H")
A2._assert("B2-4426 ENE 2", 4.0)
A3.move("LVL", "M", "H,H,H,H")
A3._assert("B2-4524 ENE 4", 4.0)
A4.move("LVL", "M", "H,H,H,H")
A4._assert("B2-4626 NNE 2", 4.0)
endgameturn()

starttestsetup(sheets=[["B2"]], levelincrement=2, leveloffset=-1)
A1 = aircraft("A1", "AF", "F-80C", "B2-4228", "ENE", 2, 4.0, "CL")
A2 = aircraft("A2", "AF", "F-80C", "B2-4227", "ENE", 2, 4.0, "CL")
A3 = aircraft("A3", "AF", "F-80C", "B2-4226", "ENE", 3, 4.0, "CL")
A4 = aircraft("A4", "AF", "F-80C", "B2-4526/4627", "NNE", 2, 4.0, "CL")
endtestsetup()

startgameturn()
A1.move("LVL", "M", "H,H,H,H")
A1._assert("B2-4626       ENE   2", 4.0)
A2.move("LVL", "M", "H,H,H,H")
A2._assert("B2-4525       ENE   2", 4.0)
A3.move("LVL", "M", "H,H,H,H")
A3._assert("B2-4624       ENE   3", 4.0)
A4.move("LVL", "M", "H,H,H,H")
A4._assert("B2-4625/4725  NNE   2", 4.0)
endgameturn()

endfile(__file__)
