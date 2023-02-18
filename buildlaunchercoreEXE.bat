
set mypath=%~dp0
pyinstaller --onefile "Examples/Crowd Control Main Menu.py" --add-data "Images;Images/" --add-data "Examples;Examples/" --icon Images\appicon.ico --add-data "Images\Launcher_BG.png;." 
move "%mypath%dist\Crowd Control Main Menu.exe" "%mypath%/"
RENAME "%mypath%\Crowd Control Main Menu.exe" "Crowd Control Main Menu.exe"
@RD /S /Q "%mypath%/build"
@RD /S /Q "%mypath%/dist"
DEL /S /Q "%mypath%/openGOALModLauncher.spec"
