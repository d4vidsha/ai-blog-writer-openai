from modules.store_client import *
store = StoreClient("bad79293-00b7-4e71-b0d7-4607b18c855f")

## OPENAI STUFF
OPENAI_API_KEY = store.get("OpenAI-API-key")


## FLASK STUFF
class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    SECRET_KEY = "3kjlqhfejakdlbiodfsafenwavcxozkhdsaq"


config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}
