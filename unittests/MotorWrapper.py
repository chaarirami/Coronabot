#!/usr/bin/python

import time
import atexit
import math

class Adafruit_MotorHAT:
    FORWARD= 0
    BACKWARD= 0
    DOUBLE= 0
    SINGLE= 0
    stepsPerRevolution=0
    port=0
    steps=0

    def __init__(self, stepsPerRevolution, port):
        self.stepsPerRevolution=stepsPerRevolution
        self.port = port

    def step(self, steps, direction, stepsize):
        self.steps=steps

class Motor:
    distance = 0
    stepsPerRevolution = 0
    myMotor = 0
    rpm=0
    def __init__(self, stepsPerRevolution, port):
        self.stepsPerRevolution = stepsPerRevolution
        self.port = port
        self.myMotor = Adafruit_MotorHAT(stepsPerRevolution, port)

    def drive(self, distance):
        self.distance = distance
        revolutions = abs(distance/math.pi*100)  #Durchmesser der Rad = 100 mm
        steps = int(self.stepsPerRevolution*revolutions)
        if distance > 0:                         #Fahre vorwaerts
            self.myMotor.step(steps, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.DOUBLE)
        else:                                   #Fahre rueckwaerts
            self.myMotor.step(steps, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.DOUBLE)
        return steps
    def stop(self):
        self.distance = 0
    def setSpeed(self, rpm):
        self.rpm = rpm
    def getDistance(self):
        return self.distance
    def driveInStep(self,steps): #Um den Roboter zu drehen, nur nach vorne
        self.myMotor.step(steps, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.SINGLE)