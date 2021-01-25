#!/usr/bin/python
# -*- coding: utf-8 -*-
from MotorWrapper import Motor, Adafruit_MotorHAT
import threading

class MoveRobot:
    angle = 0
    totalAngle = 0
    distance = 0
    MotorLeft = Motor(200,2)    #spr,port
    MotorRight = Motor(200,1)   #spr,port
    

    def drive(self, distance):
        self.distance=distance
        if distance > 0:
            dir = Adafruit_MotorHAT.FORWARD
        elif distance < 0:
            dir = Adafruit_MotorHAT.BACKWARD
    def turn(self, angle):
        self.totalAngle=angle
        self.angle = self.angle + angle #Wert vom Winkel abspeichern
        if angle > 0:   #nach rechts drehen
            while self.angle > 0:
                self.MotorLeft.driveInStep(1)
                self.angle = self.angle - (360 / self.MotorLeft.stepsPerRevolution) #=1.8° bei spr=200
        elif angle < 0: #nach links drehen
            while angle < 0:
                self.MotorRight.driveInStep(1)
                self.angle = self.angle + (360 / self.MotorRight.stepsPerRevolution)
    def setSpeed(self, rpm):
        self.MotorLeft.setSpeed(rpm)
        self.MotorRight.setSpeed(rpm)
        print("Speed is set")
    def getDistance(self):
        return self.distance
    def getAngle(self):
        return self.totalAngle
    def stepper_worker(stepper, numsteps, direction, style):
    #print("Steppin!")
        stepper.step(numsteps, direction, style)
    #print("Done")
