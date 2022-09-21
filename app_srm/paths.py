import os

from decouple import config
from pathlib import Path


root_path = os.curdir
upload_path = Path(root_path, 'download')

USER_OS = config('USER')
USER = config('USER_DB')
PASSWORD = config('PASSWORD')
NAME_DB = 'contract_db'
HOST_DB = config("HOST_DB", default="localhost")

URl_DB = "postgresql+psycopg2://" + USER + ':' + PASSWORD + "@" + HOST_DB + "/" + NAME_DB

