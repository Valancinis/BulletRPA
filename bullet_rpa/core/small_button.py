import flet as ft

# NOT USED ANYMORE, A BUILT-IN CONTROL WAS USED
class SmallButton(ft.UserControl):
    def __init__(self, icon, action, size=10):
        super().__init__()

        # Assigning user inputs
        self.icon = icon
        self.action = action
        self.size = size

        # Defining variable icon name input
        custom_icon = getattr(ft.icons, self.icon, None)

        # Creating a small button
        self.small_button = ft.Container(
            content=ft.Icon(name=custom_icon, size=self.size),
            ink=True,
            width=20,
            height=20,
            border_radius=5,
            bgcolor='#141024',
            border=ft.border.all(0.5, "#848fce"),

        )
        self.small_button.on_click = action

    def build(self):
        return ft.Stack([self.small_button], expand=True)
