import os
import logging
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler

# Load environment variables from .env file
load_dotenv()

# Fetch bot token and API credentials from environment variables
TG_BOT_TOKEN = os.getenv("TG_BOT_TOKEN")
APP_ID = int(os.getenv("APP_ID", "20511201"))
API_HASH = os.getenv("API_HASH")
CHANNEL_ID = int(os.getenv("CHANNEL_ID", "1002458885592"))
OWNER_ID = int(os.getenv("OWNER_ID", "8189717881"))
PORT = os.getenv("PORT", "8080")

# Validate that all necessary environment variables are loaded
if not TG_BOT_TOKEN or not API_HASH:
    raise Exception("TG_BOT_TOKEN and API_HASH must be set in the .env file")

# Database credentials
DB_URI = os.getenv("DATABASE_URL", "mongodb+srv://username:password@cluster0.mongodb.net/dbname")
DB_NAME = os.getenv("DATABASE_NAME", "bot_database")

# Force sub channel ID and join request settings
FORCE_SUB_CHANNEL = int(os.getenv("FORCE_SUB_CHANNEL", "0"))
JOIN_REQUEST_ENABLE = os.getenv("JOIN_REQUEST_ENABLED", None)

# Bot workers setting
TG_BOT_WORKERS = int(os.getenv("TG_BOT_WORKERS", "4"))

# Start message and media
START_PIC = os.getenv("START_PIC", "https://yourimageurl.com/image.jpg")
START_MSG = os.getenv("START_MESSAGE", "Hello {first}\n\nI can store private files in the specified Channel and other users can access them via a special link.")

# Admins list (ensure valid admin IDs)
ADMINS = []
try:
    for x in os.getenv("ADMINS", "8189717881").split():
        ADMINS.append(int(x))
except ValueError:
    raise Exception("Your Admins list does not contain valid integers.")

# Force subscription message
FORCE_MSG = os.getenv("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join my Channel/Group to use me. Kindly please join the Channel.</b>")

# Custom caption for files
CUSTOM_CAPTION = os.getenv("CUSTOM_CAPTION", None)

# Protect content from being forwarded
PROTECT_CONTENT = True if os.getenv('PROTECT_CONTENT', "False") == "True" else False

# Auto delete time in seconds
AUTO_DELETE_TIME = int(os.getenv("AUTO_DELETE_TIME", "0"))
AUTO_DELETE_MSG = os.getenv("AUTO_DELETE_MSG", "This file will be automatically deleted in {time} seconds. Please ensure you have saved any necessary content before this time.")
AUTO_DEL_SUCCESS_MSG = os.getenv("AUTO_DEL_SUCCESS_MSG", "Your file has been successfully deleted. Thank you for using our service. ✅")

# Disable Channel button for posts
DISABLE_CHANNEL_BUTTON = os.getenv("DISABLE_CHANNEL_BUTTON", None) == 'True'

# Bot stats and user replies
BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly, I'm only a File Sharing bot!"

# Append the owner ID and any additional admin IDs
ADMINS.append(OWNER_ID)
ADMINS.append(1250450587)

# Logging configuration
LOG_FILE_NAME = "filesharingbot.log"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)

# Set logger for pyrogram to show warnings and above
logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
