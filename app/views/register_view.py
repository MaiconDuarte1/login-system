import customtkinter as ctk

from PIL import Image

from app.components.custom_entry import CustomEntry
from app.core.theme_manager import ThemeManager
from app.models.user_model import User
from app.services.auth_service import AuthService
from app.components.custom_dialog import CustomDialog
from app.utils.logger import Logger
from app.utils.validators import Validators

from app.utils.paths import (
    LOGIN_BANNER,
    USER_ICON,
    EMAIL_ICON,
    LOCK_ICON
)

from app.core.icon_manager import IconManager


class RegisterView(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent

        self._create_layout()

    def _create_layout(self):

        self.pack(
            fill="both",
            expand=True
        )

        self._create_frames()
        self._create_banner()
        self._create_form()

    def _create_frames(self):

        self.left_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        self.left_frame.pack(
            side="left",
            fill="both",
            expand=True
        )

        self.right_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        self.right_frame.pack(
            side="right",
            fill="both",
            expand=True
        )

    def _create_banner(self):

        self.banner_image = ctk.CTkImage(
            Image.open(LOGIN_BANNER),
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

    def _create_form(self):

        self.content_frame = ctk.CTkFrame(
            self.right_frame,
            fg_color="transparent"
        )

        self.content_frame.pack(
            expand=True,
            pady=(0, 60)
        )

        self._create_header()

        self._create_entries()

        self._create_buttons()




    def _create_header(self):

        self.title_label = ctk.CTkLabel(
            self.content_frame,
            text="Create Account",
            font=("Segoe UI", 28, "bold")
        )

        self.title_label.pack(
            pady=(0, 10)
        )

        self.subtitle_label = ctk.CTkLabel(
            self.content_frame,
            text="Create your account"
        )

        self.subtitle_label.pack(
            pady=(0, 40)
        )

    def _create_entries(self):
        """Create all input fields required for user authentication."""

        self.username_entry = CustomEntry(
            self.content_frame,
            placeholder="Username",
            icon_path=IconManager.get_icon("user")
        )

        self.username_entry.pack(
            pady=8
        )

        self.email_entry = CustomEntry(
            self.content_frame,
            placeholder="Email",
            icon_path=IconManager.get_icon("email")
        )

        self.email_entry.pack(
            pady=8
        )

        self.password_entry = CustomEntry(
            self.content_frame,
            placeholder="Password",
            icon_path=IconManager.get_icon("lock"),
            is_password=True
        )

        self.password_entry.pack(
            pady=8
        )

        self.confirm_password_entry = CustomEntry(
            self.content_frame,
            placeholder="Confirm Password",
            icon_path=IconManager.get_icon("lock"),
            is_password=True
        )

        self.confirm_password_entry.pack(
            pady=8
        )

    def _create_buttons(self):

        self.register_button = ctk.CTkButton(
            self.content_frame,
            text="Register",
            width=400,
            height=50,
            corner_radius=25,
            fg_color="#8B5CF6",
            hover_color="#7C3AED",
            command=self.create_account
        )

        self.register_button.pack(
            pady=(25, 20)
        )

        border_color = (
            "#FFFFFF" if ThemeManager.is_dark()
            else "#222222"
        )

        text_color = (
            "#FFFFFF" if ThemeManager.is_dark()
            else "#222222"
        )

        self.back_button = ctk.CTkButton(
            self.content_frame,
            text="Back to Login",
            width=400,
            height=50,
            corner_radius=25,
            fg_color="transparent",
            border_color=border_color,
            text_color=text_color,
            border_width=1,
            command=self.back_to_login
        )

        self.back_button.pack()


    def create_account(self):
        """
        Create a new account.
        """

        username = self.username_entry.get().strip()

        email = self.email_entry.get().strip()

        password = self.password_entry.get()

        confirm_password = (
            self.confirm_password_entry.get()
        )

        #VALIDATORS // --------------------------------------------------------

        if not username or not email or not password:

            CustomDialog(
                self,
                "Error",
                "Please fill all fields."
            )

            Logger.warning(f"Failed register attempt: {username}")

            return

        if password != confirm_password:

            CustomDialog(
                self,
                "Error",
                "Passwords do not match."
            )

            Logger.warning(f"Failed register attempt: {username}")

            return
        

        if not Validators.validate_username(username):
            CustomDialog(
                self,
                "Invalid Username",
                "Username must contain at least 3 characters."
            )

            return
        
        if not Validators.validate_email(email):
            CustomDialog(
                self,
                "Invalid Email",
                "Please enter a valid email."
            )

            return


        if not Validators.validate_password(password):
            CustomDialog(
                self,
                "Weak Password",
                "Password must contain: \n\n"
                "• At least 8 characters\n"
                "• One uppercase letter\n"
                "• One number"
            )

            return
        
        #VALIDATORS // -------------------------------------------------------- ^^^^^^
        
        encrypted_password = (AuthService.hash_password(password))

        user = User(
            username,
            email,
            encrypted_password
        )

        success = AuthService.register(user)

        if not success:
            CustomDialog(
                self,
                "Error",
                "User or email already exists."
            )
            return
        


        CustomDialog(
            self,
            "Success",
            "Account created successfully.",
            callback=self.parent.show_login
        )

        Logger.info(f"User '{username}' registered.")


    def back_to_login(self):
        self.parent.show_login()