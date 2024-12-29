import os

class Settings:
    # general settings
    APP_NAME: str = "E-Library Management System"
    VERSION: str = "1.0.0"
    DEBUG: bool = True
    
    # environment configurations
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")
    BASE_URL: str = os.getenv("BASE_URL", "http://127.0.0.1:8000")
    
    # authentication (future scope)
    SECRET_KEY: str = os.getenv("SECRET_KEY", "yet-to-be-determined")
    
    # database configurations
    
settings = Settings()