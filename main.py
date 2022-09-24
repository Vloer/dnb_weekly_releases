from src.reddit import Reddit
from src.spotify import Spotify
from dotenv import load_dotenv
import os

load_dotenv()


def run_process(post_url: str, recursive: int = 1) -> None:
    """
    :param post_url:    Post url to gather songs from. Also serves as starting post for recursive search
    :param recursive:   Set to > 0 if links from previous weeks have to be scraped as well
                        (number indicates amount of weeks to go back)
    """
    reddit = Reddit()
    spotify = Spotify()
    recursive = 1   # TODO fix this

    for i in range(recursive):
        if i > 0:
            reddit.get_previous_post()  # TODO Doesn't work yet, max retry error
        else:
            reddit.get_post(post_url=post_url)
        reddit.set_genre_data()

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


if __name__ == '__main__':
    run_process('https://www.reddit.com/r/DnB/comments/xc9s2v/new_music_this_week_we_get_some_fresh_tunes_from/', 3)
