# Ubercat

Ubercat is a simple Python-based GUI application that allows you to manage multiple Netcat (nc) listeners. It is built using the Tkinter library and provides an easy-to-use interface for adding and removing listeners based on specified port numbers.

## Features

Add Netcat listeners on specified ports.
Manage multiple listeners simultaneously.
Remove listeners when no longer needed.
Simple and easy-to-use graphical interface.

## Requirements

1. Python 3.6 or higher
2. Tkinter library (usually comes pre-installed with Python)
3. Netcat (nc) command-line tool installed on your system

## Installation

Clone the repository or download the source code.

1. ```git clone https://github.com/cpncrunch/ubercat.git```
2. ```cd ubercat```
2. Run the application using Python.
4. ```python ubercat.py```

## Usage

1. Run the application.
2. Enter the desired port number in the "Port" field.
3. Click the "Add Listener" button to start a new listener on the specified port.
4. The new listener will appear in the list.
5. To remove a listener, select it in the list and click the "Remove Listener" button.
Notes
6. This program is designed to work with the Netcat (nc) command-line tool. Ensure that the "nc" command is accessible from your system's command prompt or terminal before using this program.
Removing a listener will terminate its associated process.

### This application is intended for educational and demonstration purposes only. Exercise caution when opening network listeners on your system.
