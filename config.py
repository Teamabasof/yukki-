from os import getenv

from dotenv import load_dotenv

load_dotenv()

# VARS

get_queue = {}
STRING = getenv("STRING_SESSION", "AgB0-_NdUZX9F8r0fDpxM8IknD-cxQTTU6BYTkNS5Lw42dxa4pTCuPlrG-kU6yBwwcUTGl8Z1Ejc5HXiOo9H-_jNsmxhz_SyvIOLplNdZGi7aI0ZkOcP4rp-yMUtMBYL9l9IOCA54_nSrhpPwdG6672fnn5TlhZMibVh79qXRS5VpcycHIOSa-87ckXql_LVZKhGh0w_wDeppRSYYcewgUrMUlilT6AJ4jvBbppb_s0Uz2N1pxXSFtWa6GYUhl7oUuu3ahfRxdb9Iboh_prlD0s637sJTBdYbP61t8NogvWjlWdCNk4RzIuH7ts7ox5mNXvCI0zwYkY_gWh5bQR-xMDmAAAAAT8q85oA")
BOT_TOKEN = getenv("BOT_TOKEN", "5681957815:AAH3HubFdioBKAUuUnc2LvNqM5o8pDRXdPM")
API_ID = int(getenv("API_ID", "15954332"))
API_HASH = getenv("API_HASH", "85adea6f1eaf068b707703b4846a9ced")
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "10"))
ASSISTANT_PREFIX = list(getenv("ASSISTANT_PREFIX", ".").split())
MONGO_DB_URI = getenv("MONGO_DB_URI", "~mongodb+srv://music:music@cluster0.sh6h4.mongodb.net/myFirstDatabase?retryWrites=true&w=majority`")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5134595693").split()))
OWNER_ID = list(map(int, getenv("OWNER_ID", "5508658149").split()))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001737573985"))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "AzeSongRobot")
if str(getenv("SUPPORT_CHANNEL")).strip() == "":
    SUPPORT_CHANNEL = None
else:
    SUPPORT_CHANNEL = str(getenv("SUPPORT_CHANNEL", "apkprogram1"))
if str(getenv("SUPPORT_GROUP")).strip() == "":
    SUPPORT_GROUP = None
else:
    SUPPORT_GROUP = str(getenv("SUPPORT_GROUP", "oldsupport"))
