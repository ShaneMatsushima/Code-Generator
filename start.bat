@echo off
REM Change this to the directory where your virtual environment resides
set VENV_DIR=venv

REM Set your Python script to run (optional, if applicable)
set SCRIPT=gui.py

:MENU
echo.
echo ==========================
echo Virtual Environment Manager
echo ==========================
echo [1] Activate Environment
echo [2] Deactivate Environment
echo [3] Run Python Script
echo [4] Exit
echo ==========================
set /p choice=Select an option:

if "%choice%"=="1" goto activate
if "%choice%"=="2" goto deactivate
if "%choice%"=="3" goto runscript
if "%choice%"=="4" goto exit

:activate
REM Activate the virtual environment
if exist %VENV_DIR% (
    call %VENV_DIR%\Scripts\activate
    echo Virtual environment activated.
) else (
    echo Virtual environment not found! Make sure %VENV_DIR% exists.
)
goto menu

:deactivate
REM Deactivate the virtual environment
%VENV_DIR%\Scripts\deactivate
echo Virtual environment deactivated.
goto menu

:runscript
REM Activate environment and run script
if exist %VENV_DIR% (
    call %VENV_DIR%\Scripts\activate
    python %SCRIPT%
    deactivate
) else (
    echo Virtual environment not found! Make sure %VENV_DIR% exists.
)
goto menu

:exit
echo Exiting the Virtual Environment Manager.
exit