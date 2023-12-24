import flet as ft


class SmallButton(ft.UserControl):
    def __init__(self, icon, action, size=10):
        super().__init__()

        # Assigning user inputs
        self.icon = icon
        self.action = action
        self.size = size

        # Defining variable icon name input
        custom_name = f"ft.icons.{self.icon}"

        # Creating a small button
        self.small_button = ft.Container(
            content=ft.Icon(name=custom_name, size=self.size),
            ink=True,
            on_click=lambda e: self.action,
            width=20,
            height=20,
            border_radius=5,
            bgcolor='#141024',
            border=ft.border.all(0.5, "#848fce"),
    )

    def build(self):
        return ft.Stack([self.small_button], expand=True)
