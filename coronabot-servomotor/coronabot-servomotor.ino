/*
 Coronabot
 controlling servomotor
 author: Tatjana Scheele
*/

#include "myServo.h"


void setup() 
{
  myServo::initialise();
}

void loop() 
{  
  myServo::runTest(); //Lässt einen Softwaretest durchlaufen, um die Programmierung zu testen

  for(int i=0; i<180; i++) //Lässt den Servomotor vom Winkel 0 bis zum Winkel 180° durchlaufen
  {
    myServo::moveAngle(i); //Bewegt den Servomotor zum Winkel i
    delay(100); //Verzögert den Durchlauf um 100ms
  }
}
