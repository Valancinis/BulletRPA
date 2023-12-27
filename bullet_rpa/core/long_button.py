import flet as ft
import subprocess

# NO LONGER NEEDED AS LAMBDA FUNCTIONALITY DOES NOT WORK WITH SCROLLING FUNCTIONALITY IN COLUMNS
class LongButton(ft.UserControl):
    def __init__(self, bot_dict):
        # Initialising the class, assigning arguments to variables
        super().__init__()
        self.name = bot_dict['name']
        self.path = bot_dict['path']

        # Creating a container for background color and functionality
        self.container = ft.Container(
            content=ft.Text(value=self.name, size=12),
            bgcolor='#141024',
            width=float('inf'),
            height=50,
            ink=True,
            # Add on click, so that ink would work and container would become a button.
            padding=16,
            on_click=lambda e: self.launch_software(e),
        )

    def launch_software(self, _):
        subprocess.Popen(['open', self.path])

    # Defining a build function to push any controls from a class instance
    def build(self):
        return ft.Stack([self.container], expand=True)
