import flet as ft
from core import small_button, long_button


def main(page: ft.Page):

    def action():
        print("Testing")

    # Define the list of robots and assign it to a column control
    widgets = []
    for i in range(30):
        widgets.append(ft.Row([
                ft.ElevatedButton(
                    content=ft.Row([ft.Icon(name=ft.icons.DELETE, size=12)], alignment=ft.MainAxisAlignment.END),
                    width=50,
                    height=50,
                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5)),
                    on_click=lambda: action(),
                ),
            ],))

    bot_library = ft.Column(
        widgets,
        spacing=10,
        height=350,
        width=200,
        scroll=ft.ScrollMode.HIDDEN,
        on_scroll_interval=0
    )

    page.add(bot_library)


if __name__ == '__main__':
    ft.app(target=main)


    """
    ft.ElevatedButton(
                    ' ',
                    width=50,
                    icon=ft.icons.DELETE,
                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5)),
                    on_click=lambda e, index=i: print("Testing"),
                ),

        ft.Container(
                #content=ft.Icon(name=ft.icons.DELETE),
                content=ft.Text(value="Test"),
                ink=True,
                on_click=lambda e: action(),
                width=20,
                height=20,
                border_radius=5,
                bgcolor='#141024',
                border=ft.border.all(0.5, "#848fce"),
        ))
    """