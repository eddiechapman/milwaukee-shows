import os
import pathlib
import dotenv

env_path = pathlib.Path('.', '.env')
load_dotenv(dotenv_path=env_path)


class BaseConfig:
    DEBUG = False
    TESTING = False
    TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
    TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
    TWILIO_FROM = os.getenv('TWILIO_FROM')


class Testing(BaseConfig):
    TESTING = True
    DEBUG = True


class Development(BaseConfig):
    DEBUG = True


class Production(BaseConfig):
    pass
