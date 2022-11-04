from sqlalchemy import MetaData, select
from sqlalchemy.orm import Session
from sqlalchemy.orm import registry
from config import Config as conf, Tb, map_name_to_table
from pprint import pprint
from datetime import date

mapper_registry = registry()

engine = conf.engine
# Using SQLAlchemy reflection example
metadata_obj = MetaData()
metadata_obj.reflect(bind=engine)
tables = metadata_obj.tables
# passign tables to TB
class tempTb(object):
    pass

for tablename in tables:
    setattr(tempTb, tablename.capitalize(), tables[tablename])
    
@map_name_to_table
class User:
    def __repr__(self) -> str:
        return f'User({self.id}, {self.name}, {self.fullname})'

@map_name_to_table
class Address:
    def __repr__(self) -> str:
        return f'Address({self.id}, {self.user_id}, {self.email_address})'

mapper_registry.map_imperatively(Tb.User, tempTb.User)
mapper_registry.map_imperatively(Tb.Address, tempTb.Address)


# User = Table('user', users_meta, autoload_with=engine)

def read_users():
    with Session(engine) as session:
        results = session.query(Tb.User).filter(Tb.User.name=='Sponge')
        pprint(results.all())


def create_users():
    with Session(engine) as session:
        user1 = Tb.User(name='Pablo1', fullname='Sponge bob', nickname='nick sponge', create_date=date.today() )
        user2 = Tb.User(name='Pablo2', fullname='Paul bob', nickname='nick sandy', create_date= date.today())
        session.add_all([user1, user2])
        session.commit()
        user1_addr = Tb.Address(email_address="pablo1@sqlalchemy.org", user_id = user1.id)
        user2_addr1 = Tb.Address(email_address="pablo2_1@sqlalchemy.org", user_id = user2.id)
        user2_addr2 = Tb.Address(email_address="pablo2_2@squirrelpower.org", user_id = user2.id)
        session.add_all([user1_addr, user2_addr1, user2_addr2])
        session.commit()


def reading_last_3_users():
    with Session(engine) as session:
        stmt = (
            select(Tb.User.id,Tb.User.name, Tb.User.create_date)
            .order_by(Tb.User.id.desc())
            .limit(3)
            )
        pprint(session.execute(stmt).all())


def reading_all_users_join_email_address():
    with Session(engine) as session:
        stmt = (
            select(Tb.User, Tb.Address.email_address)
            .join(Tb.Address)
            .where(Tb.User.id == Tb.Address.user_id)
            .order_by(Tb.User.id.asc())
            )
        
        pprint(session.execute(stmt).all())
