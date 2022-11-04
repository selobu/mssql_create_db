__all__ = ['Tb', 'map_name_to_table','Config']

class TbContainer(object):
    pass

Tb = TbContainer()

def map_name_to_table(cls):
    if hasattr(Tb, cls.__name__):
        raise Exception(f'ya esta declarada la tabla {cls.__name__}')
    setattr(Tb, cls.__name__, cls)


class Config(object):
    driver = 'ODBC Driver 17 for SQL Server'
    username = ''
    password = ''
    server = 'localhost'
    database = 'Nuevo'
    # engine_stmt = f"mssql+pyodbc://{username}:{password}@{server}/{database}?DRIVER={driver}"
    # uri = 'DRIVER={SQL Server Native Client 11.0};SERVER=localhost;DATABASE=Test;Trusted_Connection=yes'
    SQLALCHEMY_DATABASE_URI = f"mssql+pyodbc://{username}:{password}@{server}/{database}?driver={driver}"
