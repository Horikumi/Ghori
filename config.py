import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "6"))
API_HASH = getenv("API_HASH", "eb06d4abfb49dc3eeb1aeb98ae0f581e")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "5281020570:AAHGgFNVCEtz-iv9b3A10c5JOTH0PeeCN84")

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
STRING1 = getenv("STRING_SESSION", "AQD8GTcAOu43YuMAYbiB3RwZKjhn3wCL8HOG-z8N6JyHQe19FSxgf35dyc5qVMnRRWcWOD9OQj6Ivv5PCzpcBLKibajEArajK7Njp5bvqbT1MY0i20ak1Oj09AkcV8yjqUY6SCB0A_XIqptbIFyf_yKnOovWMAE3Kjp65EYwz51FrNNknS0miLvP5H-M4wB0LLLHKXJ2bqMt0_daHOOY3ey50W9pUz-IFw4fRNpgNPsIxY1LWc6FkTfFm3mdvlYwsHUJ7nwijcC1x03k4mDHlvySknOPRmCMb19Wwvn-25aSzeqvcLSbgLSmEUJsTHay8X7o6J8oD7b7g0GkILxHIDkcmbJhNgAAAAEzHL6XAA")
STRING2 = getenv("STRING_SESSION2", "AQGds_MAGXq4tmhuJfJw1NkImW-pYvKb-J79OTW_ygErOou8cty6BtFAkLT2IAHeWQk7f7CePeWEq01RB-8nQsDcNkApvdhor4q4M1OTs-bm4-MQPLcnb6e2Nm4uGvsTRnLqZVbM_v1-3WTE17BxGD2uI5Kg7Ub_139WBDLukc-vfwmCzZltp1tKtzOXFb39p_P_I_SqxXD102VetjOBzPZ_gA4io9HokkqIpCy6TuEGH7sNHCXfVZDwfOeqz2oOmRcS_Sz-LviaodRem4KdXPvpPIqLKfyNJZ5xPf0IZNhkPEfLvbdpq_T7MtDwYzvPoT8Sed19OhsS0IxPRQZiMt17aQldMgAAAAE9HQwhAA")
STRING3 = getenv("STRING_SESSION3", None)
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
