/*
 project: Coronabot
 file: Servo.h
 function: controlling servomotor
 author: Tatjana Scheele
*/

#ifndef myServo_h
#define myServo_h

#include <Arduino.h>
#include <Servo.h>
#include <ArduinoUnit.h>

namespace myServo{
  void initialise();
  void moveAngle(int angle);
  int getAngle();
  void runTest();
};

#endif
