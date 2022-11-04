
from config import Config as conf
from sqlalchemy import create_engine

SQLALCHEMY_DATABASE_URI = conf.SQLALCHEMY_DATABASE_URI

engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True) # pool_recycle = 3600,
setattr(conf, 'engine', engine)

DECLARATIVE = False
if DECLARATIVE:
    from model import Base
    metadata = Base.metadata
    print('//---------------------------//')
    print('// CREATING TABLES //')
    metadata.create_all(engine)
    # setting engine to config

    import routes
    print('//---------------------------//')
    print('// CREATING USERS //')
    #routes.create_users()

    print('//---------------------------//')
    print('// READING USERS ONE BY ONE //')
    #routes.read_users_one_by_one()

    print('//---------------------------//')
    print('// READING USERS ALL AT TIME //')
    #routes.read_users_all()

    print('//---------------------------//')
    print('// SELECT WITH JOIN //')
    routes.select_join()
else:
    # working with the database as unknown structure
    import  reflect
    print('//-----------------------------//')
    print('// READING USERS FROM REFLECT //')
    #reflect.read_users()
    
    print('//-----------------------------//')
    print('// CREATIN USERS//')
    #reflect.create_users()
    
    print('//-----------------------------//')
    print('// readign last 3 users//')
    reflect.reading_last_3_users()
    
    print('//-----------------------------//')
    print('// reading all users //')
    reflect.reading_all_users_join_email_address()
    a = 1
