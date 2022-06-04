import spotipy
from spotipy.oauth2 import SpotifyOAuth
from songs_list import SongsList
songlist = SongsList()

# ___ We are using spotipy python library for creating the spotify playlist___ 3
# ___spotify.oauth2 helps us to authenticate___ #

scope = "playlist-modify-public"
username = "your user name"
Client_ID = "your client id"
Client_Secret = "your client secret"
Redirect_URI = "your uri saved in the spotify developer API"

# ___scope basically details our permission___ #
# ___username to specify for whom playlist is created___ #
# ___Client id, secert, URI are part of the parameters in spotify API___ #

token = SpotifyOAuth(
    scope=scope,
    username=username,
    client_id=Client_ID,
    client_secret=Client_Secret,
    redirect_uri=Redirect_URI,
    cache_path="token.txt")

# ___spotifyobject will do all the task of creating playlist___ #
# ___token is a parameter to pass into the auth_manager for authentification___ #
# ___ cache_path is used to name the file created during the process where the access token is saved___ #

spotifyObject = spotipy.Spotify(auth_manager=token)

# ___Authenticated, next step is to create a playlist___ #
# ___To create a playlist then give a name and description to our playlist___ #
playlist_name = input("Enter a playlist name: ")
playlist_description = input("Enter a playlist description: ")

spotifyObject.user_playlist_create(
    user=username,
    name=playlist_name,
    description=playlist_description,
    public=True)

# ___Tap in the songs list from song_list.py, and using spotify searching method to get the URL___ #

songs = songlist.song_generator()
play_list = []
for each in songs:
    try:
        result = spotifyObject.search(q=each)
        play_list.append(result["tracks"]["items"][0]["uri"])

    except FileNotFoundError:
        pass

    else:
        continue

# ___Adding the URL list thus created to make a playlist___ #

prePlayList = spotifyObject.user_playlists(user=username)
playlist = prePlayList["items"][0]["id"]
spotifyObject.playlist_add_items(playlist_id=playlist, items=play_list)