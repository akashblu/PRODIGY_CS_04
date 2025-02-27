# PRODIGY_CS_04

This script is a simple keylogger that records keystrokes and logs them into a file called keylog.txt. It also displays a notification window to inform the user that keystrokes are being logged.

How the Code Works:
1. Imports Required Libraries
pynput.keyboard – Captures keyboard events.
tkinter – Creates a notification window.
threading.Thread – Runs the notification window separately to avoid blocking the main script.

3. Displays a Notification Window
The function show_notification() creates a pop-up using Tkinter.
It runs in a separate thread (Thread(target=show_notification).start()) so that the keylogger starts immediately without waiting for the user to close the notification.

4. Writes Keystrokes to a Log File
The write_to_file(key) function appends keystrokes to keylog.txt.

5. Handles Key Presses
The on_press(key) function:

Detects when a key is pressed.
Converts special keys (Space, Enter, Backspace, Tab, Shift, Ctrl, Alt) into readable format.
Regular keys (like letters and numbers) are logged as-is.
Removes unnecessary quotes (str(key).replace("'", "")).

5. Listens for Keystrokes
keyboard.Listener(on_press=on_press) continuously listens for key presses.
The script keeps running until manually stopped.
