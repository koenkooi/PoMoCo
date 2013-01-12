import time

# Move: Crab Right

for timeStop in range(3):
    hexy.LF.ankle(-60)
    hexy.LM.ankle(-60)
    hexy.LB.ankle(-60)

    hexy.RF.ankle(0)
    hexy.RM.ankle(0)
    hexy.RB.ankle(0)

    hexy.LF.knee(75)
    hexy.LM.knee(75)
    hexy.LB.knee(75)

    hexy.RF.knee(60)
    hexy.RM.knee(60)
    hexy.RB.knee(60)

    time.sleep(0.1)

    hexy.LF.ankle(0)
    hexy.LM.ankle(0)
    hexy.LB.ankle(0)

    hexy.RF.ankle(-60)
    hexy.RM.ankle(-60)
    hexy.RB.ankle(-60)

    hexy.LF.knee(60)
    hexy.LM.knee(60)
    hexy.LB.knee(60)

    hexy.RF.knee(75)
    hexy.RM.knee(75)
    hexy.RB.knee(75)

    time.sleep(0.1)

    move('Reset')
