import flet as ft
import bullet_rpa.core.workers as workers


def main(page: ft.Page):
    file_path = 'data/robots.json'
    bot_list = []
    bot_list = workers.load_data(file_path)

    # Defining a file picker function
    def pick_files_result(e: ft.FilePickerResultEvent):
        selected_files.value = (
            ", ".join(map(lambda f: f.path, e.files)) if e.files else "Cancelled!"
        )
        selected_files.update()

    def add_robot(e):
        bot = {
            "name": input_name.value,
            "path": selected_files.value
        }
        bot_list.append(bot)
        workers.store_data(bot_list, file_path)
        input_name.value = ""
        selected_files.value = ""
        widgets = [ft.ElevatedButton(bot["name"], style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5))) for bot in bot_list]
        bot_library.controls = widgets
        page.update(input_name, selected_files, bot_library)

    header = ft.Text(value="BULLET", color="green")
    input_name = ft.TextField(label="RPA name", color="green", autofocus=True)
    page.add(header, input_name)

    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
    selected_files = ft.TextField(label="File path", expand=True)

    page.overlay.append(pick_files_dialog)

    page.add(
        ft.Row(
            [
                ft.ElevatedButton(
                    "Pick files",
                    icon=ft.icons.UPLOAD_FILE,
                    on_click=lambda _: pick_files_dialog.pick_files(
                        allow_multiple=True
                    ),
                ),
                selected_files,
            ]
        )
    )

    add_button = ft.ElevatedButton(
        "Add", icon=ft.icons.ADD, on_click=add_robot
    )
    page.add(add_button)

    page.add(ft.Divider())

    widgets = [ft.ElevatedButton(bot["name"], style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5))) for bot in bot_list]
    bot_library = ft.Column(widgets)
    page.add(bot_library)

ft.app(target=main)
