from app.core.theme_manager import ThemeManager
from app.utils.paths import ICONS_DIR


class IconManager:
    """
    Manage application icons according to the current theme.
    """

    @staticmethod
    def get_icon(icon_name: str):
        """
        Return the appropriate icon path based on theme.

        Args:
            icon_name (str): Base icon name.

        Returns:
            Path: Icon path.
        """

        current_theme = ThemeManager.get_appearance_mode()

        if current_theme.lower() == "light":
            return ICONS_DIR / f"{icon_name}_black.png"

        return ICONS_DIR / f"{icon_name}.png"