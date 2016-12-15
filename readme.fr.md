[English](https://github.com/pigetArduino/ubuzzer/)

![Photo UBuzzer](https://github.com/pigetArduino/ubuzzer/raw/master/doc/ubuzzer_photo.jpg)   
UBuzzer est un périphérique à base d'Arduino nano pour contrôler un buzzer   
Une application est disponible pour utiliser le buzzer dans un **logiciel de musique** ou/avec un **clavier midi**.

**Attention: L'application est en alpha, il se peut qu'elle ne marche pas correctement!**      

Démo: 

![UBuzzer App](https://github.com/pigetArduino/ubuzzer/raw/master/doc/ubuzzer_app.png)   

# Installation
Les pilotes pour l'Arduino Nano ch340 sont fourni avec l'installeur.    
Ceci seront installé silencieusement.

* Télécharger le code pour l'arduino : http://ubuzzer.madnerd.org
* Téléverser le croquis **ubuzzer.ino**
* Télécharger l'installeur de ubuzzer: http://ubuzzerdapp.madnerd.org  
* Démarrer **ubuzzer_setup.exe**  

Si ubuzzer **ne marche pas**, vérifier 
* Si Windows est **à jour**
* [Redistribuable Visual C++](https://www.microsoft.com/fr-fr/download/details.aspx?id=48145) !
* Qu'aucun logiciel utilisant le midi n'est démarré.

# Utilisation
## Clavier Midi
Connectez votre **clavier midi** et jouer, ubuzzer va détecté celui-ci **automatiquement**

## Logiciel Midi
Vous pouvez aussi composer des musiques qui sera jouer par un buzzer.    
### LoopMidi
![LoopMidi Ajouter un port Midi](https://github.com/pigetArduino/ubuzzer/raw/master/doc/loopMidi.png)     
Malheuresement rtmidi ne peut pas créer un port midi virtual sous Windows.
Nous avons besoin de loopMidi pour cela.    
* Télécharger http://www.tobias-erichsen.de/software/loopmidi.html   
* Cliquer sur **+** pour créer un port midi virtuel

### LMMS
Des exemples sont disponibles dans **apps/ubuzzer/lmms**

![Ubuzzer dans LMMS](https://github.com/pigetArduino/ubuzzer/raw/master/doc/ubuzzer_lmms.png)
* Télécharger **LMMS** : https://lmms.io/download/#windows
* Sur **TripleOscillator** mettez le volume à 0
* Cliquer sur l'engrenage à coté de **TripleOscillator**
* Clicquer sur Midi et choissisez votre **port midi virtuel** (**Par défaut : Loopmidi**)

## Moniteur Série de l'Arduino
Vous pouvez tester ce périphérique dans **Le moniteur série de l'Arduino**    
Baudrate : 115200 / No Line Ending     

* UBuzzer --------> Vérifier si le périphérique fonctionne 
* X -------> Où X est la fréquence
* OFF -------> Arrête le son    

# Composants
* Arduino nano CH340G: 2€    
* 10 Buzzer : 1.80€  (1 Buzzer:0.18€)  
* Resistor pack 400pcs (3€) (1 résistance: 0.0071€) 
* 5 pcs stripboard (1.18€) (1 stripboard : 0.24€ )  
* Total : 7.98€ (2.43€)   

# Branchement
N'oubliez pas d'isoler le circuit de l'arduino (voir vidéo de démonstration)    
Vous pouvez utiliser du scotch/colle chaude/patafix     
## Buzzer seul
![Branchement UBuzzer](https://github.com/pigetArduino/ubuzzer/raw/master/doc/ubuzzer_wiring.png)   
* Broche 10 : RESISTANCE (100Ohm) --- Buzzer +   
* Broche 9 : Buzzer -    

## Buzzer/LED
Ajouter une LED (**avant la résistance**)
* Broche 10 : RESISTANCE (100Ohm) --- Led + / Buzzer +   
* Broche 9 : Led - / Buzzer -    

# Impression 3D
Ce modèle est un boitier pour les projets à base d'Arduino nano    
Modèle fait par Olivier Sarrailh : https://github.com/pigetArduino/ubuzzer/tree/master/3D    
**Vous n'arrivez pas à fermer correctement le boitier car le buzzer prends lègerement trop de place, pour autant le boitier reste fermable**

# Faire un installeur pour une application utilisant un Arduino
[Documentation du développeur](https://github.com/pigetArduino/ubuzzer/blob/master/dev.readme.fr.md)

# Licenses
Logiciel par Rémi Sarrailh (madnerd.org)   
License: MIT
