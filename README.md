[Download latest](https://cdn.discordapp.com/attachments/759976382121377845/1019405780342030356/Launcher_with_autoupdater.exe)  

[![Github All Releases](https://img.shields.io/github/downloads/OpenGOAL-Unofficial-Mods/OpenGoal-ModLauncher-dev/latest/total.svg?&label=Updated%20Downloads)]()
 
# Jak and Daxter Twitch Control

A program that allows Twitch viewers to control a streamer's game of Jak and Daxter: The Precursor Legacy using commands sent in Twitch chat.

## Installation

1. Clone the repository to your local machine.
2. Install the required dependencies by running `npm install`.
3. Create a Twitch account and register a new application in the [Twitch Developer Console](https://dev.twitch.tv/console/apps).
4. Set up environment variables for the Twitch application client ID and client secret in a `.env` file. The variables should be named `TWITCH_CLIENT_ID` and `TWITCH_CLIENT_SECRET` respectively.
5. Run the program using `npm start`.

## Usage

Once the program is running, viewers can use commands in Twitch chat to control the game being played by the streamer. The available commands are as follows:

- `jump`: Makes Jak jump.
- `spin`: Makes Jak perform a spin attack.
- `pause`: Pauses the game.
- `resume`: Resumes the game.
- `left`: Moves Jak to the left.
- `right`: Moves Jak to the right.
- `up`: Makes Jak look up.
- `down`: Makes Jak look down.
- `cameraleft`: Moves the camera to the left.
- `cameraright`: Moves the camera to the right.
- `camerazoomin`: Zooms the camera in.
- `camerazoomout`: Zooms the camera out.

## Contributing

Contributions are welcome! To contribute, please create a new branch with your changes and submit a pull request for review.

## License

This program is licensed under the [MIT License](https://opensource.org/licenses/MIT).
