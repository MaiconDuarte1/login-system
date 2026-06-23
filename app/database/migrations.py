from app.database.connection import DatabaseConnection
from app.database.schema import DatabaseSchema


class DatabaseMigration:
    """
    Execute database migrations.
    """

    @staticmethod
    def migrate():
        """
        Create application tables.
        """

        connection = DatabaseConnection.connect()

        cursor = connection.cursor()

        cursor.execute(
            DatabaseSchema.USERS_TABLE
        )

        connection.commit()

        connection.close()