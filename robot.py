import time
import math

from servitorComm import runMovement

#modifies how smoothly the servos move
#smoother means more processing power, and fills the serial line
#lower if movements start to slow down, or get weird
#Anything higher than 50 is pointless (maximum refresh of standard servos)
stepPerS = 50

# Determines the plane on which all feet will rest
floor = 60

class hexapod():

    def __init__(self,con):
        self.con = con
        self.RF = leg(con,'frontRight',0,1,2)
        self.RM   = leg(con,'midRight',4,5,6)
        self.RB  = leg(con,'backRight',8,9,10)

        self.LF  = leg(con,'frontLeft',16,17,18)
        self.LM    = leg(con,'midLeft',20,21,22)
        self.LB   = leg(con,'backLeft',24,25,26)

        self.legs = [self.RF,
                     self.RM,
                     self.RB,
                     self.LF,
                     self.LM,
                     self.LB]

        self.neck = neck(con,31)

        self.tripod1 = [self.RF,self.RB,self.LM]
        self.tripod2 = [self.LF,self.LB,self.RM]

class neck():
    def __init__(self,con,servoNum):
        self.con = con
        self.servoNum = servoNum

    def set(self,deg):
        self.con.servos[self.servoNum].setPos(deg=deg)

class leg():

    def __init__(self,con,name,hipServoNum,kneeServoNum,ankleServoNum,simOrigin=(0,3,0)):
        self.con = con
        self.name = name
        self.hipServoNum = hipServoNum
        self.kneeServoNum = kneeServoNum
        self.ankleServoNum = ankleServoNum

    def hip(self, deg):
        self.con.servos[self.hipServoNum].setPos(deg=deg)

    def knee(self, deg):
        self.con.servos[self.kneeServoNum].setPos(deg=deg)

    def ankle(self, deg):
        self.con.servos[self.ankleServoNum].setPos(deg=deg)

    def setHipDeg(self,endHipAngle,stepTime=1):
        runMovement(self.setHipDeg_function,endHipAngle,stepTime)

    def setFootY(self,footY,stepTime=1):
        runMovement(self.setFootY_function,footY,stepTime)

    def replantFoot(self,endHipAngle,stepTime=1):
        runMovement(self.replantFoot_function,endHipAngle,stepTime)

    def setHipDeg_function(self,endHipAngle,stepTime):
        currentHipAngle = self.con.servos[self.hipServoNum].getPosDeg()
        hipMaxDiff = endHipAngle-currentHipAngle

        steps = range(int(stepPerS))
        for i,t in enumerate(steps):
            # TODO: implement time-movements the servo commands sent for far fewer
            #       total servo commands
            hipAngle = (hipMaxDiff/len(steps))*(i+1)
            try:
                anglNorm=hipAngle*(180/(hipMaxDiff))
            except:
                anglNorm=hipAngle*(180/(1))
            hipAngle = currentHipAngle+hipAngle
            self.con.servos[self.hipServoNum].setPos(deg=hipAngle)

            #wait for next cycle
            time.sleep(stepTime/float(stepPerS))

    def setFootY_function(self,footY,stepTime):
        # TODO: max steptime dependent
        # TODO: implement time-movements the servo commands sent for far fewer
        #       total servo commands

        if (footY < 75) and (footY > -75):
            kneeAngle = math.degrees(math.asin(float(footY)/75.0))
            ankleAngle = 90-kneeAngle

            self.con.servos[self.kneeServoNum].setPos(deg=kneeAngle)
            self.con.servos[self.ankleServoNum].setPos(deg=-ankleAngle)

    def replantFoot_function(self,endHipAngle,stepTime):
    # Smoothly moves a foot from one position on the ground to another in time seconds
    # TODO: implement time-movements the servo commands sent for far fewer total servo
    #       commands

        currentHipAngle = self.con.servos[self.hipServoNum].getPosDeg()

        hipMaxDiff = endHipAngle-currentHipAngle

        steps = range(int(stepPerS))
        for i,t in enumerate(steps):

            hipAngle = (hipMaxDiff/len(steps))*(i+1)
            #print "hip angle calc'd:",hipAngle

            #calculate the absolute distance between the foot's highest and lowest point
            footMax = 0
            footMin = floor
            footRange = abs(footMax-footMin)

            #normalize the range of the hip movement to 180 deg
            try:
                anglNorm=hipAngle*(180/(hipMaxDiff))
            except:
                anglNorm=hipAngle*(180/(1))
            #print "normalized angle:",anglNorm

            #base footfall on a sin pattern from footfall to footfall with 0 as the midpoint
            footY = footMin-math.sin(math.radians(anglNorm))*footRange
            #print "calculated footY",footY

            #set foot height
            self.setFootY(footY,stepTime=0)
            hipAngle = currentHipAngle+hipAngle
            self.con.servos[self.hipServoNum].setPos(deg=hipAngle)

            #wait for next cycle
            time.sleep(stepTime/float(stepPerS))