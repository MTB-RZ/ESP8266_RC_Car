import pygame
import websocket
import json

def send_command(command):
    try:
        ws = websocket.create_connection("ws://192.168.4.1:81/")
        ws.send(json.dumps(command))
        ws.close()
    except Exception as e:
        print("Connection Error:", e)

# Initialize Pygame for Xbox controller
pygame.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()

print("Connected to Xbox Controller")

while True:
    pygame.event.pump()

    # Left Stick X-Axis for Steering (Fixing sensitivity and smoothing)
    steering = joystick.get_axis(0)
    if abs(steering) < 0.05:  # Small deadzone to prevent unintended movement
        steering = 0.0

    # Right Trigger (RT) for Forward Throttle (Axis 5)
    throttle_forward = joystick.get_axis(5)
    throttle_forward = max(0, (throttle_forward + 1) / 2)  # Convert -1 to 1 -> 0 to 1

    # Left Trigger (LT) for Reverse Throttle (Axis 2)
    throttle_reverse = joystick.get_axis(4)
    throttle_reverse = max(0, (throttle_reverse + 1) / 2)  # Convert -1 to 1 -> 0 to 1

    # Final Throttle Value (Forward is positive, Reverse is negative)
    throttle = throttle_forward - throttle_reverse

    # Send data to ESP8266
    command = {
        "throttle": round(throttle, 2),   # Limiting decimal places for smoothness
        "steering": -round(steering, 2)
    }
    send_command(command)

    # Print updated values in the same line
    print(f"\rSent: Throttle={throttle:.2f} | Steering={steering:.2f}", end="", flush=True)
