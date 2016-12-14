Créer son application pour un Arduino
* Allez voir ce tutoriel:    
https://github.com/pigetArduino/utest/    
* Le code source est disponible sur **apps/ubuzzer**

## Installer Python 3 / pyserial
* Télécharger python 3 : https://www.python.org/downloads/
* Pendant l'installation, cocher **Add Python 3.5 to PATH**   
![Python Path](https://github.com/pigetArduino/utest/raw/master/doc/python_install_path.jpg)

* Ouvrez une invite de commande (Touche Windows / Tapez cmd) et installer pyserial
```
pip install pyserial
```

## Installer rtmidi2
Nous allons utiliser **rtmidi2** pour gérer le midi    
Malheuresement, vous aurez besoin de **Visual Studio** pour compiler rtmidi2 (L'installation est longue et prends inutilement 4go ou plus)
* Télécharger [rtmidi2](https://github.com/gesellkammer/rtmidi2/archive/master.zip)
* Télécharger [Visual Studio Community](http://www.visualstudio.com/vs/community)
* Installer Visual Studio Community et **Sélectionner**
    *  **Programming Languages**
        *  **Visual C++**
            * **Common Tools for Visual C++**
        * **Python Tools for Visual Studio**
* Sur la ligne de commande aller dans le dossier **rtmidi2**
* Tapez
```
pip install cython
python setup.py install
```

## Lancer l'application
* Ouvrez une invite de commande
* Aller dans le dossier du code source (apps/ubuzzer/)
* Tapez:
```
python ubuzzer.py
```
## Compiler l'Application
Vous aurez besoin de pyinstaller pour compiler l'application
```
pip install pyinstaller
```
Compiler le code python avec **compile.bat** ou la commande:
```
pyinstaller --noconsole --icon=ubuzzer.ico ubuzzer.py 
```

## Faire un installeur avec inno setup compiler
* Télécharger inno setup compiler: http://www.jrsoftware.org/isinfo.php
* Télécharger les pilotes Arduino pour nano ch340g : http://nano.madnerd.org
* Ouvrir **app/buzzer/buzzer_installer.iss**
* Changer les chemins des dossiers des pilotes et de l'application
```
;CHANGE PATHS before compiling!
#define APP "Y:\arduino\ubuzzer\apps\ubuzzer\dist\ubuzzer\"
#define DRIVERS "c:\nano"
```
Dans [RUN], Nous installons les pilotes silencieusement (comme expliquer sur le bouton help de setup.exe du pilotes)
```
[Run]
;Silent install for arduino nano ch340g drivers
Filename: {app}\nano\setup.exe; Parameters: "/s"; WorkingDir: {app}\nano;
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent
```
