from core import workers
from utils import helpers

import flet as ft
import subprocess
import threading
import time

current_bot_name = ""


def main(page: ft.Page):

    # Load the list of robots
    file_path = 'data/robots.json'
    bot_list = []
    bot_list = workers.load_data(file_path)

    # Define page appearance
    page.title = "BULLET RPA"
    page.window_width = 200
    page.window_height = 580
    page.window_resizable = False
    page.bgcolor = "#131517"
    page.theme = ft.Theme(
        scrollbar_theme=ft.ScrollbarTheme(
            thickness=2,
            cross_axis_margin=-4,
        )
    )

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
                    on_click=lambda e: open_popup(bot_item['name'], e),
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
                "path": selected_files.value,
                "schedule": None
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
        subprocess.Popen(['open', path], close_fds=True)

    # Define a lock for thread-safe operations on bot_list
    bot_list_lock = threading.Lock()

    def schedule_bots(bot_list):
        last_run_times = {}

        while True:
            with bot_list_lock:  # Acquire lock before accessing bot_list
                current_time = time.time()

                for bot in bot_list:
                    # Initialize last run time for new bots
                    if bot['name'] not in last_run_times:
                        last_run_times[bot['name']] = None

                    schedule_str = bot.get('schedule')
                    if not schedule_str:
                        continue  # Skip bots without a valid schedule

                    try:
                        schedule = float(schedule_str)
                        if schedule <= 0:
                            continue
                    except ValueError:
                        continue  # Skip if schedule is not a valid number

                    schedule_time = schedule * 3600  # Convert hours to seconds

                    if last_run_times[bot['name']] is None:
                        # First run, set the last run time to current time
                        last_run_times[bot['name']] = current_time
                    else:
                        next_run_time = last_run_times[bot['name']] + schedule_time
                        if current_time >= next_run_time:
                            launch_software(bot['path'])
                            last_run_times[bot['name']] = current_time  # Update last run time

            # Check every 15 minutes if bots need to run
            check_interval = 15
            time.sleep(60 * check_interval)

    # Function to close the popup
    def close_popup(_):
        popup_container.visible = False
        container_dimmer.visible = False
        page.update()

    # Function to open the scheduling popup
    def open_popup(bot_name, _):
        global current_bot_name
        current_bot_name = bot_name
        popup_title.value = f"Schedule for {bot_name}"
        current_bot = next((each_bot for each_bot in bot_list if each_bot["name"] == bot_name), None)
        if current_bot is not None:
            # Convert None to an empty string
            schedule_value = "" if current_bot.get("schedule") is None else str(current_bot["schedule"])
            bot_schedule.value = schedule_value
        popup_container.visible = True
        container_dimmer.visible = True
        page.update()

    # Function to set the schedule for a bot
    def set_schedule(_):
        try:
            global current_bot_name
            current_bot = next((bot for bot in bot_list if bot["name"] == current_bot_name), None)
            if current_bot is not None:
                if bot_schedule.value:
                    try:
                        # Convert to float then back to string to clean the input
                        schedule_value = float(bot_schedule.value)
                        # Format string to remove trailing zeros and prevent scientific notation
                        current_bot["schedule"] = ('{:.5f}'.format(schedule_value)).rstrip('0').rstrip('.')
                    except ValueError:
                        # Handle invalid float input here (e.g., log or display an error)
                        pass
                else:
                    current_bot["schedule"] = "0"  # Default value if empty

                workers.store_data(bot_list, file_path)
            else:
                # Handle the case where the bot is not found
                pass
            close_popup(None)
        except Exception as e:
            # Handle exceptions silently, could add log here
            pass

    # Running a thread to schedule bots
    thread = threading.Thread(target=schedule_bots, args=(bot_list,))
    thread.daemon = True  # This makes the thread exit when the main program exits
    thread.start()

    # Popup container for scheduling
    popup_title = ft.Text("", size=12, color="#ffffff")  # White text color
    bot_schedule = ft.TextField(
        label="Interval (hours)",
        label_style=ft.TextStyle(color="#ffffff", size=12)  # White label text
    )
    set_button = ft.ElevatedButton(
        content=ft.Text(value="Set", size=12),
        on_click=set_schedule,
        style=ft.ButtonStyle(bgcolor="#fd6161", color="#ffffff", padding=2),
        width=60,
        height=30,

    )
    close_button = ft.ElevatedButton(
        content=ft.Text(value="Cancel", size=12),
        on_click=close_popup,
        style=ft.ButtonStyle(bgcolor="#889be6", color="#ffffff", padding=2),
        width=80,
        height=30,
    )

    # Popup content definition
    popup_content = ft.Container(
        content=ft.Column([
            popup_title,
            bot_schedule,
            ft.Row([set_button, close_button], alignment=ft.MainAxisAlignment.CENTER, spacing=10)
        ]),
        width=180,
        padding=ft.padding.only(top=3, right=10, left=10, bottom=10),
        bgcolor="#2c2833",  # A contrasting background color for the popup
        border_radius=10
    )

    # Wrapping the popup content for alignment purposes
    popup_container = ft.Column(
        [popup_content],
        expand=True,  # Expand to fill the available space
        alignment=ft.alignment.center,
        visible=False,
        top=180,
    )

    # Dimmer to cover the background when the popup is open
    container_dimmer = ft.Container(
        width=500,
        height=600,
        expand=True,
        bgcolor="#000000",
        opacity=0.5,
        visible=False,
        left=0,
        bottom=0,
    )

    input_name = ft.TextField(
        label="RPA name",
        color="#ffffff",
        height=35,
        text_size=14,
        label_style=ft.TextStyle(color="#ffffff", size=14),
        border_color="#889be6",
        focused_border_color="#fd6161",
        content_padding=ft.padding.only(left=10, right=5),
    )

    # Define file picker and its functionality
    pick_files_dialog = ft.FilePicker(
        on_result=lambda e: helpers.pick_files_result(e, selected_files))

    selected_files = ft.TextField(
        label="File path",
        height=30,
        width=140,
        text_size=13,
        label_style=ft.TextStyle(color="#ffffff", size=14),
        color="#ffffff",
        border_color="#889be6",
        focused_border_color="#fd6161",
        content_padding=ft.padding.only(left=10, right=5),
    )

    picker_button = ft.ElevatedButton(
        content=ft.Row([
            ft.Icon(name=ft.icons.UPLOAD_FILE, size=20, color="#ffffff"),  # White icon color for visibility
        ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        style=ft.ButtonStyle(
            bgcolor="#1c1f24",  # Slightly lighter shade than the background for subtlety
            elevation=2,  # Small elevation to give depth
            shape=ft.RoundedRectangleBorder(radius=20),  # Rounded corners for style
            padding=5
        ),
        width=30,
        height=30,
        on_click=lambda _: pick_files_dialog.pick_files(
            allow_multiple=False,
        )
    )

    # Define the row that contains the file picker and the selected file text field
    file_pick_row = ft.Row([
        selected_files,
        picker_button,
        pick_files_dialog,
        ],
        spacing=6,
    )

    # Define the button that adds the robot to the list
    add_button = ft.Row([
        ft.ElevatedButton(
            "Add", icon=ft.icons.ADD,
            on_click=add_robot,
            style=ft.ButtonStyle(
                bgcolor="#fd6161",
                color="#ffffff",
                shape=ft.RoundedRectangleBorder(radius=15),
            ),
            width=float('inf'),
            expand=True,
            height=30,
        )],
        alignment=ft.MainAxisAlignment.START,
    )

    # Define the list of robots and assign it to a column control
    widgets = []
    for i, bot in enumerate(bot_list):
        widgets.append(create_bot_button(bot, i))

    bot_library = ft.Column(widgets, spacing=10, height=380, width=200, scroll=ft.ScrollMode.HIDDEN)

    # Main content of the page
    main_content = ft.Column([
        input_name,
        file_pick_row,
        add_button,
        ft.Divider(),
        bot_library,
    ])

    overlay = ft.Stack([
        main_content,
        container_dimmer,
        popup_container
    ])

    # Add controls to the page
    page.add(overlay)


if __name__ == '__main__':
    ft.app(target=main)
