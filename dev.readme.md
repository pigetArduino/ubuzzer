
# Create your own application
* Check this tutorial:    
https://github.com/pigetArduino/utest/    
* Source code is available in **apps/ubuzzer**

## Install Python 3 / pyserial
* Download python 3 : https://www.python.org/downloads/
* During the installation, tick **Add Python 3.5 to PATH**   
![Python Path](https://github.com/pigetArduino/utest/raw/master/doc/python_install_path.jpg)

* Open a command prompt (Windows Key + cmd) and install pyserial
```
pip install pyserial
```

## Install rtmidi2
We are going to use **rtmidi2** to manage midi    
Unfortunatly you will need **Visual Studio** to compile rtmidi2 (which takes forever to install and uses at least 4go)
* Download [rtmidi2](https://github.com/gesellkammer/rtmidi2/archive/master.zip)
* Download [Visual Studio Community](http://www.visualstudio.com/vs/community)
* Install Visual Studio Community and **Select**
    *  **Programming Languages**
        *  **Visual C++**
            * **Common Tools for Visual C++**
        * **Python Tools for Visual Studio**
* In the command line go to **rtmidi2** folder
* Type
```
pip install cython
python setup.py install
```

## Start the application
* Open a command prompt (Windows key + cmd)
* Go to the source code (apps/ubuzzer/)
* Type:
```
python ubuzzer.py

## Compile Application
You will need pyinstaller to compile your application
```
pip install pyinstaller
```
Compile python software using **compile.bat** or
```
pyinstaller --noconsole --icon=ubuzzer.ico ubuzzer.py 
```

## Make an installer with inno setup compiler
* Download inno setup compiler: http://www.jrsoftware.org/isinfo.php
* Download Arduino Drivers for nano ch340g : http://nano.madnerd.org
* Open app/buzzer/buzzer_installer.iss
* Change path
```
;CHANGE PATHS before compiling!
#define APP "Y:\arduino\ubuzzer\apps\ubuzzer\dist\ubuzzer\"
#define DRIVERS "c:\nano"
```
in [RUN], we install the drivers silently (as explains in setup.exe help button)
```
[Run]
;Silent install for arduino nano ch340g drivers
Filename: {app}\nano\setup.exe; Parameters: "/s"; WorkingDir: {app}\nano;
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent
```
