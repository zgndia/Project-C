@echo off
:: Get the current directory of the .bat file
set current_dir=%~dp0

pip install -r requirements.txt

:: Copy main.pyw to the shell:startup folder
copy "%current_dir%main.pyw" "%appdata%\Microsoft\Windows\Start Menu\Programs\Startup\"

del requirements.txt
del setup.bat