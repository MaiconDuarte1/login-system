import json
from pathlib import Path
from app.utils.paths import DATABASE_FILE

class Settings:
    def __init__(self):
        self.config_path = (
            Path(__file__).parent / "app_config.json"
        )

        self._load()

        if not self.appearance_mode:
            self.appearance_mode = "Dark"

    def _load(self):
            with open(
                self.config_path,
                "r",
                encoding="utf-8"
            ) as file:
                config = json.load(file)

            # App
            self.app_name = config["app_name"]
            self.version = config["version"]

            # Window
            self.window_width = config["window"]["width"]
            self.window_height = config["window"]["height"]
            self.resizable = config["window"]["resizable"]

            # Theme
            self.appearance_mode = config["theme"]["appearance_mode"]
            self.color_theme = (config["theme"].get("color_theme", "blue"))

            # Login
            self.remember_me = config["login"]["remember_me"]
            self.show_register_button = config["login"]["show_register_button"]
            self.show_forgot_password = config["login"]["show_forgot_password"]

            # Database
            self.database_name = DATABASE_FILE

            # Logs
            self.logs_enabled = config["logs"]["enabled"]
            self.log_level = config["logs"]["level"]

    def save(self):
        """
        Save settings to app_config.json.
        """

        config_data = {
            "app_name": self.app_name,
            "version": self.version,

            "window": {
                "width": self.window_width,
                "height": self.window_height,
                "resizable": self.resizable
            },

            "theme": {
                "appearance_mode": self.appearance_mode,
                "color_theme": self.color_theme
            },

            "login": {
                "remember_me": self.remember_me,
                "show_register_button": self.show_register_button,
                "show_forgot_password": self.show_forgot_password
            },

            "database": {
                "name": self.database_name
            },

            "logs": {
                "enabled": self.logs_enabled,
                "level": self.log_level
            }
        }

        with open(
            self.config_path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                config_data,
                file,
                indent=4
            )

settings = Settings()