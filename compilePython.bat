@echo off
set /p pyFile ="Enter python file name that you want to compile: "
pyinstaller.exe -F %pyFile%
pause