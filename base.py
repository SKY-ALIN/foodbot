from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import config

engine = create_engine('mysql+pymysql://root:password@localhost/database_name')
Session = sessionmaker(bind=engine)

Base = declarative_base()
