import os
class Environment():
    POSTGRES_USER = os.environ.get("POSTGRES_USER")
    POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
    POSTGRES_SERVER_ADDRESS = os.environ.get("POSTGRES_SERVER_ADDRESS")
    POSTGRES_PORT = os.environ.get("POSTGRES_PORT")
    POSTGRES_DATABASE = os.environ.get("POSTGRES_DATABASE")
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER_ADDRESS}:{POSTGRES_PORT}/{POSTGRES_DATABASE}"

environ = Environment()

# export var=value