from config import Tb, Config as conf
from sqlalchemy import select
from sqlalchemy.orm import Session
from pprint import pprint
engine = conf.engine

def create_users():
    with Session(engine) as session:
        user1 = Tb.User(name='Sponge', fullname='Sponge bob', nickname='nick sponge',
                        addresses=[Tb.Address(email_address="spongebob@sqlalchemy.org")])
        user2 = Tb.User(name='Sandy', fullname='Paul bob', nickname='nick sandy',
                        addresses=[
                            Tb.Address(email_address="sandy@sqlalchemy.org"),
                            Tb.Address(email_address="sandy@squirrelpower.org"),
                        ])
        session.add_all([user1, user2])
        session.commit()
        
def read_users_one_by_one():
    with Session(engine) as session:
        stmt = select(Tb.User).where(Tb.User.name.in_(["spongebob", "sandy"]))
        for user in session.scalars(stmt):
            pprint(user)


def read_users_all():
    with Session(engine) as session:
        stmt = select(Tb.User).where(Tb.User.name.in_(["spongebob", "sandy"]))
        users = session.execute(stmt).all()
        pprint(users)


def select_join():
    res = (
        select(Tb.User.id, Tb.User.name, Tb.Address)  
        .join(Tb.Address.user)
        .where(Tb.User.id == Tb.Address.user_id)
        .where(Tb.User.id == 12)
    )
    with Session(engine) as session:
        res = session.execute(res).all()
        pprint(res)
    
