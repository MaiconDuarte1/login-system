import customtkinter as ctk

from app.utils.paths import APP_ICON


class CustomDialog(ctk.CTkToplevel):
    """
    Custom application dialog.
    """

    def __init__(
        self,
        parent,
        title: str,
        message: str,
        callback=None
    ):
        super().__init__(parent)

        self.callback = callback

        self.title(title)

        self.geometry("350x180")

        self.resizable(False, False)

        self.grab_set()

        self.transient(parent)

        self.after(
            100,
            lambda: self.iconbitmap(str(APP_ICON))
        )

        message_label = ctk.CTkLabel(
            self,
            text=message,
            wraplength=280,
            justify="center",
            font=("Segoe UI", 14)
        )

        message_label.pack(
            expand=True,
            padx=20,
            pady=(30, 10)
        )

        ok_button = ctk.CTkButton(
            self,
            text="OK",
            command=self.close_dialog,
            width=120
        )

        ok_button.pack(
            pady=(0, 20)
        )


    def close_dialog(self):
        """close dialog."""


        self.destroy()

        if self.callback:
            self.callback()