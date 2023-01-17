import os


class BaseCfg(object):
    SECRET_KEY = os.environ.get('SECRET_KEY_DEV')
    DEBUG = False
    TESTING = False


class DevelopmentCfg(BaseCfg):
    DEBUG = True
    TESTING = True


class TestingCfg(BaseCfg):
    DEBUG = False
    TESTING = True


class ProductionCfg(BaseCfg):

    SECRET_KEY = os.environ.get('SECRET_KEY_PROD')
    DEBUG = False
    TESTING = False
