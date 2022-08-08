import requests.auth
from typing import Optional
import os
import re
from dotenv import load_dotenv

load_dotenv()


class Reddit:
    def __init__(self):
        self.authenticated: bool = False
        self.endpoint: str = 'https://oauth.reddit.com'
        self.app_user_agent: str = f'windows:REPLACE_APP_ID:vREPLACE_VERSION (by /u/REPLACE_USERNAME)'
        self.access_token: Optional[str] = None
        self.token_type: Optional[str] = None
        self.post_list: Optional[list[str]] = []
        self.post_url: Optional[str] = None
        self.post_text: Optional[str] = None
        self.post_segments: Optional[list] = []
        self.post_genres: Optional[list[Genre]] = []

        if not self.authenticated:
            self.get_token()

    def get_token(self) -> None:
        api_secret = os.getenv('REDDIT_API_SECRET')
        reddit_app_id = os.getenv('REDDIT_APP_ID')
        auth = requests.auth.HTTPBasicAuth(reddit_app_id, api_secret)
        reddit_user = os.getenv('REDDIT_USERNAME')
        reddit_pass = os.getenv('REDDIT_PASSWORD')
        version = os.getenv('VERSION')
        user_agent = self.app_user_agent. \
            replace('REPLACE_APP', reddit_app_id). \
            replace('REPLACE_USERNAME', reddit_user). \
            replace('REPLACE_VERSION', version)
        self.app_user_agent = user_agent

        data = {
            'grant_type': 'password',
            'username': reddit_user,
            'password': reddit_pass
        }

        headers = {'User-Agent': self.app_user_agent}

        res = requests.post('https://www.reddit.com/api/v1/access_token', auth=auth, data=data, headers=headers)
        res.raise_for_status()
        self.access_token = res.json()['access_token']
        self.token_type = res.json()['token_type']
        self.authenticated = True

    def get_post(self, post_author: str = None, title_contains: str = None, subreddit: str = None, post_url: str = None,
                 post_search_limit: int = 500) -> str:
        headers = {
            'User-Agent': self.app_user_agent,
            'Authorization': f'{self.token_type} {self.access_token}'
        }
        post_data = None
        if not post_url:
            if not post_author or not title_contains or not subreddit:
                raise KeyError('Please supply either author, (part of) the post title and subreddit, or the post url.')
            else:
                res = requests.get(f'{self.endpoint}/r/{subreddit}/new', headers=headers,
                                   params={'limit': f'\'{post_search_limit}\''})
                res.raise_for_status()
                for post in res.json()['data']['children']:
                    title = post['data']['title']
                    author = post['data']['author']
                    if author in post_author and title_contains in title:
                        post_data = post['data']
                        break
                else:
                    raise ValueError(f'Post not found! Parameters: {locals()}')

        else:
            post_endpoint = re.sub(r'((https:\/\/)?(www.)?reddit\.com)', self.endpoint, post_url)
            res = requests.get(f'{post_endpoint}', headers=headers)
            res.raise_for_status()
            post_data = res.json()[0]['data']['children'][0]['data']

        self.post_text = post_data['selftext']
        self.post_list.append(post_data)
        self.post_url = post_data['url']
        return self.post_text

    def read_segments(self, delimiter: str = '###') -> None:
        if not self.post_text:
            try:
                self.get_post(self.post_url)
            except KeyError as err:
                raise KeyError from err
            except ValueError as err:
                raise ValueError from err
        for seg in self.post_text.split(delimiter):
            self.post_segments.append(seg)

    def set_genre_data(self) -> None:
        if not self.post_segments:
            self.read_segments()
        for seg in self.post_segments:
            genre_name = re.match(r'(\w+)(?=\n\n\*)', seg)
            if genre_name:
                genre = Genre(genre_name[0].lower(), seg)
                self.post_genres.append(genre)


class Genre:
    def __init__(self, name: str, data: str):
        self.name: str = name
        self.data: str = data
        self.spotify_links: list[str] = []

        self.get_spotify_links()

    def get_spotify_links(self) -> None:
        matches = re.findall(r'(?<=\[\*\*\[Spotify\]\*\*\]\()(.*)(?=\))', self.data)
        if len(matches) > 0:
            [self.spotify_links.append(m) for m in matches]
        else:
            print(f'No matches found for {self.name!r}!')

