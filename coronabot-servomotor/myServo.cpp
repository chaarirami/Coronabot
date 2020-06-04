/*
 project: Coronabot
 file: Servo.cpp
 function: controlling servomotor
 author: Tatjana Scheele
**/
#include "myServo.h"

namespace myServo {
  int currentAngle = 0;
  Servo libServo;  
  
  void initialise(){
    libServo.attach(3);  
    Serial.begin(9600);
    while(!Serial){} //Für Arduino Micro
  }

  /*Servomotor bewegt sich zu dem angegebenen Winkel*/
  void moveAngle(int angle)
  {
      libServo.write(angle);
      currentAngle = angle;
  }
  
  /*Gibt aktuellen Winkel zurück*/
  int getAngle()
  {
    return currentAngle;  
  }

  void runTest(){
    Test::run(); 
  }
  
  test(ok){
    int angle = 20;
    moveAngle(angle);
    assertEqual(angle, getAngle());
  }
};
