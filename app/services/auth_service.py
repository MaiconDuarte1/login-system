from app.database.connection import DatabaseConnection
from sqlite3 import IntegrityError
import bcrypt

class AuthService:
    """
    Authentication service.
    """

    @staticmethod
    def hash_password(password):
        """hash user password."""

        return bcrypt.hashpw(
            password.encode(),
            bcrypt.gensalt()
        ).decode()

    @staticmethod
    def register(user):

        connection = DatabaseConnection.connect()

        cursor = connection.cursor()

        try:

            cursor.execute(
                """
                INSERT INTO users (
                    username,
                    email,
                    password
                )
                VALUES (?, ?, ?)
                """,
                (
                    user.username,
                    user.email,
                    user.password
                )
            )

            connection.commit()

            return True

        except IntegrityError:

            return False

        finally:

            connection.close()


    @staticmethod
    def login(username, password):
        """Authenticate user."""

        connection = DatabaseConnection.connect()

        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT password
            FROM users
            WHERE username = ?
            """,
            (username,)
        )

        result = cursor.fetchone()

        connection.close()

        if not result:
            return False

        stored_password = result[0]

        return bcrypt.checkpw(
            password.encode(),
            stored_password.encode()
        )