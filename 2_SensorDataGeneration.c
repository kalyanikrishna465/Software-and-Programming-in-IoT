#define NUM_READINGS 5 // Number of readings for moving average

float readings[NUM_READINGS]; // Array to store readings
int index = 0; // Current index
float total = 0; // Total for average calculation
float average = 0; // Average value

void setup() {
  Serial.begin(9600);
  for (int i = 0; i < NUM_READINGS; i++) {
    readings[i] = 0; // Initialize readings
  }
}

void loop() {
  // Generate random temperature data
  float temperature = random(200, 301) / 10.0; // Scale to 20.0 - 30.0
  
  // Subtract the last reading
  total = total - readings[index];
  // Add the new reading
  readings[index] = temperature;
  total = total + readings[index];
  // Move to the next index
  index = (index + 1) % NUM_READINGS;
  // Calculate the average
  average = total / NUM_READINGS;

  // Print the sensor data and the average
  Serial.print("Current Temperature: ");
  Serial.print(temperature);
  Serial.print(" °C, Moving Average: ");
  Serial.print(average);
  Serial.println(" °C");

  delay(2000); // Wait for 2 seconds
}