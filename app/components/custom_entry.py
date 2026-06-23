import customtkinter as ctk

from app.utils.paths import EYE_CLOSED_ICON, EYE_OPEN_ICON

from PIL import Image


class CustomEntry(ctk.CTkFrame):
    def __init__(
        self,
        parent,
        placeholder="",
        width=320,
        height=45,
        icon_path=None,
        is_password=False,
        *args,
        **kwargs
    ):
        super().__init__(
            parent,
            fg_color="transparent",
            *args,
            **kwargs
        )

        self.is_password = is_password
        self.password_visible = False

        self.grid_columnconfigure(1, weight=1)

        # Ícone esquerdo
        if icon_path:
            self.icon_image = ctk.CTkImage(
                Image.open(icon_path),
                size=(16, 16)
            )

            self.icon_label = ctk.CTkLabel(
                self,
                text="",
                image=self.icon_image,
                width=24
            )

            self.icon_label.grid(
                row=0,
                column=0,
                padx=(0, 2)
            )

        # Campo principal
        self.entry = ctk.CTkEntry(
        self,
        placeholder_text=placeholder,
        width=width,
        height=48,
        corner_radius=24,
        border_width=0,
        fg_color="#3A3A3A",
        show="*" if is_password else ""
)

        self.entry.grid(
            row=0,
            column=1,
            sticky="ew"
        )

        # Botão olho (somente senha)
        if is_password:

            self.eye_open_icon = ctk.CTkImage(
            Image.open(EYE_OPEN_ICON),
            size=(18, 18)
        )

            self.eye_closed_icon = ctk.CTkImage(
            Image.open(EYE_CLOSED_ICON),
            size=(18, 18))

            self.eye_button = ctk.CTkButton(
                self,
                text="",
                image=self.eye_closed_icon,
                width=35,
                height=35,
                fg_color="transparent",
                command=self.toggle_password
            )

            self.eye_button.grid(
                row=0,
                column=2,
                padx=(5, 0)
            )

        else:

            self.empty_label = ctk.CTkLabel(
                self,
                text="",
                width=35
            )

            self.empty_label.grid(
                row=0,
                column=2,
                padx=(5, 0)
            )

    def toggle_password(self):

        self.password_visible = not self.password_visible

        if self.password_visible:

            self.entry.configure(show="")

            self.eye_button.configure(
                image=self.eye_open_icon
            )

        else:

            self.entry.configure(show="*")

            self.eye_button.configure(
                image=self.eye_closed_icon
            )

    
    def get(self):
        """
        Return entry value.
        """

        return self.entry.get()


    def delete(self, start, end):
        """
        Delete entry text.
        """

        self.entry.delete(start, end)


    def insert(self, index, text):
        """
        Insert text.
        """

        self.entry.insert(index, text)