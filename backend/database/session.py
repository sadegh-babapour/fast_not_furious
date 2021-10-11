from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
#======================================
from backend.environment import environ

SQL_ALCHEMY_DATASBASE_URL = environ.DATABASE_URL

engine = create_engine(SQL_ALCHEMY_DATASBASE_URL)

local_session = sessionmaker(autocommit = False, autoflush = False, bind = engine)


