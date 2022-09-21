from pathlib import Path

from app_srm.models import engine, Base


def drop_all_table():
    Base.metadata.drop_all(engine)


def creation_all_table():
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    drop_all_table()
    creation_all_table()
