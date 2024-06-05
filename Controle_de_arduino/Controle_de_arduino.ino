#include <SoftwareSerial.h> //Biblioteca para realizar a leitura do serial interno
#include <Servo.h>

const int greenPin = 2;
const int redPin = 4;
const int servoPin = 5; // Pino em que o Servo motor será conectado

Servo myServo; // Nome para o Servo motor

void setup() {
  pinMode(greenPin, OUTPUT);
  pinMode(redPin, OUTPUT);

  myServo.attach(servoPin); // Define que o Servo motor está conectado no servoPin

  Serial.begin(9600); // Deve ser o mesmo valor do código em Python
}

void loop() {
  if (Serial.available() > 0) {
    // Exibe o valor recebido no serial do Arduino
    String command = Serial.readString();
    Serial.print("Received command: ");
    Serial.println(command);

    if (command == "ON") {
      // Ativa o LED verde e o Servo motor caso o comando do serial seja ON
      digitalWrite(greenPin, HIGH);
      digitalWrite(redPin, LOW);
      myServo.write(180); // Gira o servo em 180 graus
      delay(5000);
      } else if (command == "OFF") {
        // Ativa o LED vermelho e retorna o Servo motor para o estado original 
      digitalWrite(greenPin, LOW);
      digitalWrite(redPin, HIGH);
      myServo.write(0); // Gira o servo para 0 graus
      } else {
      // Desliga os dois LEDs caso seja recebido um comando desconhecido  
      digitalWrite(greenPin, LOW);
      digitalWrite(redPin, LOW);
    }
  }
}
