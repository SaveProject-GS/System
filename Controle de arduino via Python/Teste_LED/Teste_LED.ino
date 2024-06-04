
#include <SoftwareSerial.h>

const int greenPin = 2;
const int redPin = 4;

void setup() {
  pinMode(greenPin, OUTPUT);
  pinMode(redPin, OUTPUT);

  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    String command = Serial.readString();
    Serial.print("Received command: ");
    Serial.println(command);

    if (command == "ON") {
      digitalWrite(greenPin, HIGH);
      digitalWrite(redPin, LOW);
    } else if (command == "OFF") {
      digitalWrite(greenPin, LOW);
      digitalWrite(redPin, HIGH);
    } else {
      digitalWrite(greenPin, LOW);
      digitalWrite(redPin, LOW);
    }
  }
}
