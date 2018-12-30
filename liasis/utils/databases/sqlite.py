from sqlite3 import connect, IntegrityError, Row
from typing import Text

from liasis.core import DatabaseConnector
from liasis.utils.config import config_of

CONFIG = config_of('corpus')

class SQLiteConnector(DatabaseConnector):
    """
    Base class for Database Builders.
    """

    def __init__(self, dir=CONFIG.database_dir) -> None:
        self.dir = dir

    def connect(self, database: Text):
        self.name = self.dir / database
        self.conn = connect(self.name)
        self.conn.row_factory = Row
        return self

    def __enter__(self):
        self.conn.__enter__()
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        return self.conn.__exit__(exc_type, exc_value, traceback)