import flet as ft


class LongButton(ft.UserControl):
    def __init__(self, btn_name):
        # Initialising the class, assigning arguments to variables
        super().__init__()
        self.name = btn_name

        # Creating a container for background color and functionality
        self.container = ft.Container(
            content=ft.Text(value=self.name, size=20),
            bgcolor='#ff0000',
            expand=True,
            width=300,
            height=100,
            ink=True,
        )

    # Defining a build function to push any controls from a class instance
    def build(self):
        return ft.Stack([self.container], expand=True)