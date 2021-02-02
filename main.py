import praw
import API_KEYS

reddit = praw.Reddit(client_id=API_KEYS.API_KEYS['API_CLIENT_ID'],
                     client_secret=API_KEYS.API_KEYS['API_CLIENT_SECRET'],
                     password=API_KEYS.API_KEYS['API_PASSWORD'],
                     user_agent=API_KEYS.API_KEYS['API_USER_AGENT'],
                     username=API_KEYS.API_KEYS['API_USERNAME'])

print(reddit.user.me())

URL = "https://www.reddit.com/r/Techno/"
