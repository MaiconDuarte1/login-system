import re


class Validators:
    """
    Application validators.
    """

    @staticmethod
    def validate_username(username):
        """
        Validate username.
        """

        return len(username) >= 3

    @staticmethod
    def validate_email(email):
        """
        Validate email.
        """

        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

        return re.match(
            pattern,
            email
        )

    @staticmethod
    def validate_password(password):
        """
        Validate password.
        """

        if len(password) < 8:
            return False

        if not any(
            char.isupper()
            for char in password
        ):
            return False

        if not any(
            char.isdigit()
            for char in password
        ):
            return False

        return True