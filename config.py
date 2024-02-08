import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", 6))
API_HASH = getenv("API_HASH", "eb06d4abfb49dc3eeb1aeb98ae0f581e")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "5281020570:AAFZ0AAFYrlZj4_ZSfL7HVFDaaAVvywQJdw")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Draco:Draco@cluster0.nrqle.mongodb.net/?retryWrites=true&w=majority")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 10))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", -1001593056689))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", 5545068262))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Horikumi/Ghori",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/CheemsBackup")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/CheemsChat")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", True))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "6955f7654fe4484a881cd3041804e861")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "7b525eb06be7469a80a15de0e594fe28")


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 15))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION", "BQASceIAaTQm6CtfHmZ_S1xmF4NLvurZyHsN5bsUHAuF5pJAko8xtjQmvJb1U4oAdjeO60wZQvuNP5kbe_w5h0kFavM-qHyD1RI1mx-Q6la0YILHMxhKdxcXjMR6YSQRUxb4po0DmmTKhKtjm-dcf3Il049i54WI9jmkgeG_MA38LQTz2p_NKq-iW2su2xS_kOwoSF99zfWsmbHL8gb0w8VTRLPiSXnlUhr2EnABVkxZbji7jQVnDdC5BFynBfLrvUSC0xg6gmH_z2hH3ArrmipTkuLgbIjMIjKByMEr8ZkBbDUiPt_PLU9yG7irh-VpUpxHCTvpqH796VHo5mwoREbL8fGx3gAAAAF2BS1SAA")
STRING2 = getenv("STRING_SESSION2", "AQGds_MAIXdHpX5nY83ygalE7GQuGTJZ1dG95IwE6rsfc9yxXZCmk8iKsLrghfX7BwkTVBYXJvwQqm9WcU8-s-TA_UzjTbDO3K8DbWKIFsTC5sZIaefs9hZCq8eATm1CkMUaZU-nQ5FUvwD60wRvPWVY3m1_NaHrU8NEvE4PKm4rquJ0NEUuuLh_RDkRTOWIGCtjapvVhfTTCc0us2f6QpNtFrPK4e_y005xaOQ4R6MVsDvaSRj-nxrj_uM8yEjIcvVugqpk09sE5_nN6mNicSLpad2MUf4zitnR3fs_Slg6je58Tt4dygb3KZK3E9IhBUbm1TNmErnSIDF2wLpSxtB_gfVeoAAAAAE9HQwhAA")
STRING3 = getenv("STRING_SESSION3", "BQGHGBsAp1gLMvHXvfpAOImTSgD8i6qkQ9Zi0Tw13XZYsEOfIkqZYjrxfQXLZcQ2dc-3-j5Of_lM6DTagR2eCJH8eUhgUytan90I41kxZaaEJqNXYW1KOKcTh6t84Ucjl1P3gLAiDzby1SY6it6heKeC9RBbgqVHu7jmjhrF-yKoI6YOPQwy-QII7Fh5v8Xr_B8XgkwKCAf5wpVigyzLLmhmJBz7DWJXG4AHU838KwPXleKAWFyM7K7S94vhE_LxEyqKmjtcQWDhDsCioOwnLJo-ILlWFveQ5ZsgP7FRKf-rRXFe8-sqe_aIVD58xdZ1s30c0rS57pcvERx6if5Bx13TV9rTUgAAAAFv-tKOAA")
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://telegra.ph/file/98c6127186df8dc1d7290.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://telegra.ph/file/98c6127186df8dc1d7290.jpg"
)
PLAYLIST_IMG_URL = "https://te.legra.ph/file/4ec5ae4381dffb039b4ef.jpg"
STATS_IMG_URL = "https://te.legra.ph/file/e906c2def5afe8a9b9120.jpg"
TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
