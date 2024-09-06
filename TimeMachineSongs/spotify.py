from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from datetime import datetime

# Use the following command to install the dotenv library:
# pip install python-dotenv
class Spotify:
    def __init__(self, songs_info):
        self.__file_path = os.environ.get("MY_ENV")
        load_dotenv(dotenv_path = self.__file_path)

        self.__sp_client_id = os.getenv('SP_CLIENT_ID')
        self.__client_secret = os.getenv('SP_CLIENT_SECRET')
        self.__token_path = os.getenv('SP_TOKEN_PATH')

        self.__playlist_id = None
        self.__playlist_name = None
        self.__user_id = None
        self.__playlists= None
        self.__uri_list=[]

        self.__sp = None
        self.__songs_info = songs_info

        self.__connect_to_sp()

    def __connect_to_sp(self):
        try:
            self.__sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
                client_id=self.__sp_client_id,
                client_secret=self.__client_secret,
                redirect_uri='http://localhost:8888/callback',
                scope='playlist-modify-public',
                cache_path=self.__token_path
            ))
            user_info = self.__sp.current_user()

            if user_info is None:
                raise Exception("Failed to retrieve user information.")
            self.__user_id = user_info['id']
            self.__playlists = self.__sp.current_user_playlists()
            print(f"Connected to Spotify as user ID: {self.__user_id}")
        except spotipy.exceptions.SpotifyException as e:
            print(f"Spotify API error: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")


    def create_playlist(self, date):
        # Create a new playlist on spotify
        # Using the year, and week number based on the date input
        week_num = self.__get_week_num(date)
        year = date[0:4]
        playlist_name = f"Time Machine Year: {year} Week: {week_num}"

        if(self.__playlist_exist(playlist_name)):
            print(f"Playlist already exist for Year{year} Week{week_num}")
            return

        self.__playlist_name = playlist_name
        playlist_description = "A playlist created using Spotipy and python"
        playlist = self.__sp.user_playlist_create(user=self.__user_id, name=self.__playlist_name, public=True,
                                                  description=playlist_description)

        self.__playlist_id = playlist['id']
        self.__build_uri_list()
        self.__add_songs()

    def __get_week_num(self, date):
        date_obj = datetime.strptime(date, '%Y-%m-%d')

        # Get the week number of the year using %U (Sunday as the first day of the week)
        week_number_U = date_obj.strftime('%U')

        return week_number_U


    def __playlist_exist(self, name):
        playlist_exist = False
        for playlist in self.__playlists['items']:
            if playlist['name'] == name:
                playlist_exist = True

        return playlist_exist

    def __get_uri_tracks(self, song_name, artist_name):
        query = f"track:{song_name} artist:{artist_name}"
        results = self.__sp.search(q=query, limit=1, type='track')
        tracks = results['tracks']['items']
        if tracks:
            return tracks[0]['uri']
        return None

    def __build_uri_list(self):
        for song_name, artist_name in self.__songs_info:
            track_uri = self.__get_uri_tracks(song_name, artist_name)
            print(track_uri)
            if track_uri:
                self.__uri_list.append(track_uri)

    def __add_songs(self):
        self.__sp.user_playlist_add_tracks(user=self.__user_id, playlist_id=self.__playlist_id, tracks=self.__uri_list)
        print(f"Playlist '{self.__playlist_name}' created successfully with {len(self.__uri_list)} tracks!")
