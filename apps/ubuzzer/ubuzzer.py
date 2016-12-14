#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Universal Buzzer to midi 
# Doc : http://github.com/pigetArduino/ubuzzer
# Author : Rémi Sarrailh (madnerd.org)
# Licence : MIT

# Arduino communication is completely managed by arduino module
# If connection is lost it will try to reconnect

import rtmidi2
from tkinter import *
import time
from threading import Thread
from functools import partial
import os
from lib import USB

# Change device_name to detect another device
# Device name CH340 is arduino nano clone
# Device type is sent to the arduino and it should answer return_string
# Baudrate : Should be 9600 or 115200
device_name = "CH340"
device_type = "UBuzzer"
device_return_string = "OK"
device_baudrate = 115200

# Bootstrap color for ui
bg_grey = "#f3f3f3"

######################
# Universal Buzzer   #
######################

global lastnote,last_time
lastnote = 0
last_time = 0

midi_to_hz = {
11:31,
12:33,
13:35,
14:37,
15:39,
16:41,
17:44,
18:46,
19:49,
20:52,
21:55,
22:58,
23:62,
24:65,
25:69,
26:73,
27:78,
28:82,
29:87,
30:93,
31:98,
32:104,
33:110,
34:117,
35:123,
36:131,
37:139,
38:147,
39:156,
40:165,
41:175,
42:185,
43:196,
44:208,
45:220,
46:233,
47:247,
48:262,
49:277,
50:294,
51:311,
52:330,
53:349,
54:370,
55:392,
56:415,
57:440,
58:466,
59:494,
60:523,
61:554,
62:587,
63:622,
64:659,
65:698,
66:740,
67:784,
68:831,
69:880,
70:932,
71:988,
72:1047,
73:1109,
74:1175,
75:1245,
76:1319,
77:1397,
78:1480,
79:1568,
80:1661,
81:1760,
82:1865,
83:1976,
84:2093,
85:2217,
86:2349,
87:2489,
88:2637,
89:2794,
90:2960,
91:3136,
92:3322,
93:3520,
94:3729,
95:3951,
96:4186,
97:4435,
98:4699,
98:4978
}

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
root.geometry("210x50")
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
        midi.config(text=str(note))
        lastnote = note #Send tone
        last_time = time_stamp
        usb.write(str(midi_to_hz[note]))
    if velocity == 0:
        if lastnote == note:
            usb.write("OFF")
            print("OFF: "+str(note) + " " + str(time_stamp))
        else:
            print("DIS OFF: "+str(note) + " " + str(time_stamp) + "  " + str(last_time))

def midi_out_callback(message,time_stamp):
    print(message)



def check_midi():
    midi_in = rtmidi2.MidiInMulti()
    curr_ports = []
    prev_ports = []
    first_loop = True

    while True:
        curr_ports = rtmidi2.get_in_ports()
        if(len(prev_ports) != len(curr_ports)):
            midi_in.close_ports()
            prev_ports = []
            for port in curr_ports:
                if port not in prev_ports and 'Midi Through' not in port and (len(prev_ports) != len(curr_ports)):
                    midi_in.open_ports(port)
                    midi_in.callback = midi_callback
                    if first_loop:
                        print('Opened MIDI port: ' + port)
                    else:
                        print('Reopening MIDI port: ' + port)
        prev_ports = curr_ports
        first_loop = False
        time.sleep(0.2)

MidiThread = Thread(target=check_midi)
MidiThread.daemon = True
MidiThread.start()

	
#################
# Status Frame  #
#################

frame_status = Frame(root)
frame_status.grid(row=2)
status = Label(frame_status,fg="red",text="Searching...")
status.grid()
midi = Label(frame_status,fg="blue",text="Midi")
midi.grid()

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
