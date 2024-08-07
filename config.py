from os import environ 

class Config:
    API_ID = environ.get("API_ID", "28611965")
    API_HASH = environ.get("API_HASH", "d36cfa9250dd3d0d46678b538836ca8b")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7250990840:AAHCyAzT5EcX093DV6BPVmbWaoaPw22dNnE") 
    BOT_SESSION = environ.get("BOT_SESSION", "BQG0lX0AM7QgmleMXf6IT2SeES7V_M1lK_bNToNAEgEaMPgzm-C3byIyTbyOu9fhnQRfR1cEfujT3Vd0P-WyxG_lCx0j_GzvqjFLtLuvykutQCLsokZQQXFRyZYdFT2WdQ_j4OiksS66ykCB_mePp8oz-LFllwweMA1tYuwnQs9eBP74AzyLh0cq-4rJs7gnnF-noiFnyT6estEqG9eauPcxMVKYrj2zym9IB6BX9cO_21-1-As4HKputfsjRg5vY_8uFNBQB4Bs1iUcUXwKkv80jhgUlFa5EEW0ynf4F5wBfrdqEm4UIP6votLpJoSZI6e-uSNdOq-9yy8I0FrbOVkO2XGoeAAAAAGwMVb4AQ") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://BinaryBandiT69:UeeYS0XprxPatRjT@db10.jv66i.mongodb.net/?retryWrites=true&w=majority&appName=DB10")
    DATABASE_NAME = environ.get("DATABASE_NAME", "DB10")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '772384743').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
