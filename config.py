import os

class BaseConfig:
    DATABASE = "blog.db"
    SECRET_KEY = "guess what"
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
