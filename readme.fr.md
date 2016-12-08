[English](https://github.com/pigetArduino/ubuzzer/)

![Photo UBuzzer](https://github.com/pigetArduino/ubuzzer/raw/master/doc/ubuzzer_photo.jpg)   
UBuzzer est un périphérique USB crée à partir d'un Arduino nano (clone) pour contrôler un buzzer   
Une application est disponible afin d'utiliser le buzzer, avec un logiciel de musique et un synthé.      
Démonstration : 

![UBuzzer App](https://github.com/pigetArduino/ubuzzer/raw/master/doc/ubuzzer_app.png)   

# Utilisation
* Installer les pîlotes de l'arduino nano (clone ch340g) : http://nano.madnerd.org
* Télécharger loopMidi : http://www.tobias-erichsen.de/software/loopmidi.html
* Télécharger le code arduino/python : http://ubuzzer.madnerd.org
* Téléverser le croquis **ubuzzer.ino**
* Télécharger l'application : http://ubuzzerdapp.madnerd.org    

Comment installer les pilotes ?: https://www.youtube.com/watch?v=m3CsftsfiQU



# Commandes disponibles
Vous pouvez tester ce périphérique dans le moniteur série du logiciel Arduino
Baudrate : 115200 / No Line Ending   

* UBuzzer --------> Vérifie si c'est le bon périphérique 
* X -------> Où X est la fréquence
* OFF -------> Stop le son


# Composants
* Arduino nano CH340G: 2€
* 1 Buzzer : ??€
* Resistor pack 400pcs (3€) (1 resistance: 0.0071€)
* Total : ??€

# Branchement
![UBuzzer Wiring](https://github.com/pigetArduino/ubuzzer/raw/master/doc/ubuzzer_wiring.png)   
Pin 9 : RESISTANCE (100Ohm) --- Buzzer +
Pin 10 : Buzzer -

# Impression 3D


# Créer sa propre application
* Aller voir ce tutoriel: https://github.com/pigetArduino/utest/blob/master/README.fr.MD
* Ainsi que celui-ci https://github.com/pigetArduino/uled/blob/master/README.fr.MD
* Le code source est disponible dans **apps/ubuzzer**

## Installer rtmidi2
Afin de gérer le midi nous utilisons rtmidi2   
* Télécharger ![rtmidi2](https://github.com/gesellkammer/rtmidi2/archive/master.zip)
* Aller dans le dossier en ligne de Commande
* Tapez
```
pip install cython
python setup.py install
```

#LoopMidi
![LoopMidi Add Midi Port](https://github.com/pigetArduino/ubuzzer/raw/master/doc/loopMidi.png) 
Malheuresement sous Windows rtmidi ne peut pas générer de port midi virtuel   
Nous allons utiliser loopMidi pour faire cela.
* Télécharger http://www.tobias-erichsen.de/software/loopmidi.html
* Cliquer sur + pour créer un port midi virtuel

# Licences
Logiciel par Rémi Sarrailh (madnerd.org)   
License: MIT

