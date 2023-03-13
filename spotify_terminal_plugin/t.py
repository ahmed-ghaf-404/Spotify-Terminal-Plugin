from spotify_terminal_plugin.spotify_plugin import SpotifyPlugin


s = SpotifyPlugin()
s.parseCommand("play a lonely night")
s.execute()