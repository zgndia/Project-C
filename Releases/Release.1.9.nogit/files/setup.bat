@echo off
set current_dir=%~dp0
pip install -r requirements.txt
copy "%current_dir%main.pyw" "%appdata%\Microsoft\Windows\Start Menu\Programs\Startup\"