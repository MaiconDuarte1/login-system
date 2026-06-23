import customtkinter as ctk

from app.config.settings import settings
from app.services.session_manager import SessionManager
from app.utils.logger import Logger

class DashboardView(ctk.CTkFrame):
    """
    Main application dashboard.
    """

    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent

        session = SessionManager.load()

        self.username = session.get(
            "username",
            "User"
        )

        self.pack(
            fill="both",
            expand=True
        )

        self._create_layout()

    def _create_layout(self):
        """
        Create dashboard layout.
        """

        # Sidebar
        self.sidebar = ctk.CTkFrame(
            self,
            width=220,
            corner_radius=0
        )

        self.sidebar.pack(
            side="left",
            fill="y"
        )

        # Content
        self.content_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        self.content_frame.pack(
            side="right",
            fill="both",
            expand=True,
            padx=30,
            pady=30
        )

        self._create_sidebar()

        self._create_content()

    def _create_sidebar(self):
        """
        Create sidebar widgets.
        """

        title = ctk.CTkLabel(
            self.sidebar,
            text=settings.app_name,
            font=("Segoe UI", 24, "bold")
        )

        title.pack(
            pady=(40, 30)
        )

        dashboard_button = ctk.CTkButton(
            self.sidebar,
            text="Dashboard",
            height=45
        )

        dashboard_button.pack(
            padx=20,
            pady=10,
            fill="x"
        )

        settings_button = ctk.CTkButton(
            self.sidebar,
            text="Settings",
            height=45,
            command=self.open_settings
        )

        settings_button.pack(
            padx=20,
            pady=10,
            fill="x"
        )

        logout_button = ctk.CTkButton(
            self.sidebar,
            text="Logout",
            height=45,
            fg_color="#c0392b",
            hover_color="#a93226",
            command=self.logout
        )

        logout_button.pack(
            side="bottom",
            padx=20,
            pady=30,
            fill="x"
        )

    def _create_content(self):
        """
        Create dashboard content.
        """

        welcome = ctk.CTkLabel(
            self.content_frame,
            text=f"Welcome back, {self.username}!",
            font=("Segoe UI", 32, "bold")
        )

        welcome.pack(
            anchor="w"
        )

        subtitle = ctk.CTkLabel(
            self.content_frame,
            text="You are successfully logged in.",
            font=("Segoe UI", 16),
            text_color="gray"
        )

        subtitle.pack(
            anchor="w",
            pady=(0, 30)
        )

        info_card = ctk.CTkFrame(
            self.content_frame,
            corner_radius=15,
            height=120
        )

        info_card.pack(
            fill="x",
            pady=10
        )

        info_label = ctk.CTkLabel(
            info_card,
            text=f"{settings.app_name}\nVersion {settings.version}",
            font=("Segoe UI", 18)
        )

        info_label.pack(
            pady=35
        )

    def open_settings(self):
        """
        Open settings window.
        """

        from app.views.settings_view import SettingsView

        SettingsView(self.parent)

    def logout(self):
        """
        Return to login screen.
        """

        Logger.info(f"User '{self.username}' logged out.")

        SessionManager.clear()

        self.parent.show_login()