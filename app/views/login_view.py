import customtkinter as ctk

from app.components.custom_entry import CustomEntry

from PIL import Image

from app.utils.paths import LOGIN_BANNER
from app.core.icon_manager import IconManager
from app.views.settings_view import SettingsView
from app.core.theme_manager import ThemeManager
from app.services.auth_service import AuthService
from app.components.custom_dialog import CustomDialog
from app.services.session_manager import SessionManager
from app.utils.logger import Logger

class LoginView(ctk.CTkFrame):
    """
    Login screen of the application.

    Responsible for displaying the authentication form,
    navigation to the registration screen, and future
    login validation.
    """
    def __init__(self, parent):
        """
        Initialize the login view.

        Args:
            parent: Main application window.
        """
        super().__init__(parent)

        self.parent = parent

        self.pack(fill="both", expand=True)

        self._configure_grid()
        self._create_frames()
        self._create_banner()
        self._create_login_header()
        self._create_settings_button()

    def _configure_grid(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.grid_rowconfigure(0, weight=1)

    def _create_frames(self):
        """
        Create the main layout frames.

        The left frame contains the banner image,
        while the right frame contains the login form.
        """
        self.left_frame = ctk.CTkFrame(
        self,
        fg_color="transparent",
        corner_radius=0
        )

        self.left_frame.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        self.right_frame = ctk.CTkFrame(
            self,
            corner_radius=0,
            fg_color="transparent",
        )

        self.right_frame.grid(
            row=0,
            column=1,
            sticky="nsew"
        )

    def _create_banner(self):
        try:
            image = Image.open(LOGIN_BANNER)

            self.banner_image = ctk.CTkImage(
                light_image=image,
                dark_image=image,
                size=(760, 760)
            )

            self.banner_label = ctk.CTkLabel(
                self.left_frame,
                text="",
                image=self.banner_image
            )

            self.banner_label.pack(
                expand=True
            )

        except Exception as error:
            print(f"Erro ao carregar banner: {error}")

            self.banner_label = ctk.CTkLabel(
                self.left_frame,
                text="LOGIN BANNER",
                font=("Segoe UI", 28, "bold")
            )

            self.banner_label.pack(
                expand=True
            )

    def _create_login_header(self):

        self.content_frame = ctk.CTkFrame(
            self.right_frame,
            fg_color="transparent"
        )

        self.content_frame.pack(
            expand=True,
            pady=40
        )

        self.title_label = ctk.CTkLabel(
            self.content_frame,
            text="Welcome Back",
            font=("Segoe UI", 28, "bold")
        )

        self.title_label.pack(
            pady=(0, 10)
        )

        self.subtitle_label = ctk.CTkLabel(
            self.content_frame,
            text="Sign in to continue",
            font=("Segoe UI", 14)
        )

        self.subtitle_label.pack(
            pady=(0, 40)
        )

        self.username_entry = CustomEntry(
            self.content_frame,
            placeholder="Username",
            icon_path=IconManager.get_icon("user")
        )

        self.username_entry.pack(
            pady=10
        )

        self.password_entry = CustomEntry(
            self.content_frame,
            placeholder="Password",
            icon_path=IconManager.get_icon("lock"),
            is_password=True

        )

        self.password_entry.pack(
            pady=10
        )

        self.options_frame = ctk.CTkFrame(
            self.content_frame,
            fg_color="transparent"
        )

        self.options_frame.pack(
            fill="x",
            padx=20,
            pady=(5, 20)
        )

        self.remember_checkbox = ctk.CTkCheckBox(
            self.options_frame,
            text="Remember me",
            font=("Segoe UI", 12),
            checkbox_width=16,
            checkbox_height=16,
            text_color=("gray40", "gray70")
        )

        session = SessionManager.load()

        if session and session.get("username"):
            self.remember_checkbox.select()
        else:
            self.remember_checkbox.deselect()


        self.remember_checkbox.pack(
            side="left"
        )


        self.forgot_password_label = ctk.CTkLabel(
            self.options_frame,
            text="Forgot Password?",
            cursor="hand2",
            font=("Segoe UI", 11),
            text_color="#9A9A9A"
        )

        self.forgot_password_label.bind("<Button-1>", lambda event: self.open_forgot_password())

        self.forgot_password_label.pack(
            side="right"
        )

        self.login_button = ctk.CTkButton(
            self.content_frame,
            text="Login",
            width=400,
            height=50,
            fg_color="#8B5CF6",
            hover_color="#7C3AED",
            corner_radius=25,
            command=self.login
        )

        self.login_button.pack(
            pady=(0, 25)
        )

        self.or_label = ctk.CTkLabel(
            self.content_frame,
            text="──────────── OR ────────────"
        )

        self.or_label.pack(
            pady=15
        )

        border_color = (
            "#FFFFFF" if ThemeManager.is_dark()
            else "#222222"
        )

        text_color = (
            "#FFFFFF" if ThemeManager.is_dark()
            else "#222222"
        )

        self.register_button = ctk.CTkButton(
            self.content_frame,
            text="Create Account",
            width=400,
            height=50,
            corner_radius=25,
            fg_color="transparent",
            border_width=1,
            border_color=border_color,
            text_color=text_color,
            command=self.open_register
        )

        self.register_button.pack(
            pady=15
        )



    def open_forgot_password(self):
        """Open forgot password screen."""

        self.parent.show_forgot_password()



    def open_register(self):
        """
        Open the registration screen.
        """
        self.parent.show_register()

    def _create_settings_button(self):

        settings_icon = ctk.CTkImage(
            Image.open(IconManager.get_icon("settings")),
            size=(22,22)
        )

        self.settings_button = ctk.CTkButton(
            self.right_frame,
            text="",
            width=40,
            height=40,
            corner_radius=20,
            fg_color="transparent",
            image=settings_icon,
            command=self.open_settings
        )

        self.settings_button.place(
            relx=0.95,
            rely=0.95,
            anchor="center"
        )

    def open_settings(self):
        """
        Open settings window.
        """

        self.settings_window = SettingsView(
            self.parent
        )

    def login(self):
        """Authenticate user."""

        username = self.username_entry.get().strip()

        password = self.password_entry.get()

        if not username or not password:

            CustomDialog(
                self,
                "Error",
                "Please fill all fields."
            )

            return

        authenticated = AuthService.login(
            username,
            password
        )

        if not authenticated:

            CustomDialog(
                self,
                "Error",
                "Invalid username or password."
            )

            Logger.warning(f"Failed login attempt: {username}")

            return

        if self.remember_checkbox.get():
            SessionManager.save(username)
        else:
            SessionManager.clear()

        Logger.info(f"User '{username}' logged in.")


        self.parent.show_dashboard()