from database.crud import engine
from database.models import Base

import sys

def create_database():
    Base.metadata.create_all(engine)


def recreate_database():
    Base.metadata.drop_all(engine)
    create_database()

if __name__ == "__main__":
    option = sys.argv[1]
    if option == '-c':
        create_database()
        print("DATABASE CREATED")

    elif option == '-r':
        recreate_database()
        print("DATABASE RECREATED")
    
    else:
        print("'{}' option not found".format(option))
