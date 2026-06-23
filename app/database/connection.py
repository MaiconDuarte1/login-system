import sqlite3
from pathlib import Path

from app.config.settings import settings


class DatabaseConnection:
    """
    SQLite database connection manager.
    """

    @staticmethod
    def connect():
        """
        Create database connection.
        """

        Path(
            settings.database_name
        ).parent.mkdir(
            parents=True,
            exist_ok=True
        )

        return sqlite3.connect(
            settings.database_name
        )