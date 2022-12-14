import requests.auth
from dotenv import load_dotenv
import os
import json
from spotify_get_token import app
import base64

load_dotenv()


class Spotify:
    def __init__(self):
        self.authenticated: bool = False
        self.endpoint: str = 'https://api.spotify.com/v1'
        self.access_token: str = ''
        self.token_type: str = ''
        self.oauth_token: str = os.getenv('SPOTIFY_OAUTH_TOKEN')
        self.auth_headers: dict = {}
        self.all_song_links: list[str] = []
        self.playlist_songs_names: list[str] = []
        self.playlist_songs_uris: list[str] = []

        if not self.authenticated:
            self.get_token()

    def get_token(self) -> None:
        # if not self.oauth_token:
        #     app.run()
        url = "https://accounts.spotify.com/api/token"
        client_id = os.getenv('SPOTIFY_CLIENT_ID')
        client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')
        auth = requests.auth.HTTPBasicAuth(client_id, client_secret)
        data = {'grant_type': 'client_credentials'}

        res = requests.post(url, auth=auth, data=data)
        res.raise_for_status()
        self.access_token = res.json()['access_token']
        self.token_type = res.json()['token_type']
        self.authenticated = True
        self.auth_headers = {
            'Authorization': f'{self.token_type} {self.access_token}'
        }
    #
    # def get_token_client_credentials(self) -> None:
    #     url = "https://accounts.spotify.com/api/token"
    #     client_id = os.getenv('SPOTIFY_CLIENT_ID')
    #     client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')
    #     redirect_uri = 'http://localhost:8888/callback'
    #     scope = 'playlist-read-private playlist-modify-private'
    #     auth_code = requests.get(url, {
    #         'client_id': client_id,
    #         'response_type': 'code',
    #         'redirect_uri': redirect_uri,
    #         'scope': scope
    #     })

    def add_to_playlist(self, playlist_id: str, songs: str | list[str] = None) -> None:
        if isinstance(songs, str):
            songs = [songs]
        playlist = self._check_playlist_exists(playlist_id)
        if playlist:
            self.get_playlist_data(playlist)
            songs_to_add = self.get_songs_to_add(songs)
            if songs_to_add:
                try:
                    url = f'{self.endpoint}/playlists/{playlist_id}/tracks'
                    headers = self.auth_headers
                    headers['Content-Type'] = 'application/json'
                    headers['Authorization'] = f'Bearer {self.oauth_token}'
                    data = json.dumps({
                        'uris': songs_to_add
                    })

                    res = requests.post(url, headers=headers, data=data)
                    res.raise_for_status()
                except requests.exceptions.HTTPError:
                    raise ValueError(f'Your OAuth token is invalid or expired! Refresh it and place it in the .env file.')
            print(f"Added {len(songs_to_add)} new song(s) to playlist {playlist['name']!r}!")
        else:
            err = f"Playlist with id {playlist_id!r} does not exist!"
            raise ValueError(err)

    @staticmethod
    def convert_track_to_uri(track_id: str) -> str:
        if 'spotify.com' in track_id:
            track_id = track_id.split('/')[-1]
        if not track_id.startswith('spotify:track:'):
            return f'spotify:track:{track_id}'
        return track_id

    def _check_playlist_exists(self, playlist_id: str) -> bool | dict:
        url = f'{self.endpoint}/playlists/{playlist_id}'
        _res = requests.get(url, headers=self.auth_headers)
        res = _res.json()
        if 'error' in res.keys():
            print(f'Failed to get playlist!\n'
                  f"{res.get('message')}")
            return False
        _res.raise_for_status()
        return res

    def extract_uris_from_album_or_song(self, link: str) -> str | list[str]:
        song_list = []
        if '/track/' in link:
            return self.convert_track_to_uri(link)
        # if not self.authenticated:
        #     self.get_token()
        if '/album/' in link:
            album_id = link.split('/')[-1]
            url = f'{self.endpoint}/albums/{album_id}/tracks'
            headers = self.auth_headers
            headers['Content-Type'] = 'application/json'
            res = requests.get(url, headers=headers)
            res.raise_for_status()
            try:
                for song in res.json()['items']:
                    song_list.append(song['uri'])
            except KeyError:
                for song in res.json()['tracks']['items']:
                    song_list.append(song['uri'])
        return song_list

    def get_list_of_songs_correct_format(self, data: list[str]) -> list[str]:
        song_list = []
        for link in data:
            songs = self.extract_uris_from_album_or_song(link)
            if isinstance(songs, list):
                [song_list.append(s) for s in songs]
            else:
                song_list.append(songs)
        return song_list

    def get_playlist_data(self, playlist: dict, print_output: bool = False) -> None:
        playlist_songs_names = []
        playlist_songs_uris = []
        for track in playlist['tracks']['items']:
            song = track['track']
            name = song['name']
            artist = song['artists'][0]['name']
            uri = song['uri']
            playlist_songs_names.append(f'{artist}-{name}')
            playlist_songs_uris.append(f'{uri}')
            if print_output:
                print(f'Found \"{artist}-{name}\" in playlist')
        self.playlist_songs_uris = playlist_songs_uris
        self.playlist_songs_names = playlist_songs_names

    def check_song_already_in_playlist(self, song: str, is_uri: bool = True) -> bool:
        if is_uri:
            return song in self.playlist_songs_uris
        return song in self.playlist_songs_names

    def get_songs_to_add(self, songs: list[str]) -> list[str]:
        new_list = []
        for song in songs:
            if not self.check_song_already_in_playlist(song):
                new_list.append(song)
        return new_list
