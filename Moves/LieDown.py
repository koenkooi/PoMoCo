import time, math

# Move: Lie Down

stepPerS = 5

footMax = -20
footMin = 0 #floor
footRange = abs(footMax-footMin)

moveDuration = 1
moveSteps = math.ceil(stepPerS * moveDuration)

steps = range(int(moveSteps))
for i,t in enumerate(steps):

    newY = footMin - i * (footRange / (moveSteps - 1))
    print "i: %s t: %s newY: %s footRange: %s moveSteps: %s" % ( i, t, newY, footRange, moveSteps )
	
    hexy.LF.setFootY(newY, stepTime=0)
    hexy.LM.setFootY(newY, stepTime=0)
    hexy.LB.setFootY(newY, stepTime=0)

    hexy.RF.setFootY(newY, stepTime=0)
    hexy.RM.setFootY(newY, stepTime=0)
    hexy.RB.setFootY(newY, stepTime=0)
    time.sleep(moveDuration/moveSteps)

#hexy.con.killAll()
