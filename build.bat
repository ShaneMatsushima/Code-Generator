@echo off
REM Generating executable for application
pyinstaller --onefile --windowed --icon=plant.ico gui.py
echo Executable generated for application