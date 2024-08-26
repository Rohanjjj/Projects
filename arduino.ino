#include <LiquidCrystal_I2C.h>
// Define pins for ultrasonic sensors
const int trigPins[6] = {13,2,4,6,8,10};
const int echoPins[6] = {11,3,5,7,9,12};
int re=A0;
// Array to store distances
long distances[6];
LiquidCrystal_I2C lcd(0x27, 16, 2);// I2C address 0x27, 16 column and 2 rows
LiquidCrystal_I2C lcd1(0x26, 16, 2);

void setup()
{
  digitalWrite(0,HIGH);
  lcd.init(); 
  lcd.backlight();
  lcd1.init(); 
  lcd1.backlight();
  lcd1.setCursor(0,0);
  lcd1.print("Welcome");
  pinMode(re,OUTPUT);
  for (int i = 0; i < 6; i++) {
    pinMode(trigPins[i], OUTPUT);
    pinMode(echoPins[i], INPUT);
  }
  delay(10);
}

void loop() {
  for (int i = 0; i < 6; i++) {
    distances[i] = measureDistance(trigPins[i], echoPins[i]);
  }

  // Print distances to the serial monitor
  for (int i = 0; i < 6; i++) {
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("Sensor ");
    lcd.setCursor(7,0);
    lcd.print(i + 1);
    lcd.setCursor(0,1);
    lcd.print(": ");
    lcd.setCursor(2,1);
    lcd.print(distances[i]);
    lcd.setCursor(10,1);
    lcd.print(" cm");
    if(distances[i]<40){
      digitalWrite(re,HIGH);
    }
    else{
      digitalWrite(re,LOW);
    }
    if(distances[i]<40){
    lcd1.clear();
    lcd1.setCursor(0,0);
    lcd1.print("Sensor ");
    lcd1.setCursor(7,0);
    lcd1.print(i + 1);
    lcd1.setCursor(0,1);
    lcd1.print("Warning !!!!!!");
    delay(300);
    }
    else{
      lcd1.clear();
      lcd1.setCursor(0,0);
      lcd1.print("Safe drive");
    }
    delay(30);
  }
  delay(10); // Wait 1 second before next measurement
}

long measureDistance(int trigPin, int echoPin) {
  // Send a 10us pulse to trigger the sensor
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  // Read the echo pin, and calculate distance
  long duration = pulseIn(echoPin, HIGH);
  long distance = (duration / 2) / 29.1; // Convert time to distance in cm

  return distance;
}
