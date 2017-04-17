class Config(object):
    """
    Common configurations across all environments

    """
   
    
class DevelopmentConfig(Config):
    """
    All development configurations
    """
    DEGUG = True #activates debug mode in development env
    SQLALCHEMY_ECHO = True #allows sql to log errors.

class ProductionConfig(Config):
    """
    All production Configurations
    """

    DEBUG = False #deactivate debug mode in production env

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
