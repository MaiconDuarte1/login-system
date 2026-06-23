import customtkinter as ctk

from app.config.settings import settings


class ThemeManager:
    """
    Manage application theme settings.
    """

    @staticmethod
    def apply_theme():
        """
        Apply application theme.
        """

        appearance_mode = (
            settings.appearance_mode
            if settings.appearance_mode
            else "Dark"
        )

        ctk.set_appearance_mode(
            appearance_mode
        )

        ctk.set_default_color_theme(
            settings.color_theme
        )

    @staticmethod
    def get_appearance_mode():
        """
        Return current appearance mode.
        """

        return settings.appearance_mode

    @staticmethod
    def set_appearance_mode(mode: str):
        """
        Update appearance mode.
        """

        settings.appearance_mode = mode

        settings.save()

        ctk.set_appearance_mode(mode)

    @staticmethod
    def is_dark():
        """
        Return True if current theme is Dark.
        """

        return settings.appearance_mode.lower() == "dark"