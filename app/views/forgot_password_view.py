import customtkinter as ctk

from app.config.settings import settings


class ForgotPasswordView(ctk.CTkFrame):
    """
    Password recovery screen.
    """

    def __init__(self, parent):

        super().__init__(parent)

        self.parent = parent

        self.pack(
            fill="both",
            expand=True
        )

        self._create_widgets()

    def _create_widgets(self):
        """
        Create widgets.
        """

        title = ctk.CTkLabel(
            self,
            text="Forgot Password",
            font=("Segoe UI", 32, "bold")
        )

        title.pack(
            pady=(80, 10)
        )

        subtitle = ctk.CTkLabel(
            self,
            text="Enter your email to recover your account.",
            text_color="gray"
        )

        subtitle.pack(
            pady=(0, 40)
        )

        self.email_entry = ctk.CTkEntry(
            self,
            width=350,
            height=45,
            placeholder_text="Email"
        )

        self.email_entry.pack(
            pady=10
        )

        send_button = ctk.CTkButton(
            self,
            text="Send Recovery Link",
            width=350,
            height=45,
            command=self.send_recovery
        )

        send_button.pack(
            pady=(20, 10)
        )

        back_button = ctk.CTkButton(
            self,
            text="Back to Login",
            width=350,
            height=45,
            fg_color="transparent",
            border_width=1,
            command=self.back_to_login
        )

        back_button.pack(
            pady=10
        )

    def send_recovery(self):
        """
        Placeholder for recovery integration.
        """

        print(
            "Recovery integration goes here."
        )

    def back_to_login(self):
        """
        Return to login screen.
        """

        self.parent.show_login()