import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

_dbEngine = sqlalchemy.create_engine("sqlite:///Database/data.sqlite", echo=False)
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


def ImportModules(modules):
    map(__import__, modules)


def Initialize():
    '''
    imports all of the table modules and initializes the database after they have been added
    tests are added to TableBase.metadata as a side effect of being inherited.
    '''
    modules = GetTableModules()
    ImportModules(modules)
    TableBase.metadata.create_all(_dbEngine)
