import rtmidi2 as rtmidi
from lib import USB
print(rtmidi.get_in_ports())

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

print(midi_to_hz)

def callback(message, time_stamp):
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
midi_in.callback = callback
midi_in.open_port(0)

device_name = "CH340"
device_type = "UBuzzer"
device_return_string = "OK"
device_baudrate = 115200

usb = USB.Device(device_name,device_type,device_return_string,device_baudrate)

while True:
    notes=2