[Version française / French version](https://github.com/pigetArduino/ubuzzer/blob/master/readme.fr.md)

![Photo UBuzzer](https://github.com/pigetArduino/ubuzzer/raw/master/doc/ubuzzer_photo.jpg)   
UBuzzer is an usb device maded from an Arduino nano (clone) to control a buzzer   
An application is available to use this buzzer on a music software and a USB midi keyboard.
Demo: 

![UBuzzer App](https://github.com/pigetArduino/ubuzzer/raw/master/doc/ubuzzer_app.png)   

# Usage
* Install arduino nano (clone ch340g) : http://nano.madnerd.org
* Download loopMidi : http://www.tobias-erichsen.de/software/loopmidi.html
* Download arduino/python code : http://ubuzzer.madnerd.org
* Upload **ubuzzer.ino** sketch
* Download ubuzzer app : http://ubuzzerdapp.madnerd.org    

How to install drivers ?: https://www.youtube.com/watch?v=m3CsftsfiQU

# Availables commands
You can test this device on **Arduino Serial Monitor**    
Baudrate : 115200 / No Line Ending     

* UBuzzer --------> Check if this is the right device    
* X -------> Where X is the frequency   
* OFF -------> Stop sound    

# Components
* Arduino nano CH340G: 2€    
* 1 Buzzer : ??€    
* Resistor pack 400pcs (3€) (1 resistance: 0.0071€)   
* Total : ??€   

# Wiring
![UBuzzer Wiring](https://github.com/pigetArduino/ubuzzer/raw/master/doc/ubuzzer_wiring.png)   
Pin 9 : RESISTOR (100Ohm) --- Buzzer +   
Pin 10 : Buzzer -    

# 3D Printing

# Create your own application
* Check these tutorials:    
https://github.com/pigetArduino/utest/    
https://github.com/pigetArduino/uled/
* Source code is availble in **apps/ubuzzer**

## Install rtmidi2
We are going to use rtmidi2 to manage midi   
* Download [rtmidi2](https://github.com/gesellkammer/rtmidi2/archive/master.zip)
* In the command line go to rtmidi2 folder
* Type
```
pip install cython
python setup.py install
```

#LoopMidi
![LoopMidi Add Midi Port](https://github.com/pigetArduino/ubuzzer/raw/master/doc/loopMidi.png)     
Unfortunately rtmidi can't generate virtual midi port on Windows
We are going to use loopMidi instead
* Download http://www.tobias-erichsen.de/software/loopmidi.html
* Click on **+** to create a virtual midi port

# Licences
Software by Rémi Sarrailh (madnerd.org)   
License: MIT

LoopMidi
Tobias Erichsen