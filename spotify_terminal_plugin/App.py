from SpotifyController import SpotifyController

from base import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, SCOPE
from spotipy.oauth2 import SpotifyOAuth

import spotipy
class App:
    def __init__(self) -> None:
        # ? idea: cache this
        self.controller = SpotifyController(spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI, scope=SCOPE)))
        self.commands = {
            "play": self.controller.playSong
        }

    def execute(self, command:str):
        try:
            self.parseCommand(command)
            self.exectueActiveCommand()
        except Exception as e:
            return e

    def parseCommand(self, command:str)->None:
        parts = command.split(' ')
        try:
            self.active_command = self.commands[parts.pop(0)]
            self.active_args = parts
        except KeyError:
            return f"Invalid command\nValid commands: {self.commands.keys}"
    
    def exectueActiveCommand(self):
        self.active_command(*self.active_args)

if __name__=="__main__":
    a = App()
    a.execute("play starboy")