@echo off
set /p pyFile= "Enter python file name that you want to compile: "
pyinstaller.exe -F %pyFile% 
set pyFile=%pyFile:~0,-4%

REM echo %pyFile%

set x=.exe"

REM echo %x%
set pyFile=%pyFile%%x%

REM echo %pyFile%
REM echo %cd%

move %cd%\dist\%pyFile%  %cd%
pause