import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

_dbEngine = sqlalchemy.create_engine("sqlite:///database", echo=False)
TableBase = declarative_base()
Session = sessionmaker(bind=_dbEngine)()

def GetTableModules():
    tableModules = []
    files = os.listdir('.')
    for file in files:
        filename, fileExt = os.path.splitext(file)
        if fileExt is '.py' and file is not '__init__':
            tableModules.append('.'.join([filename, filename]))
    return tableModules


def Initialize():
    '''
    imports all of the tables to ensure they are added to TableBase
    Then runs create_all funtion to create all of the tables
    '''
    map(__import__, GetTableModules())
    TableBase.metadata.create_all(_dbEngine)
