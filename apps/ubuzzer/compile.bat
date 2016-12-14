pyinstaller --noconsole --icon=ubuzzer.ico ubuzzer.py 
rem pyinstaller --debug ubuzzer.py --log-level=DEBUG --hidden-import=cython --hidden-import=rtmidi2