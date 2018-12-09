/*
 Controlling a servo position using a potentiometer (variable resistor)
 by Michal Rinott <http://people.interaction-ivrea.it/m.rinott>

 modified on 8 Nov 2013
 by Scott Fitzgerald
 http://www.arduino.cc/en/Tutorial/Knob
*/

#include <Servo.h>

Servo myservo;  // create servo object to control a servo

void setup() {
  Serial.begin(9600);
  myservo.attach(10);  // attaches the servo on pin 9 to the servo objec 
  myservo.write(160); 
}

void loop() 
{
  if(analogRead(A0)>500)
  {
    delay(100);
    if(analogRead(A0)>500)
    {
      Serial.println("ON");
      myservo.write(20); 
      delay(10000);
      Serial.println("OFF");
      myservo.write(160);  
    }            
  }
  else
  {
    // Nothing
  }
   
                      
}
