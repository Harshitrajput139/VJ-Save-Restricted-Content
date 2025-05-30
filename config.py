import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7937846483:AAGgBl4E1rt3fjZRrnPGAQP0KnUF6FxZWQ0")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "25640530"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "139cd8279e1b70a0ecb7852d832068ca")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "7650071083"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "mongodb+srv://harshitrajput13986:xHdbPj7fiH61bX6l@sharingbot.0ayg3lt.mongodb.net/?retryWrites=true&w=majority&appName=SHARINGBOT") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "SHARINGBOT")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
