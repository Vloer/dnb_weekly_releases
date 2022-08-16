from src.reddit import Reddit
from src.spotify import Spotify
from dotenv import load_dotenv
import os

load_dotenv()

if __name__ == '__main__':
    reddit = Reddit()
    # reddit.get_post(post_author='TELMxWILSON', title_contains='new tunes', subreddit='DnB')
    reddit.get_post(
        post_url='https://www.reddit.com/r/DnB/comments/wj64wp/this_weeks_new_tunes_technimatic_alix_perez_as/')
    reddit.set_genre_data()

    spotify = Spotify()

    list_dance_neuro = []

    for genre in reddit.post_genres:
        list_genre = []
        if 'deep' in genre.name.lower():
            playlist_id = os.getenv('SPOTIFY_PLAYLIST_DEEP')
        elif 'general' in genre.name.lower():
            playlist_id = os.getenv('SPOTIFY_PLAYLIST_GENERAL')
        else:
            playlist_id = os.getenv(f'SPOTIFY_PLAYLIST_{genre.name.upper().replace(" ", "")}')
        [list_genre.append(link) for link in genre.spotify_links]
        list_songs = spotify.get_list_of_songs_correct_format(list_genre)
        spotify.add_to_playlist(playlist_id, list_songs)

        if any([g in genre.name.lower() for g in ['neuro', 'dancefloor']]):
            list_dance_neuro += list_songs

    spotify.add_to_playlist(os.getenv('SPOTIFY_PLAYLIST'), list_dance_neuro)
