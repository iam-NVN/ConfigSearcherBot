import re
from os import environ

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
USER_SESSION = environ.get('USER_SESSION', 'User_Bot')
API_ID = int(environ['API_ID'])
API_HASH = environ['API_HASH']
BOT_TOKEN = environ['BOT_TOKEN']

# Bot settings
MAX_RESULTS = int(environ.get('MAX_RESULTS', 6))
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))

# Admins, Channels & Users
ADMINS = [int(admin) if re.search('^\d+$', admin) else admin for admin in environ['ADMINS'].split()]
CHANNELS = [int(ch) if re.search('^.\d+$', ch) else ch for ch in environ['CHANNELS'].split()]
auth_users = [int(user) if re.search('^\d+$', user) else user for user in environ['AUTH_USERS'].split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []

# MongoDB information
DATABASE_URI = environ['DATABASE_URI']
DATABASE_NAME = environ['DATABASE_NAME']
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Messages
START_MSG = """
**Hi, I'm Config Searcher bot🔍**

Here you can find most of the Configs for Openbullet in inline mode.
I make it easier for you to find the config you need❣️

**I'm made By @NinjaNaveen

🔹For Requesting Configs and For Reporting Dead Configs in this Bot, Kindly DM @NinjaGiveaways_Bot**
"""
INFO_MSG = """
**Hey there!
I'm made to make it easier for you to find the config you need❣️

Admins:-
@NinjaNaveen
@luciferr_xD
@yourdaddy9999

If you want us to add any config to this bot, Then DM @NinjaGiveaways_Bot
If you find Any dead configs in this bot, Kindly Report it to @NinjaGiveaways_Bot**
"""

SHARE_BUTTON_TEXT = 'Yo, Checkout {username}. There you can find most of the Configs for Openbullet in inline mode. **It make it easier for us to find the config we need❣️**'
