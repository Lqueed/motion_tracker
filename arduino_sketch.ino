#include <Servo.h>

int servoPin = 5; // def arduino servo pin
Servo Servo1;

void setup() {
  Serial.begin(9600);
  Servo1.attach(servoPin);
  Serial.setTimeout(100);
}

void loop() {
    int inByte = Serial.parseInt();
    Servo1.write(inByte);
    Serial.println(inByte); // debug - sends back received value
}
