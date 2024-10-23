const int redPin = 8;    // Pin for Red LED
const int yellowPin = 9; // Pin for Yellow LED
const int greenPin = 10; // Pin for Green LED

void setup() {
  pinMode(redPin, OUTPUT); 
  pinMode(yellowPin, OUTPUT); 
  pinMode(greenPin, OUTPUT); 
}

void loop() {
  digitalWrite(greenPin, HIGH); // Turn on Green light
  delay(10000); // Wait for 10 seconds
  digitalWrite(greenPin, LOW); // Turn off Green light

  digitalWrite(yellowPin, HIGH); // Turn on Yellow light
  delay(3000); // Wait for 3 seconds
  digitalWrite(yellowPin, LOW); // Turn off Yellow light

  digitalWrite(redPin, HIGH); // Turn on Red light
  delay(10000); // Wait for 10 seconds
  digitalWrite(redPin, LOW); // Turn off Red light
}