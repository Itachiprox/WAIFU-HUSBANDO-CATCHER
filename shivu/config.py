class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "5490773419"
    sudo_users = "5228565677", "6590287973"
    GROUP_ID = -1002037503706
    TOKEN = "6878148789:AAEjZJTGRDyfOv5eD1kWn6f7mu7YDgMJeyc"
    mongo_url = "mongodb+srv://itachi:itachi@itachi.hyhnjlq.mongodb.net/?retryWrites=true&w=majority"
    PHOTO_URL = ["https://telegra.ph/file/b925c3985f0f325e62e17.jpg", "https://telegra.ph/file/4211fb191383d895dab9d.jpg"]
    SUPPORT_CHAT = "waifu_support"
    UPDATE_CHAT = "catchlogs"
    BOT_USERNAME = "Catchyourwaifubot"
    CHARA_CHANNEL_ID = "-1002037503706"
    api_id = 24658337
    api_hash = "bf99242dbb7f3501f28d39f0a0383cbf"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
