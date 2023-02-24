import unittest
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from spotify_terminal_plugin.SpotifyController import SpotifyController
from base import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, SCOPE

class TestSpotifyController(unittest.TestCase):

    def setUp(self):
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI, scope=SCOPE))
        self.controller = SpotifyController(self.sp)

    def test_play_song(self):
        song_name = 'get lucky'
        self.controller.playSong(song_name)
    
    
        

if __name__ == '__main__':
    unittest.main()
