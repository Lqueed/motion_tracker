#include <Servo.h>

int servoPin = 5;
Servo Servo1;

void setup() {
  Serial.begin(9600);
  Servo1.attach(servoPin);
  Serial.setTimeout(100);
}

void loop() {
  
//  if (Serial.available()) {

    int inByte = Serial.parseInt();
    Servo1.write(inByte);
    Serial.println(inByte); 
    
//    delay(1000);
//  }
}
