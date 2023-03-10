from dataclasses import dataclass

import spotipy

# from base import CLIENT_ID, CLIENT_SECRET, CLIENT_URI, CLIENT_SCOPE

@dataclass
class SpotifyController():
    sp: spotipy.Spotify
    
    def __init__(self, sp:spotipy.Spotify) -> None:
        self.sp = sp
        # spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=CLIENT_URI, scope=CLIENT_SCOPE))
        self.active_device_id = self.sp.devices()['devices'][0]['id']
        

    def playSong(self, *args):
        songName = ' '.join(args)

        track_uri = self.searchTrack(songName)

        self.sp.transfer_playback(device_id=self.active_device_id, force_play=True)
        
        # Play the track
        self.sp.start_playback(uris=[track_uri])
        return 
    
    def pause(self):
        self.sp.pause_playback(self.active_device_id)
    
    
    def searchTrack(self, trackName:str) -> str:
        # Search for a track and get its URI
        search_results = self.sp.search(q=trackName, type="track", limit=1)
        return search_results["tracks"]["items"][0]["uri"]
