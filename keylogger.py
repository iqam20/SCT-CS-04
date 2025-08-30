from pynput import keyboard

# File to store key logs
LOG_FILE = "key_log.txt"

def on_press(key):
    try:
        # Record key press in file
        with open(LOG_FILE, "a") as f:
            f.write(f"Key Pressed: {key.char}\n")
        print(f"Key Pressed: {key.char}")   # also show in console
    except AttributeError:
        # Handle special keys (like space, enter, shift)
        with open(LOG_FILE, "a") as f:
            f.write(f"Special Key: {key}\n")
        print(f"Special Key: {key}")

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener when Esc is pressed
        print("Exiting logger...")
        return False

print("=== Keyboard Event Logger (Safe Version) ===")
print("Press keys... (Press ESC to exit)\n")

# Start listening to keyboard events
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
