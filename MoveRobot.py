#!/usr/bin/python
# -*- coding: utf-8 -*-
from Motor import Motor
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor
import threading
class MoveRobot:
    angle = 0
    distance = 0
    MotorLeft = Motor(200,2)    #spr,port
    MotorRight = Motor(200,1)   #spr,port
    

    def drive(self, distance):
        print("Robot driving")
        if distance > 0:
            dir = Adafruit_MotorHAT.FORWARD
        elif distance < 0:
            dir = Adafruit_MotorHAT.BACKWARD
        st1 = threading.Thread(target=self.stepper_worker, args=(self.MotorLeft,self.MotorLeft.drive(distance) , dir, Adafruit_MotorHAT.SINGLE))
        st1.start()
        st2 = threading.Thread(target=self.stepper_worker, args=(self.MotorRight,self.MotorRight.drive(distance) , dir, Adafruit_MotorHAT.SINGLE))
        st1.start()
    def turn(self, angle):
        """Steps per Revolution = 360⁰ / Step Angle, Basis Winkel bei uns = 1.8°"""
        print("turning")
        self.angle = self.angle + angle #Wert vom Winkel abspeichern
        if angle > 0:   #nach rechts drehen
            while angle > 0:
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
    def stepper_worker(stepper, numsteps, direction, style):
    #print("Steppin!")
        stepper.step(numsteps, direction, style)
    #print("Done")
