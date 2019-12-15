from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# engine = create_engine('mysql+pymysql://root:password@localhost/database_name')
engine = create_engine('sqlite:///sqlalchemy_example.db')
Session = sessionmaker(bind=engine)

Base = declarative_base()
