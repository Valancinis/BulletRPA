import flet as ft
import bullet_rpa.core.workers as workers
def main(page: ft.Page):

    bot_list = []
    bot_list = workers.load_data() or []

    def pick_files_result(e: ft.FilePickerResultEvent):
        selected_files.value = (
            ", ".join(map(lambda f: f.name, e.files)) if e.files else "Cancelled!"
        )
        selected_files.update()

    def add_robot(e):
        bot = {
            "name" : inputName.value,
            "files" : selected_files.value
        }
        bot_list.append(bot)
        workers.store_data(bot_list)

    header = ft.Text(value="BULLET", color="green")
    inputName = ft.TextField(label="RPA name", color="green", autofocus=True)
    page.add(header, inputName)

    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
    selected_files = ft.Text()

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

ft.app(target=main)
