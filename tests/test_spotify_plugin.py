import pytest
from unittest.mock import MagicMock

from typing import Callable

from spotipy.oauth2 import SpotifyOAuth
import spotipy
from dataclasses import dataclass

import sys
sys.path.append('./spotify_terminal_plugin')
from spotify_plugin import SpotifyPlugin
from base import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, SCOPE
from spotify_controller import SpotifyController


class TestSpotifyPlugin:
    @pytest.fixture
    def spotify_plugin(self):
        spotify = MagicMock(spotipy.Spotify)
        return SpotifyPlugin()

    def test_parse_command(self, spotify_plugin):
        result = spotify_plugin.parseCommand("play starboy")
        assert "Command parsed" in str(result)
        assert spotify_plugin.active_command == spotify_plugin.controller.playSong
        assert spotify_plugin.active_args == ['starboy']

    def test_execute_valid_command(self, spotify_plugin):
        result = spotify_plugin.parseCommand("play starboy")  
        spotify_plugin.execute() 
        assert "Command parsed" in str(result)

    def test_execute_invalid_command(self, spotify_plugin):
        result = spotify_plugin.parseCommand("invalid")  
        spotify_plugin.execute() 
        assert 'Invalid command:' in str(result)

    def test_set_active_command(self, spotify_plugin):
        spotify_plugin.setActiveCommand('play', ['starboy'])
        assert spotify_plugin.active_command == spotify_plugin.controller.playSong
        assert spotify_plugin.active_args == ['starboy']
    def test_pause(self, spotify_plugin):
        spotify_plugin.setActiveCommand('pause')
        spotify_plugin.execute()
        assert spotify_plugin.active_command == spotify_plugin.controller.pause

