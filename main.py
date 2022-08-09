from src.reddit import Reddit
from src.spotify import Spotify

if __name__ == '__main__':
    reddit = Reddit()
    # reddit.get_post(post_author='TELMxWILSON', title_contains='new tunes', subreddit='DnB')
    reddit.get_post(
        post_url='https://www.reddit.com/r/DnB/comments/wj64wp/this_weeks_new_tunes_technimatic_alix_perez_as/')
    reddit.set_genre_data()

    spotify_list = []

    for genre in reddit.post_genres:
        if genre.name in ['dancefloor', 'neuro']:
            [spotify_list.append(link) for link in genre.spotify_links]

    spotify = Spotify(playlist_id_to_add_to='2ers3ra7gipMNBzaiEULH9')
    song_list = spotify.get_list_of_songs_correct_format(spotify_list)
    spotify.add_to_playlist(song_list)
