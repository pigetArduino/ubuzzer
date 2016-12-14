[Version française / French version](https://github.com/pigetArduino/ubuzzer/blob/master/readme.fr.md)

![Photo UBuzzer](https://github.com/pigetArduino/ubuzzer/raw/master/doc/ubuzzer_photo.jpg)   
UBuzzer is an device based on an Arduino nano to control a buzzer   
An application is available to use this buzzer on a **music software** and/or a **midi keyboard**.

**Warning: This application should be considered alpha, and could not works correctly.**      

Demo: 

![UBuzzer App](https://github.com/pigetArduino/ubuzzer/raw/master/doc/ubuzzer_app.png)   

# Installation
Drivers for the Arduino nano ch340 is provided in the installer.    
It will install it silently     

* Download arduino/python code : http://ubuzzer.madnerd.org
* Upload **ubuzzer.ino** sketch
* Download ubuzzer installer: http://ubuzzerdapp.madnerd.org  
* Start **ubuzzer_setup.exe**  

If ubuzzer **doesn't works**, check that 
* Windows is **updated**
* [Visual C++ redistribuable](https://www.microsoft.com/en-us/download/details.aspx?id=48145) !
* No software using midi is started

# Usage
## Midi Keyboard
Just plug your **midi keyboard** and play, ubuzzer will detect it **automatically**

## Midi Software
You can compose music that will be played by the buzzer.   
### LoopMidi
![LoopMidi Add Midi Port](https://github.com/pigetArduino/ubuzzer/raw/master/doc/loopMidi.png)     
Unfortunately rtmidi can't generate virtual midi port on Windows   
We are going to use loopMidi instead
* Download http://www.tobias-erichsen.de/software/loopmidi.html   
* Click on **+** to create a virtual midi port

### LMMS
Examples are available in **apps/ubuzzer/lmms**

![Ubuzzer on LMMS](https://github.com/pigetArduino/ubuzzer/raw/master/doc/ubuzzer_lmms.png)
* Download **LMMS** : https://lmms.io/download/#windows
* On **TripleOscillator** put the volume to 0
* Click on the gear next to **TripleOscillator**
* Click on Midi and choose your **virtual midi port** (**Loopmidi by default**)

## Arduino Serial Monitor
You can test this device on **Arduino Serial Monitor**    
Baudrate : 115200 / No Line Ending     

* UBuzzer --------> Check if this is the right device    
* X -------> Where X is the frequency   
* OFF -------> Stop sound    

# Components
* Arduino nano CH340G: 2€    
* 10 Buzzer : 1.80€  (1 Buzzer:0.18€)  
* Resistor pack 400pcs (3€) (1 resistor: 0.0071€) 
* 5 pcs stripboard (1.18€) (1 stripboard : 0.24€ )  
* Total : 7.98€ (2.43€)   

# Wiring
Don't forget to isolate the circuit from the arduino (see video)    
You can either use tape/hot glue/Blu-Tack (patafix)
## Buzzer only
![UBuzzer Wiring](https://github.com/pigetArduino/ubuzzer/raw/master/doc/ubuzzer_wiring.png)   
* Pin 9 : RESISTOR (100Ohm) --- Buzzer +   
* Pin 10 : Buzzer -    

## Buzzer/Led
Just add a led (**before the resistor**)
* Pin 9 : RESISTOR (100Ohm) --- Led + / Buzzer +   
* Pin 10 : Led - / Buzzer -    

# 3D Printing
This model is an **all purpose case** for arduino nano projects    
Models by Olivier Sarrailh : https://github.com/pigetArduino/ubuzzer/tree/master/3D    
**You won't be able to properly close the case as the buzzer takes too much place, but you should still be able to close it**

# Make your own arduino installer
[Developer documentation](https://github.com/pigetArduino/ubuzzer/blob/master/dev.readme.md)

# Licences
Software by Rémi Sarrailh (madnerd.org)   
License: MIT
