# ESP8266_RC_Car
This project is a WiFi-controlled RC car using an ESP8266 and an L298N motor driver. The ESP8266 receives throttle and steering inputs via WebSockets and controls the DC motor and servo steering proportionally.

**Features**

✅ Proportional throttle control (PWM-based speed control).

✅ Proportional steering control (Servo-based angle adjustment).

✅ WebSocket communication for real-time control.

✅ Adjustable PWM frequency for stable motor operation.


**Hardware Used**

ESP8266 (NodeMCU or Wemos D1 Mini)

L298N Motor Driver

Coreless DC Motors

Servo Motor for Steering

12V or 7.4V Li-ion Battery


**Setup & Upload**

Flash the ESP8266 with the provided code using Arduino IDE.

Power the ESP8266 separately or through the L298N’s 5V output (with a capacitor for stability).

Connect the ESP8266 to the motor driver as per the pin configuration.

Use a WebSocket client or a custom controller (e.g., a mobile app or PC) to send throttle and steering data. (In the code provided, it is being controlled via Xbox Controller)


**Next Improvements**

Implement PID-based speed control for better accuracy.

Add IMU-based stabilization for smoother handling.

Develop a mobile app UI for easier control.


