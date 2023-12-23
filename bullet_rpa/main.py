from core import workers as workers, long_button

import flet as ft


def main(page: ft.Page):
    # Defining a function that picks a file and updates the text field
    def pick_files_result(e: ft.FilePickerResultEvent):
        selected_files.value = (
            ", ".join(map(lambda f: f.path, e.files)) if e.files else ""
        )
        selected_files.update()

    # Define function to update the bot list
    def update_bot_list():
        bot_widgets = []
        for i, bot in enumerate(bot_list):
            bot_widgets.append(ft.Stack([
                long_button.LongButton(bot['name']),
                ft.Row([
                    ft.ElevatedButton(
                        ' ',
                        width=50,
                        icon=ft.icons.DELETE,
                        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5)),
                        on_click=lambda e, index=i: remove_robot(index),
                    ),
                ],
                    bottom=10,
                    right=10,
                ),
            ]))
        bot_library.controls = bot_widgets
        page.update()

    # Defining a function that adds a robot to the list
    def add_robot(e):
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

    # TODO: Function that runs the robot

    # Define page appearance
    page.window_width = 200
    page.window_resizable = False

    # Load the list of robots
    file_path = 'data/robots.json'
    bot_list = []
    bot_list = workers.load_data(file_path)

    # Defining the initial page layout
    header = ft.Text(value="BULLET", color="green", size=25)

    input_name = ft.TextField(
        label="RPA name",
        color="green",
        autofocus=True,
        height=50,
        text_size=15,
        label_style=ft.TextStyle(size=15),
    )

    # Define file picker and its functionality
    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
    selected_files = ft.TextField(
        label="File path",
        height=45,
        width=120,
        text_size=8,
        label_style=ft.TextStyle(size=14),
    )

    picker_button = ft.ElevatedButton(
        text=" ",
        icon=ft.icons.UPLOAD_FILE,
        width=45,
        on_click=lambda _: pick_files_dialog.pick_files(
            allow_multiple=False
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
            "Add", icon=ft.icons.ADD, on_click=add_robot
        )],
        alignment=ft.MainAxisAlignment.CENTER,
    )

    # Define the list of robots and assign it to a column control
    widgets = []
    for i, bot in enumerate(bot_list):
        widgets.append(ft.Stack([
                long_button.LongButton(bot['name']),
                ft.Row([
                    ft.ElevatedButton(
                        ' ',
                        width=50,
                        icon=ft.icons.DELETE,
                        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5)),
                        on_click=lambda e, index=i: remove_robot(index),),
                    ],
                    bottom=10,
                    right=10,
                )],


        ))

    bot_library = ft.Column(
        widgets,
        spacing=10,
        height=float('inf'),
        width=200,
        scroll=ft.ScrollMode.ALWAYS,
        on_scroll_interval=0
    )

    # Add controls to the page
    page.add(header, input_name, file_pick_row, add_button, ft.Divider(), bot_library,)


if __name__ == '__main__':
    ft.app(target=main)
