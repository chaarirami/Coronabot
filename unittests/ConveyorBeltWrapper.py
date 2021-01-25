from MotorWrapper import Motor
true = 1

class ConveyorBelt:
    distance = 0
    motorConveyorBelt = Motor(200,3)
    def driveForward(self):
        #while(not self.objectDetected):
            self.distance = 10
            self.motorConveyorBelt.drive(10)
    def driveBackward(self):
        #while(not self.objectDetected):
            self.distance = -10
            self.motorConveyorBelt.drive(-10)
    def stop(self):
        self.motorConveyorBelt.stop()
        self.distance = 0
    def getDistance(self):
        return self.distance