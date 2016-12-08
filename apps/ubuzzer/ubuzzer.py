#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Example application for Universal Led 
# Doc : http://github.com/pigetArduino/uled
# Author : Rémi Sarrailh (madnerd.org)
# Licence : MIT

# Arduino communication is completely managed by arduino module
# If connection is lost it will try to reconnect

from tkinter import *
import time
from threading import Thread
from functools import partial
import os
from lib import USB
import rtmidi2 as rtmidi
# Change device_name to detect another device
# Device name CH340 is arduino nano clone
# Device type is sent to the arduino and it should answer return_string
# Baudrate : Should be 9600 or 115200
device_name = "CH340"
device_type = "uBuzzer"
device_return_string = "OK"
device_baudrate = 115200

# Bootstrap color for ui
bg_grey = "#f3f3f3"

######################
# Universal Buzzer   #
######################

exec(open("buzzer.py").read())

#####################
# GUI Functions     #
#####################
# We use a callback when we quit the application so 
# we can correctly close the arduino connection
def quit_callback():
	try:
		usb.close()
	except:
		print("Arduino was not gracefully closed")
	root.destroy()

# This function generate buttons and commands with arguments
# We need to use partial to programatically create the commands


# GUI

# Create interface
root = Tk()
root.title(device_type) #Title
root.configure(background=bg_grey) #Background color
root.iconbitmap('ubuzzer.ico') #Icon

# Callback when application is closed
root.protocol("WM_DELETE_WINDOW", quit_callback)

#################
# Buttons Frame #
#################
frame_commands = Frame(root)
frame_commands.grid(row=0)

def midi_callback(message, time_stamp):
    global lastnote,last_time
    note = message[1]
    velocity = message[2]
  
    if velocity != 0:
        print("ON:  "+str(note) + " " + str(time_stamp))
        lastnote = note #Send tone
        last_time = time_stamp
        usb.write(str(midi_to_hz[note]))
    if velocity == 0:
        if lastnote == note:
            usb.write("OFF")
            print("OFF: "+str(note) + " " + str(time_stamp))
        else:
            print("DIS OFF: "+str(note) + " " + str(time_stamp) + "  " + str(last_time))

midi_in = rtmidi.MidiIn()
midi_in.callback = midi_callback
midi_in.open_port("*")

	
#################
# Status Frame  #
#################

frame_status = Frame(root)
frame_status.grid(row=2)
status = Label(frame_status,bg=bg_grey,fg="red",text="Searching...")
status.grid()

# Search arduino as soon as the gui is created
# We use a thread or the gui will be blocked by the function
# We passed the status label object, you can remove this if you don't want to
usb = USB.Device(device_name,device_type,device_return_string,device_baudrate,status)

# Start application (if something bad happens close arduino connection)
try:
	root.mainloop()
except:
	print("Application was forced to stop")
	try:
		#If something go wrong we try to close the serial connection correctly
		usb.close()
	except:
		print("Arduino Not gracefully closed")
