from config import Config
from sqlalchemy import create_engine, Engine


class Database:

    def __init__(self, *, config: Config):
        self.config = config

    def get_engine(self, conn_str: str) -> Engine:
        """
        Let the engine raise if the connection string is incorrect
        :param conn_str:
        :return:
        """
        engine = create_engine(conn_str)
        return engine

    def get_db_conn(self) -> str:
        """
        Get the db connection string
        :return:
        """
        url = f"sqlite:///{self.config.SQLITE_DATABASE_NAME}"
        return url
