from os import environ as env

class Telegram:
    API_ID = int(env.get("TELEGRAM_API_ID", "22419004"))
    API_HASH = env.get("TELEGRAM_API_HASH", "34982b52c4a83c2af3ce8f4fe12fe4e1")
    OWNER_ID = int(env.get("OWNER_ID", "6742022802"))
    ALLOWED_USER_IDS = env.get("ALLOWED_USER_IDS", "").split()
    BOT_USERNAME = env.get("TELEGRAM_BOT_USERNAME", "Public_file_to_linkBot")
    BOT_TOKEN = env.get("TELEGRAM_BOT_TOKEN", "7845997152:AAGyKVc0G4OtHPuMn5SzfkeXFdwL27kWb10")
    CHANNEL_ID = int(env.get("TELEGRAM_CHANNEL_ID", "-1001907672237"))
    SECRET_CODE_LENGTH = int(env.get("SECRET_CODE_LENGTH", 4))

class Server:
    BASE_URL = env.get("BASE_URL", "")
    BIND_ADDRESS = env.get("BIND_ADDRESS", "0.0.0.0")
    PORT = int(env.get("PORT", 8080))

# LOGGING CONFIGURATION
LOGGER_CONFIG_JSON = {
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s][%(name)s][%(levelname)s] -> %(message)s',
            'datefmt': '%d/%m/%Y %H:%M:%S'
        },
    },
    'handlers': {
        'file_handler': {
            'class': 'logging.FileHandler',
            'filename': 'event-log.txt',
            'formatter': 'default'
        },
        'stream_handler': {
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        }
    },
    'loggers': {
        'uvicorn': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        },
        'uvicorn.error': {
            'level': 'WARNING',
            'handlers': ['file_handler', 'stream_handler']
        },
        'bot': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        }
    }
}
