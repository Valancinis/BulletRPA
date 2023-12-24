import flet as ft


def main(page: ft.Page):
    small_button = ft.Container(
        content=ft.Icon(name=ft.icons.ACCESSIBLE_SHARP, size=10),
        ink=True,
        on_click=lambda e: print('Clicked'),
        width=20,
        height=20,
        border_radius=5,
        bgcolor='#141024',
        border=ft.border.all(0.5, "#ffffff"),
    )
    page.add(small_button)


if __name__ == '__main__':
    ft.app(target=main)