import customtkinter as ctk

from app.config.settings import settings
from app.core.theme_manager import ThemeManager
from app.utils.paths import APP_ICON

class SettingsView(ctk.CTkToplevel):
    """
    Application settings window.
    """

    def __init__(self, parent):
        super().__init__(parent)
        self.after(200, lambda: self.iconbitmap(str(APP_ICON)))

        self.parent = parent

        self._configure_window()
        self._create_widgets()
        

    def _configure_window(self):
        """
        Configure settings window.
        """

        self.title("Settings")

        self.geometry("480x580")

        self.resizable(False, False)

        self.transient(self.parent)

        self.grab_set()

    def _create_widgets(self):
        """
        Create settings widgets.
        """

        title = ctk.CTkLabel(
            self,
            text="Settings",
            font=("Segoe UI", 24, "bold")
        )

        title.pack(
            pady=(20, 30)
        )

        subtitle = ctk.CTkLabel(
            self,
            text="Customize your application",
            font=("Segoe UI", 13),
            text_color="gray"
        )

        subtitle.pack(pady=(0, 25))

        appearance_label = ctk.CTkLabel(
            self,
            text="Appearance",
            font=("Segoe UI", 15, "bold")
        )

        appearance_label.pack(anchor="w", padx=40)

        self.appearance_menu = ctk.CTkOptionMenu(
            self,
            values=[
                "Dark",
                "Light"
            ]
        )

        self.appearance_menu.set(settings.appearance_mode)

        self.appearance_menu.pack(
            pady=(10, 25),
            padx=40,
            fill="x"
        )

        color_label = ctk.CTkLabel(
            self,
            text="Accent Color",
            font=("Segoe UI", 15, "bold")
        )

        color_label.pack(anchor="w", padx=40)

        self.color_menu = ctk.CTkOptionMenu(
            self,
            values=[
            "blue",
            "green",
            "dark-blue"
        ]
        )

        self.color_menu.set(settings.color_theme)

        self.color_menu.pack(pady=(10, 30), padx=40, fill="x")

        self.save_button = ctk.CTkButton(
            self,
            text="Save",
            command=self.save_settings
        )

        self.save_button.pack(
            padx=40,
            fill="x",
            ipady=8
        )
        

        separator = ctk.CTkFrame(
        self,
        height=1
    )

        separator.pack(
        fill="x",
        padx=30,
        pady=20
    )
        
        about_title = ctk.CTkLabel(
        self,
        text="About",
        font=("Segoe UI", 15, "bold")
    )

        about_title.pack(
            anchor="w",
            padx=40
        )

        about_label = ctk.CTkLabel(
            self,
            text=f"{settings.app_name}\nVersion {settings.version}",
            justify="left",
            text_color="gray"
        )

        about_label.pack(
            anchor="w",
            padx=40,
            pady=(5, 30)
        )


    def save_settings(self):
        """
        Save application settings.
        """

        settings.appearance_mode = (
            self.appearance_menu.get()
        )

        settings.color_theme = (
            self.color_menu.get()
        )

        settings.save()

        ThemeManager.apply_theme()

        self.parent.refresh_current_view()

        self.destroy()