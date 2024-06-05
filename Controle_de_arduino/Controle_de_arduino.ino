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
      // Ativa o LED vermelho e o Servo motor caso o comando do serial seja ON
      digitalWrite(redPin, HIGH);
      digitalWrite(greenPin, LOW);
      myServo.write(140); // Gira o servo nos graus desejados
      delay(2000);
      } else if (command == "OFF") {
        // Ativa o LED verde e retorna o Servo motor para o estado original 
      digitalWrite(redPin, LOW);
      digitalWrite(greenPin, HIGH);
      myServo.write(0); // Gira o servo para 0 graus
      } else {
      // Desliga os dois LEDs caso seja recebido um comando desconhecido  
      digitalWrite(greenPin, LOW);
      digitalWrite(redPin, LOW);
    }
  }
}
