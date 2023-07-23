![](https://user-images.githubusercontent.com/95478989/198955082-6e78ebb5-e1e4-49f9-8d32-6e5af3984dcd.gif)

# Keylogger
This is a simple keylogger program developed using Python and the Tkinter library for the graphical user interface. 
The keylogger records every keystroke made by a computer user. 
It is important to note that keyloggers can be used for malicious purposes, such as gaining unauthorized access to passwords and confidential information. 
This program is purely for educational purposes and should not be used for any illegal activities.

**->How it works**

The keylogger captures key events when a key is pressed, held, or released. 
The captured events are then stored in two different formats: a JSON file (log.json) and a text file (logs.txt). 
The JSON file stores the key events in a structured format, while the text file stores the raw key strokes.

**->Features**

Start the keylogger: Click the "START KEYLOGGER" button to start the keylogger. Once started, it will capture and record all key events.
Stop the keylogger: Click the "STOP KEYLOGGER" button to stop the keylogger. It will no longer capture any key events.
Keylogger status: The status label at the bottom of the window displays the current status of the keylogger (running or stopped).

**->Prerequisites**

To run this program, you need to have the following dependencies installed:
1. Python 3.x
2. tkinter (Python GUI library)
	(Intall this library package in command prompt by using "pip install tk")
3. pynput (Python library for keyboard monitoring)
	(Intall this library package in command prompt by using "pip install pynput")
4. PIL (Python Imaging Library)
	(Intall this library package in command prompt by using "pip install pillow")

**->How to Run**

1. Clone or download the project files from the repository.
2. Make sure you have the required dependencies installed.
3. Run the keylogger.py file using Python.
4. The graphical interface will open, and you can start and stop the keylogger as needed.

**->Warning**

Using keyloggers without proper authorization is illegal and unethical. The developer of this program strongly discourages any malicious or unauthorized use.
This program should only be used for educational purposes, cybersecurity research, or with explicit consent from the target individual(s).

Please use this program responsibly and respect the privacy and security of others.
