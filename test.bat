set mypath=%~dp0
set goalROOT=%mypath%/opengoal-crowd-control/


mkdir "%mypath%/Release/openGOAL/data/"
move "%goalROOT%data" "%mypath%/Release/openGOAL/"

start wmplayer.exe /play /close "%mypath%\Unpackaged Resources\ok.mp3"