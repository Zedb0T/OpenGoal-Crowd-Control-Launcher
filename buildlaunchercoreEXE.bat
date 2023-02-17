
set mypath=%~dp0
pyinstaller --onefile "Examples/Crowd Control Main Menu.py" --icon Images\appicon.ico 
move "%mypath%dist\Crowd Control Main Menu.exe" "%mypath%/"
RENAME "%mypath%\Crowd Control Main Menu.exe" "Crowd Control Main Menu.exe"
@RD /S /Q "%mypath%/build"
@RD /S /Q "%mypath%/dist"
DEL /S /Q "%mypath%/openGOALModLauncher.spec"
