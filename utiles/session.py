from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import config
import os

def Session():
    path = os.path.join(config.BASE_PATH,'models','Sql.db3')
    engine = create_engine(f'sqlite:///{path}')
    DBsession = sessionmaker(bind=engine)
    return DBsession()