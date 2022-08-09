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

    list_neuro = []
    list_dancefloor = []

    for genre in reddit.post_genres:
        if genre.name == 'neuro':
            [list_neuro.append(link) for link in genre.spotify_links]
        elif genre.name == 'dancefloor':
            [list_dancefloor.append(link) for link in genre.spotify_links]

    spotify = Spotify(playlist_id_to_add_to=os.getenv('SPOTIFY_PLAYLIST'))
    spotify_neuro = Spotify(playlist_id_to_add_to=os.getenv('SPOTIFY_PLAYLIST_NEURO'))
    spotify_dancefloor = Spotify(playlist_id_to_add_to=os.getenv('SPOTIFY_PLAYLIST_DANCEFLOOR'))

    list_both = spotify.get_list_of_songs_correct_format(list_neuro+list_dancefloor)
    list_neuro = spotify_neuro.get_list_of_songs_correct_format(list_neuro)
    list_dancefloor = spotify_dancefloor.get_list_of_songs_correct_format(list_dancefloor)

    spotify.add_to_playlist(list_both)
    spotify_neuro.add_to_playlist(list_neuro)
    spotify_dancefloor.add_to_playlist(list_dancefloor)
