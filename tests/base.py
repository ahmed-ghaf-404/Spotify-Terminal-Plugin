"""
spotify_terminal_plugin base module.

This is the principal module of the spotify_terminal_plugin project.
here you put your main classes and objects.

Be creative! do whatever you want!

If you want to replace this with a Flask application run:

    $ make init

and then choose `flask` as template.
"""
import os
from dotenv import load_dotenv

load_dotenv()

# example constant variable
NAME = "spotify_terminal_plugin"


CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')

CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')

REDIRECT_URI = os.getenv('SPOTIFY_CLIENT_URI')

SCOPE = os.getenv('SPOTIFY_CLIENT_SCOPE')