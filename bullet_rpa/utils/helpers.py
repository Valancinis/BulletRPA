import flet as ft


# Defining a function that picks a file and updates the text field
def pick_files_result(e: ft.FilePickerResultEvent, selected_files):
    selected_files.value = e.files[0].path if e.files else ""
    selected_files.update()

