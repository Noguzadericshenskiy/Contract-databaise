import sqlite3

from utils.constants import NAME_BD
from creqte_db.create_bd import drop_bd, create_bd


def creature_bd() -> None:
    """Создает новую БД"""
    with sqlite3.connect(NAME_BD) as conn:
        cur = conn.cursor()
        cur.executescript(drop_bd)
        cur.executescript(create_bd)
