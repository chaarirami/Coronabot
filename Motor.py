#author: Fabian Gondeck
#-*- coding: utf-8 -*-
#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor

import time
import atexit
import math


class Motor:
    motor = Adafruit_MotorHAT(addr=0x60)                                                    # Adresse des unteren Motorshield
    myMotor = motor.getStepper(200,2)                                                       # Motor mit 200 Schritten pro Umdrehung; angeschlossen an Port 2
    steps = 0                                                                               # Anzahl Schritte
    stepsPerRevolution = 0                                                                  # Anzahl Schritte pro Umdrehung
    rpm =30                                                                                 # 30 Umdrehungen pro Minute
    port = 0                                                                                # Port-Nummer
    distance = 0                                                                            # zu fahrende Distanz in m

    def __init__(self, stepsPerRevolution, port):                                           # Constructor der Klasse Motor
        self.stepsPerRevolution = stepsPerRevolution                                        # StepsPerRevolution-Wert wird uebergeben
        self.port = port                                                                    # port-Wert wird uebergeben
        self.myMotor = self.motor.getStepper(stepsPerRevolution, port)                      # myMotor-Werte werden uebergeben

    def drive(self, distance):                                                              # definiere Methode 'drive'
        self.distance = distance
        self.myMotor.setSpeed(self.rpm)
        revolutions = abs(distance/math.pi*0.1)                                             # Verhaeltnis Distanz zu Umfang der Raeder (mit Raddurchmesser = 100mm)
        steps = int(2*self.stepsPerRevolution*revolutions)
        if distance > 0:                                                                    # Fahre vorwaerts
            self.myMotor.step(steps, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.SINGLE)
        elif distance > 0:                                                                              # Fahre rueckwaerts
            self.myMotor.step(steps, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.SINGLE)
        self.steps = self.steps + steps
    def stop(self):                                                                         # definiere Methode 'stop'
        self.myMotor.setSpeed(1)                                                            # stoppe Motor

    def setSpeed(self, rpm):                                                                # definiere Methode 'setSpeed'
        self.rpm = rpm                                                                      # rpm mit neuem Wert ueberschreiben

    def getDistance(self):                                                                  # definiere Methode 'getDistance'
        return self.distance                                                                # Rueckgabewert distance

    def getSteps(self):                                                                           # definiere Methode 'getSteps'
        return self.steps
    def driveInSteps(self,steps):
        self.myMotor.setSpeed(self.rpm)
        if steps <0:
            self.myMotor.step(steps,Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.SINGLE)
        elif steps>0:
            self.myMotor.step(steps,Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.SINGLE)
