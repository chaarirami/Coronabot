#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor

import time
import atexit
import math


class Motor:
    motor = Adafruit_MotorHAT()
    myMotor = motor.getStepper(200,2)
    stepsPerRevolution = 0
    rpm = 20    #round per Minutes
    port = 0    #Port Number
    distance = 0
    def __init__(self, stepsPerRevolution, port):
        self.stepsPerRevolution = stepsPerRevolution
        self.port = port
        self.myMotor = self.motor.getStepper(stepsPerRevolution, port)

    def turnOffMotors():
        motor.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
        motor.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
        motor.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
        motor.getMotor(4).run(Adafruit_MotorHAT.RELEASE)


    def drive(self, distance):
        self.distance = distance
        self.myMotor.setSpeed(self.rpm)
        revolutions = abs(distance/math.pi*100)  #Durchmesser der Rad = 100 mm
        steps = int(self.stepsPerRevolution*revolutions)
        if distance > 0:                         #Fahre vorwaerts
            self.myMotor.step(steps, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.DOUBLE)
        else:                                   #Fahre rueckwaerts
            self.myMotor.step(steps, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.DOUBLE)
    def stop():
        motor.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
        motor.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
        motor.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
        motor.getMotor(4).run(Adafruit_MotorHAT.RELEASE)
    def setSpeed(self, rpm):
        self.rpm = rpm
    def getDistance(self):
        return distance
    def driveInStep(self,steps): #Um den Roboter zu drehen, nur nach vorne
        self.myMotor.step(steps, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.SINGLE)
