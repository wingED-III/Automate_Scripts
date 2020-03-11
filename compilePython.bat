@echo off
set /p pyFile= "Enter python file name that you want to compile: "
::pyinstaller.exe -F %pyFile% 
set pyFile=%pyFile:~0,-4%
echo %pyFile%
set x=.exe"
echo %x%
set pyFile=%pyFile%%x%
echo %pyFile%

echo %cd%
move %cd%\dist\%pyFile%  %cd%
pause