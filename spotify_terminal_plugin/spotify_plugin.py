from typing import Callable
from spotify_controller import SpotifyController

from base import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, SCOPE
from spotipy.oauth2 import SpotifyOAuth

import spotipy

from dataclasses import dataclass


@dataclass
class SpotifyPlugin:
    controller: SpotifyController
    active_command: Callable
    def __init__(self) -> None:
        self.controller = SpotifyController(spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI, scope=SCOPE)))
        self.commands = {
            "play": self.controller.playSong,
            "pause": self.controller.pause

        }

    def setActiveCommand(self, activeCommand, parts=[]):
        self.active_command = self.commands[activeCommand]
        self.active_args = parts

    def execute(self):
        try:
            return self.exectueActiveCommand()
        except Exception as e:
            return e

    def parseCommand(self, command:str)->None:
        parts = command.split(' ')
        try:
            self.setActiveCommand(parts.pop(0), parts)
            self.execute()
        except KeyError:
            return f"Invalid command: {command}\nValid commands: {self.commands.keys}"
        except Exception as E:
            return str(E)
        return "Command parsed"
    
    def exectueActiveCommand(self):
        return self.active_command(*self.active_args)




if __name__=="__main__":
    a = SpotifyPlugin()
    print(a.parseCommand("play a lonely night"))
    print(a.execute())
    # a.parseCommand("pause")