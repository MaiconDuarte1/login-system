import json

from app.utils.paths import SESSION_FILE


class SessionManager:
    """
    Manage user sessions.
    """

    @staticmethod
    def save(username):
        """
        Save current session.
        """

        data = {
            "username": username
        }

        with open(
            SESSION_FILE,
            "w",
            encoding="utf-8"
        ) as file:
            json.dump(
                data,
                file,
                indent=4
            )

    @staticmethod
    def load():
        """
        Load current session.
        """

        try:

            with open(
                SESSION_FILE,
                "r",
                encoding="utf-8"
            ) as file:

                return json.load(file)

        except:
            return None

    @staticmethod
    def clear():
        """
        Remove current session.
        """

        with open(
            SESSION_FILE,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump({}, file)