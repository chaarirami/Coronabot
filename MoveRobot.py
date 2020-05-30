#author: Rami Chaari
#!/usr/bin/python
# -*- coding: utf-8 -*-
from Motor import Motor
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor
import threading
from multiprocessing import Process, current_process

        
class MoveRobot:
    angle = 0
    distance = 0
    MotorLeft = Motor(200,1)    #spr,port
    MotorRight = Motor(200,2)   #spr,port
    

    def drive(self, distance):
        print("Robot driving")
        process1 = Process(target = self.MotorLeft.drive, args=(distance,))
        process1.start()
        process2 = Process(target = self.MotorRight.drive, args=(distance,))                   
        process2.start()
    def turn(self, angle):
        """Steps per Revolution = 360⁰ / Step Angle, Basis Winkel bei uns = 1.8°"""
        print("turning")
        #1 Umdrehung = 98 Schritte = 360 Grad
        steps = angle*98/360
        self.MotorLeft.drive(steps)
        '''
        self.angle = self.angle + angle #Wert vom Winkel abspeichern
        if angle > 0:   #nach rechts drehen
            while angle > 0:
                self.MotorLeft.driveInStep(1)
                angle = angle - (360 / self.MotorLeft.stepsPerRevolution) #=1.8° bei spr=200
        elif angle < 0: #nach links drehen
            while angle < 0:
                self.MotorRight.driveInStep(1)
                self.angle = self.angle + (360 / self.MotorRight.stepsPerRevolution)
        '''
    def setSpeed(self, rpm):
        self.MotorLeft.setSpeed(rpm)
        self.MotorRight.setSpeed(rpm)
        print("Speed is set")
    def stop(self):
        self.MotorLeft.stop()
        self.MotorRight.stop()
    
