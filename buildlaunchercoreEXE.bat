set mypath=%~dp0
set goalROOT=mypath/opengoal-crowd-control


pyinstaller --onefile --noconsole "Examples/Crowd Control Main Menu.py"  --icon Images\appicon.ico --add-data "Images;Images/" --add-data "Images\Launcher_BG.png;."
mkdir "%mypath%\Release\bin\" 
move "%mypath%dist\Crowd Control Main Menu.exe" "%mypath%\Release\bin"
RENAME "%mypath%\Crowd Control Main Menu.exe" "Crowd Control Main Menu.exe"
@RD /S /Q "%mypath%/build"
@RD /S /Q "%mypath%/dist"
DEL /S /Q "%mypath%/Crowd Control Main Menu.spec"


pyinstaller --onefile --noconsole "Examples/Command Cooldowns Menu.py"  --icon Images\appicon.ico --add-data "Images;Images/" --add-data "Images\Launcher_BG.png;." 
move "%mypath%dist\Command Cooldowns Menu.exe" "%mypath%\Release\bin"
RENAME "%mypath%\Command Cooldowns Menu.exe" "Command Cooldowns Menu.exe"
@RD /S /Q "%mypath%/build"
@RD /S /Q "%mypath%/dist"
DEL /S /Q "%mypath%/Command Cooldowns Menu.spec"

pyinstaller --onefile --noconsole "Examples/Command Durations Menu.py"  --icon Images\appicon.ico --add-data "Images;Images/" --add-data "Images\Launcher_BG.png;." 
move "%mypath%dist\Command Durations Menu.exe" "%mypath%\Release\bin"
RENAME "%mypath%\Command Durations Menu.exe" "Command Durations Menu.exe"
@RD /S /Q "%mypath%/build"
@RD /S /Q "%mypath%/dist"
DEL /S /Q "%mypath%/Command Durations Menu.spec"

pyinstaller --onefile --noconsole "Examples/Enabled Commands Menu.py"  --icon Images\appicon.ico --add-data "Images;Images/" --add-data "Images\Launcher_BG.png;." 
move "%mypath%dist\Enabled Commands Menu.exe" "%mypath%\Release\bin"
RENAME "%mypath%\Enabled Commands Menu.exe" "Enabled Commands Menu.exe"
@RD /S /Q "%mypath%/build"
@RD /S /Q "%mypath%/dist"
DEL /S /Q "%mypath%/Enabled Commands Menu.spec"

pyinstaller --onefile --noconsole "Examples/Settings Main Menu.py"  --icon Images\appicon.ico --add-data "Images;Images/" --add-data "Images\Launcher_BG.png;." 
mkdir "%mypath%\Release\"
move "%mypath%dist\Settings Main Menu.exe" "%mypath%\Release\"
RENAME "%mypath%\Settings Main Menu.exe" "Settings Main Menu.exe"
@RD /S /Q "%mypath%/build"
@RD /S /Q "%mypath%/dist"
DEL /S /Q "%mypath%/Settings Main Menu.spec"

pyinstaller --onefile --noconsole "Examples/Twitch Settings Menu.py"  --icon Images\appicon.ico --add-data "Images;Images/" --add-data "Images\Launcher_BG.png;." 
move "%mypath%dist\Twitch Settings Menu.exe" "%mypath%\Release\bin"
RENAME "%mypath%\Twitch Settings Menu.exe" "Twitch Settings Menu.exe"
@RD /S /Q "%mypath%/build"
@RD /S /Q "%mypath%/dist"
DEL /S /Q "%mypath%/Twitch Settings Menu.spec"


start wmplayer.exe /play /close "%mypath%\Unpackaged Resources\ok.mp3"