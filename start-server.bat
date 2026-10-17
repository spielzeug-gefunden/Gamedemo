@echo off
cd /d "%~dp0"
py -3 start-server.py 2>nul
if errorlevel 1 python start-server.py
