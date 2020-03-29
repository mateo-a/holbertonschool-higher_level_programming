#!/usr/bin/python3
""" script that lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for qry in session.query(State).order_by(State.id).all():
        print("{}: {}".format(qry.id, qry.name))
        for qry_2 in qry.cities:
            print("\t{}: {}".format(qry_2.id, qry_2.name))
    session.close()
    engine.dispose()
