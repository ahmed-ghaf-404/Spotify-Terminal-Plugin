import os
from dotenv import load_dotenv
from spotify_client import SpotifyClient
import base64 
import requests
import json 


def main():

    spotify_client = SpotifyClient(os.getenv("SPOTIFY_AUTH_TOKEN"))

    print(os.getenv("SPOTIFY_AUTH_TOKEN"))
    track = spotify_client.search_track()


    was_added_to_library = spotify_client.add_to_library(track)

    if was_added_to_library:
        print(f'Added {track["track"]}')
    return 



if __name__ == "__main__":
    main()
    # load_dotenv()
    # client_id = os.getenv("SPOTIFY_CLIENT_ID")
    # client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
    # print(client_id, client_secret)
    # token = get_token()
