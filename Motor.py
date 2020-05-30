#-*- coding: utf-8 -*-
#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor

import time
import atexit
import math


class Motor:
    motor = Adafruit_MotorHAT()
    myMotor = motor.getStepper(200,2)
    stepsPerRevolution = 0
    rpm =30    #60 round per Minutes
    port = 0    #Port Number
    distance = 0
    def __init__(self, stepsPerRevolution, port):
        self.stepsPerRevolution = stepsPerRevolution
        self.port = port
        self.myMotor = self.motor.getStepper(stepsPerRevolution, port)
        
    def drive(self, distance):
        self.distance = distance
        self.myMotor.setSpeed(self.rpm)
        revolutions = abs(distance/math.pi*0.1)  #Durchmesser der Räder = 100 mm
        steps = int(2*self.stepsPerRevolution*revolutions)
        if distance > 0:                         #Fahre vorwaerts
            self.myMotor.step(steps, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.DOUBLE)
        else:                                   #Fahre rueckwaerts
            self.myMotor.step(steps, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.DOUBLE)
        return steps
    def stop(self):
        self.myMotor.setSpeed(1)
    def setSpeed(self, rpm):
        self.rpm = rpm
    def getDistance(self):
        return distance
    def driveInStep(self,steps): #Um den Roboter zu drehen, nur nach vorne
        self.myMotor.step(steps, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.SINGLE)

'''def turnOffMotors():
    mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)
atexit.register(turnOffMotors)
'''
