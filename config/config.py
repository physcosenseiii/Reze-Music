import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", "19153401"))
API_HASH = getenv("API_HASH", "9171b6aaf9020d8162377749e8834daf")

BOT_TOKEN = getenv("BOT_TOKEN", "5360188482:AAFjv3fCoB3QSpdoUasnH_ACpZ452wqfbUU")

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://vc:vc123@cluster0.vhiuo.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID" "-1001641370717"))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "Reze")

OWNER_ID = list(map(int, getenv("OWNER_ID", "922499043").split()))

HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)

UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/physcosenseiii/Reze-Music")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv("GIT_TOKEN", "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")

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Reze_Upadtes")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/Zeke_Grp")

SUPPORT_HEHE = SUPPORT_GROUP.split("me/")[1]

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "180"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180"))

AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "False")
AUTO_LEAVE_ASSISTANT_TIME = int(
    getenv("ASSISTANT_LEAVE_TIME", "5400")
)

AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", "True")

PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)

YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "5"))
TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "3"))

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "eb80586d720c459d869588d8eec4f971")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "8418655380194e578edde65c2c1ff7ba")

VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "5"))
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "50"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "50"))

CLEANMODE_DELETE_MINS = int(getenv("CLEANMODE_MINS", "12"))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824"))
# https://www.gbmb.org/mb-to-bytes

STRING1 = getenv("STRING_SESSION", "BQCeNrKZ9glbIMLayriN6YX93boRjTD1WBdHBcByyNJUxJKO74jlynwXKunqaCoVNRBSPo_l9ccbILML-MUPiJlAv9DdtgO7LWoImeZ2fxXr16_NPkE7bYJK_afV8xeJS-7-NiTvqO6jlgtmtePvrPj3E4srFpcCfcOJzR9kS_RGx0GOF9FWEa8gxl6B-12Y1EsOulvnwB3JxlQdP4gwlWkysqHQDj2vMxTCHgJTGnoLVuoAdifdl1FQl4R4lEDAx317ac9vK4Xj8QQidWuO0hX_1RZfgVt9Wja0ayQUNh0w8i3ROzZ0uDAk_T8RTNP7hamPt-eI8eM3pzr8LELHs6QbAAAAATVebwsA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "anonxlogs.txt"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}
autoclean = []


START_IMG_URL = getenv("START_IMG_URL", "https://te.legra.ph/file/91079f1d13cb0cc005b72.jpg")

PING_IMG_URL = getenv(
    "PING_IMG_URL",
    "https://te.legra.ph/file/5ab85c930fc3f227caaf2.jpg",
)

PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b2a7ff299640dc9672c.jpg"

GLOBAL_IMG_URL = "https://te.legra.ph/file/95b2a7ff299640dc9672c.jpg"

STATS_IMG_URL = "https://te.legra.ph/file/e906c2def5afe8a9b9120.jpg"

TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/7bb8fcb47b352216a6188.jpg"

TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/7bb8fcb47b352216a6188.jpg"

STREAM_IMG_URL = "https://te.legra.ph/file/7bb8fcb47b352216a6188.jpg"

SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/7bb8fcb47b352216a6188.jpg"

YOUTUBE_IMG_URL = "https://te.legra.ph/file/7bb8fcb47b352216a6188.jpg"

SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/7bb8fcb47b352216a6188.jpg"

SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/7bb8fcb47b352216a6188.jpg"

SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/7bb8fcb47b352216a6188.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(
        int(x) * 60**i
        for i, x in enumerate(reversed(stringt.split(":")))
    )


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00")
)


if UPSTREAM_REPO:
    if not re.match("(?:http|https)://", UPSTREAM_REPO):
        print(
            "[ERROR] - Your UPSTREAM_REPO url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if PING_IMG_URL:
    if PING_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", PING_IMG_URL):
            PING_IMG_URL = "https://te.legra.ph/file/5ab85c930fc3f227caaf2.jpg"

if START_IMG_URL:
    if START_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", START_IMG_URL):
            START_IMG_URL = "https://te.legra.ph/file/91079f1d13cb0cc005b72.jpgg"
