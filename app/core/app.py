import customtkinter as ctk

from app.config.settings import settings
from app.core.theme_manager import ThemeManager
from app.utils.paths import APP_ICON

from app.views.login_view import LoginView
from app.views.register_view import RegisterView
from app.views.dashboard_view import DashboardView
from app.database.migrations import DatabaseMigration
from app.services.session_manager import SessionManager
from app.utils.logger import Logger
from app.views.forgot_password_view import ForgotPasswordView


class LoginSystem(ctk.CTk):
    """Main application class.

    Handles window configuration, theme management,
    and screen navigation."""
    def __init__(self):
        super().__init__()

        Logger.setup()

        self._configure_theme()
        DatabaseMigration.migrate()
        self._configure_window()
        self._create_views()

    def _configure_theme(self):
        ThemeManager.apply_theme()

    def _create_views(self):
        """create initial application view."""

        session = SessionManager.load()

        if session and session.get("username"):
            self.show_dashboard()

        else:
            self.show_login()

            
    def clear_window(self):

        for widget in self.winfo_children():
            widget.destroy()


    def show_login(self):

        self.clear_window()

        self.current_view = LoginView(self)

    def show_dashboard(self):
        """Show dashboard view."""


        self.clear_window()
        self.current_view = DashboardView(self)


    def show_register(self):

        self.clear_window()

        self.current_view = RegisterView(self)

    def _configure_window(self):
        self.title(
            f"{settings.app_name} v{settings.version}"
        )

        try:
            self.iconbitmap(str(APP_ICON))
        except Exception as e:
            print(f"Erro ao carregar ícone: {e}")

        self.geometry(
            f"{settings.window_width}x{settings.window_height}"
        )

        self.resizable(
            settings.resizable,
            settings.resizable
        )

        self._center_window()

    def _center_window(self):
        self.update_idletasks()

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (
            screen_width - settings.window_width
        ) // 2

        y = (
            screen_height - settings.window_height
        ) // 2

        self.geometry(
            f"{settings.window_width}x{settings.window_height}+{x}+{y}"
        )

    def refresh_current_view(self):

        current_class = type(self.current_view)

        self.clear_window()

        self.current_view = current_class(self)

    
    def show_forgot_password(self):
        """Show forgot password view."""


        self.clear_window()

        self.current_view = ForgotPasswordView(self)