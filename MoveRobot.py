#!/usr/bin/python
# -*- coding: utf-8 -*-
from Motor import Motor
class MoveRobot:
    angle = 0
    distance = 0
    MotorLeft = Motor(200,1)    #spr,port
    MotorRight = Motor(200,2)   #spr,port
    

    def drive(self, distance):
        print("Robot driving")
        MotorLeft.drive(distance)
        MotorRight.drive(distance)
    def turn(self, angle):
        """Steps per Revolution = 360⁰ / Step Angle, Basis Winkel bei uns = 1.8°"""
        print("turning")
        self.angle = self.angle + angle #Wert vom Winkel abspeichern
        if angle > 0:   #nach rechts drehen
            while angle > 0:
                MotorLeft.driveInStep(1)
                angle = angle - (360 / MotorLeft.stepsPerRevolution) #=1.8° bei spr=200
        elif angle < 0: #nach links drehen
            while angle < 0:
                MotorRight.driveInStep(1)
                angle = angle + (360 / MotorRight.stepsPerRevolution)
    def setSpeed(self, rpm):
        MotorLeft.setSpeed(rpm)
        MotorRight.setSpeed(rpm)
        print("Speed is set")
