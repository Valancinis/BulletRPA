import json
import flet as ft


def load_data(file_path):
    with open(file_path, 'r') as file:
        # Check if the file is empty
        content = file.read()
        # Check if the content is empty
        if not content:
            return []
        data = json.loads(content)
    return data


def store_data(bot_list, file_path):
    with open(file_path, 'w') as f:
        json.dump(bot_list, f)


class LongButton(ft.UserControl):
    def __init__(self, btn_name, action):
        super().__init__()
        self.name = btn_name
        self.action = action

    def build(self):
        wide_button = ft.Stack(
            [ft.Container(bgcolor='#ff0000', expand=True, width=300, height=100),
                ft.Text(value=self.name, size=20),
             ],
            expand=True,
        )
        gesture_detector = ft.GestureDetector(on_tap=self.action, content=wide_button)

        return gesture_detector
