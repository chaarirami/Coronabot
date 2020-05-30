#-*- coding: utf-8 -*-
#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor

#from Lightbarrier import Lightbarrier
from Motor import Motor
class ConveyorBelt:
    #lightBarrier = LightBarrier()
    #motorConveyorBelt = Motor()
    objectDetected = False
    conveyor = Adafruit_MotorHAT(addr=0x61) #Förderband
    motorConveyorBelt = conveyor.getStepper(200,1)
    def driveForward(self):
        print("driving forward")
        motorConveyorBelt.setSpeed(200)
        while(not self.objectDetected):
            motorConveyor.step(10, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.DOUBLE)
    def driveBackward(self):
        print("driving backwards")
        motorConveyorBelt.setSpeed(200)
        while(not self.objectDetected):
            motorConveyor.step(10, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.DOUBLE)
    def stop(self):
        print("Stop")
        motorConveyorBelt.setSpeed(0)
