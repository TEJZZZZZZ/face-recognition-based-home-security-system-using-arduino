 #define LED_PIN 13  // Change this to the pin number where your LED is connected

void setup() {
  pinMode(13, OUTPUT);  // Initialize the LED pin as an output
  Serial.begin(9600);  // Start serial communication at 9600 baud rate
}

void loop() {
  if (Serial.available()) {  // If data is available to read
    char c = Serial.read();  // Read the incoming data
    if (c == '1') {  // If '1' is received
      blinkLED();  // Call the blinkLED function
    }
  }
}

void blinkLED() {
  for (int i = 0; i < 5; i++) {  // Blink for 5 times
    digitalWrite(LED_PIN, HIGH);  // Turn the LED on
    delay(1000);  // Wait for 1000ms
    digitalWrite(LED_PIN, LOW);  // Turn the LED off
    delay(1000);  // Wait for 1000ms
  }
}

