import os

class Config(object):
    # get a token from @BotFather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "1317475628:AAHVe8cZFS7njFgQiUKn2sgkMpXZL3leRn8")
    # The Telegram API things
    APP_ID = int(os.environ.get("APP_ID", 1667813))
    API_HASH = os.environ.get("API_HASH", "1f6921c27bf6cd01aba471a14ff33bcb")
    OWNER_ID = int(os.environ.get("OWNER_ID", 1326703864))
    # Get these values from my.telegram.org
    # to store the channel ID who are authorized to use the bot
    AUTH_CHANNEL = set(int(x) for x in os.environ.get("AUTH_CHANNEL", "-1001189650778").split())
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    # Telegram maximum file upload size
    MAX_FILE_SIZE = 50000000
    TG_MAX_FILE_SIZE = 2097152000
    FREE_USER_MAX_FILE_SIZE = 50000000
    # chunk size that should be used with requests
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))
    # default thumbnail to be used in the videos
    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "https://placehold.it/90x90")
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096
    # set timeout for subprocess
    PROCESS_MAX_TIMEOUT = 3600
    #
    ARIA_TWO_STARTED_PORT = int(os.environ.get("ARIA_TWO_STARTED_PORT", 6800))
    EDIT_SLEEP_TIME_OUT = int(os.environ.get("EDIT_SLEEP_TIME_OUT", 1))
    MAX_TIME_TO_WAIT_FOR_TORRENTS_TO_START = int(os.environ.get("MAX_TIME_TO_WAIT_FOR_TORRENTS_TO_START", 600))
    MAX_TG_SPLIT_FILE_SIZE = int(os.environ.get("MAX_TG_SPLIT_FILE_SIZE", 2097152000))
    # add config vars for the display progress
    FINISHED_PROGRESS_STR = os.environ.get("FINISHED_PROGRESS_STR", "■  ")
    UN_FINISHED_PROGRESS_STR = os.environ.get("UN_FINISHED_PROGRESS_STR", "□  ")
    # add offensive API
    TG_OFFENSIVE_API = os.environ.get("TG_OFFENSIVE_API", None)
    CUSTOM_FILE_NAME = os.environ.get("CUSTOM_FILE_NAME", "")
    LEECH_COMMAND = os.environ.get("LEECH_COMMAND", "leech@MalavikaMohan_Bot")
    YTDL_COMMAND = os.environ.get("YTDL_COMMAND", "ytdl@MalavikaMohan_Bot")
    RCLONE_CONFIG = os.environ.get("RCLONE_CONFIG", "")
    DESTINATION_FOLDER = os.environ.get("DESTINATION_FOLDER", "MalavikaMohan")
    GLEECH_COMMAND = os.environ.get("GLEECH_COMMAND", "gleech@MalavikaMohan_Bot")
    INDEX_LINK = os.environ.get("INDEX_LINK", "")
    TELEGRAM_LEECH_COMMAND_G = os.environ.get("TELEGRAM_LEECH_COMMAND_G", "tleech@MalavikaMohan_Bot")
    CANCEL_COMMAND_G = os.environ.get("CANCEL_COMMAND_G", "cancel")
    GET_SIZE_G = os.environ.get("GET_SIZE_G", "getsize@MalavikaMohan_Bot")
    STATUS_COMMAND = os.environ.get("STATUS_COMMAND", "status@MalavikaMohan_Bot")
    SAVE_THUMBNAIL = os.environ.get("SAVE_THUMBNAIL", "savethumb@MalavikaMohan_Bot")
    CLEAR_THUMBNAIL = os.environ.get("CLEAR_THUMBNAIL", "clearthumb@MalavikaMohan_Bot")
    UPLOAD_AS_DOC = os.environ.get("UPLOAD_AS_DOC", "True")
    PYTDL_COMMAND_G = os.environ.get("PYTDL_COMMAND_G", "pytdl@MalavikaMohan_Bot")
    LOG_COMMAND = os.environ.get("LOG_COMMAND", "log@MalavikaMohan_Bot")
