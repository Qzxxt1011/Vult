@echo off

echo Vult is now installing...
md c:\Users\%USERNAME%\Vult
move %~dp0\*.* c:\Users\%USERNAME%\Vult
ren c:\Users\%USERNAME%\Vult\main.py vult
set PATH=%PATH%;c:\Users\%USERNAME%\Vult\vult
cd c:\Users\%USERNAME%\Vult
pip install -r requirements.txt