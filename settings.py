import os

from dotenv import load_dotenv

load_dotenv()

tg_key = os.getenv('BOT_TOKEN')


class SiteSettings:
    api_key = os.getenv('SITE_TOKEN')
    site_url = 'https://api.kinopoisk.dev/v1.4/movie'
