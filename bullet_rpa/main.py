from core import workers
from utils import helpers
import subprocess

import flet as ft


def main(page: ft.Page):

    # Handles button creation on the main page
    def create_bot_button(bot_item, index):
        bot_path = bot_item['path']
        return ft.Stack([
            ft.ElevatedButton(
                content=ft.Row([
                    ft.Text(bot_item['name'],
                            color="#ffffff",
                            ),
                ], alignment=ft.MainAxisAlignment.START),
                width=float('inf'),
                height=50,
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=5),
                    padding=8,
                    bgcolor="#131517",
                    color="#ffffff",
                ),
                on_click=lambda e, bots_path=bot_path: launch_software(bots_path),
            ),
            ft.Column([
                ft.ElevatedButton(
                    content=ft.Icon(name=ft.icons.DELETE, size=12, color="#ffffff"),
                    width=20,
                    height=20,
                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5), padding=0),
                    on_click=lambda e, idx=index: remove_robot(idx),
                    bgcolor="#2c2833",
                ),
                ft.ElevatedButton(
                    content=ft.Icon(name=ft.icons.MORE_TIME, size=12, color="#ffffff"),
                    width=20,
                    height=20,
                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5), padding=0),
                    on_click=open_popup,
                    bgcolor="#2c2833",
                ),
            ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=3.5,
                top=3.5,
                right=5,
            ),
        ])

    # Defining a function that adds a robot to the list
    def add_robot(_):
        # Check and store the robot name and path
        if input_name.value == "" or selected_files.value == "":
            return
        else:
            bot_name = {
                "name": input_name.value,
                "path": selected_files.value
            }
            bot_list.append(bot_name)
            workers.store_data(bot_list, file_path)

            # Update the list of robots to blank values
            input_name.value = ""
            selected_files.value = ""

            # Update bot button list
            update_bot_list()

    # Defining a function that removes robots from the list
    def remove_robot(bot_index):
        del bot_list[bot_index]
        update_bot_list()
        workers.store_data(bot_list, file_path)

    # Define function to update the bot list
    def update_bot_list():
        bot_widgets = [create_bot_button(bot_item, index) for index, bot_item in enumerate(bot_list)]
        bot_library.controls = bot_widgets
        page.update()

    def launch_software(path):
        subprocess.Popen(['open', path])

    def close_popup(_):
        popup_container.visible = False
        page.update()

    def open_popup(_):
        popup_container.visible = True
        page.update()

    # Popup container for scheduling
    popup_container = ft.Container(
        content=ft.Column([
            ft.Text("Set Schedule"),
            ft.TextField(label="Interval (hours)"),
            ft.ElevatedButton(text="Set", on_click=close_popup),
            ft.ElevatedButton(text="Cancel", on_click=close_popup)
        ]),
        width=200,
        height=150,
        bgcolor=ft.colors.WHITE,
        visible=False,  # Initially hidden
        border_radius=10
    )

    page.add(popup_container)

    # Define page appearance
    page.title = "BULLET RPA"
    page.window_width = 200
    page.window_resizable = False
    page.bgcolor = "#131517"

    # Load the list of robots
    file_path = 'data/robots.json'
    bot_list = []
    bot_list = workers.load_data(file_path)

    input_name = ft.TextField(
        label="RPA name",
        color="#ffffff",
        autofocus=True,
        height=50,
        text_size=15,
        label_style=ft.TextStyle(color="#ffffff", size=15),
        border_color="#889be6",
        focused_border_color="#fd6161",
    )

    # Define file picker and its functionality
    pick_files_dialog = ft.FilePicker(
        on_result=lambda e: helpers.pick_files_result(e, selected_files))

    selected_files = ft.TextField(
        label="File path",
        height=35,
        width=140,
        text_size=10,
        label_style=ft.TextStyle(color="#ffffff", size=14),
        border_color="#889be6",
        focused_border_color="#fd6161",
    )

    picker_button = ft.ElevatedButton(
        content=ft.Row([
            ft.Icon(name=ft.icons.UPLOAD_FILE, size=18, color="#ffffff"),  # White icon color for visibility
        ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        style=ft.ButtonStyle(
            bgcolor="#1c1f24",  # Slightly lighter shade than the background for subtlety
            elevation=2,  # Small elevation to give depth
            shape=ft.RoundedRectangleBorder(radius=15),  # Rounded corners for style
            padding=6
        ),
        width=30,  # Adjust the width if necessary
        on_click=lambda _: pick_files_dialog.pick_files(
            allow_multiple=False,
        )
    )

    # Define the row that contains the file picker and the selected file text field
    file_pick_row = ft.Row([
        selected_files,
        picker_button,
        pick_files_dialog,
        ]
    )

    # Define the button that adds the robot to the list
    add_button = ft.Row([
        ft.ElevatedButton(
            "Add", icon=ft.icons.ADD,
            on_click=add_robot,
            style=ft.ButtonStyle(
                bgcolor="#fd6161",
                color="#ffffff",
            ),
        )],
        alignment=ft.MainAxisAlignment.CENTER,
    )

    # Define the list of robots and assign it to a column control
    widgets = []
    for i, bot in enumerate(bot_list):
        widgets.append(create_bot_button(bot, i))

    bot_library = ft.Column(widgets, spacing=10, height=408, width=200, scroll=ft.ScrollMode.HIDDEN)

    # Add controls to the page
    page.add(input_name, file_pick_row, add_button, ft.Divider(), bot_library,)


if __name__ == '__main__':
    ft.app(target=main)
