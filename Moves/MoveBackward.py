import time

# Move: Move Backward

deg = 25
midFloor = 30
hipSwing = 25
pause = 0.1
steptime = 0.05

# tripod1 = RF,LM,RB
# tripod2 = LF,RM,LB

for timeStop in range(2):
    # replant tripod2 backwards while tripod1 moves forward
    #   relpant tripod 2 backwards
    hexy.LF.replantFoot(deg+hipSwing,stepTime=steptime)
    hexy.RM.replantFoot(-hipSwing,stepTime=steptime)
    hexy.LB.replantFoot(-deg+hipSwing,stepTime=steptime)

    #   tripod1 moves forward
    hexy.RF.setHipDeg(-deg+hipSwing,stepTime=steptime)
    hexy.LM.setHipDeg(-hipSwing,stepTime=steptime)
    hexy.RB.setHipDeg(deg+hipSwing,stepTime=steptime)
    time.sleep(pause)

    # replant tripod1 backwards while tripod2 moves behind
    #   replant tripod1 backwards
    hexy.RF.replantFoot(-deg-hipSwing,stepTime=steptime)
    hexy.LM.replantFoot(hipSwing,stepTime=steptime)
    hexy.RB.replantFoot(deg-hipSwing,stepTime=steptime)

    #   tripod2 moves behind
    hexy.LF.setHipDeg(deg-hipSwing,stepTime=steptime)
    hexy.RM.setHipDeg(hipSwing,stepTime=steptime)
    hexy.LB.setHipDeg(-deg-hipSwing,stepTime=steptime)
    time.sleep(pause)

