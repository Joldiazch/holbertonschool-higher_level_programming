#!/usr/bin/python3

""" Firs query form SqlAlchemy """

from sys import argv
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]),
        pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()

    state = session.query(State).\
        filter(State.name == 'Louisiana').order_by(State.id).one_or_none()

    if state is not None:
        print(state.id)
    else:
        print("Not found")

    session.close()
