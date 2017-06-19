import os

class BaseConfig:
    SECRET = os.getenv("SECRET_KEY", "default secret key")
    ITEMS_PER_PAGE = 10

class DevelopmentConfig(BaseConfig):
    DEBUG = True

class TestingConfig(BaseConfig):
    TESTING = True

config = {
    'develop': DevelopmentConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
