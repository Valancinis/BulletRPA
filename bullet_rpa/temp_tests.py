import flet as ft

def main(page: ft.Page):

    # Function to close the overlay
    def close_overlay(_):
        overlay.visible = False
        page.update()

    # Define the overlay content, initially hidden
    overlay = ft.Container(
        content=ft.Column([
            ft.Text("This is a popup!"),
            ft.ElevatedButton(text="Close", on_click=close_overlay)
        ], alignment=ft.MainAxisAlignment.CENTER),
        width=300,
        height=200,
        bgcolor=ft.colors.WHITE,
        visible=False  # Initially hidden
    )

    # Function to show the overlay
    def show_overlay(_):
        overlay.visible = True
        page.update()

    # Create the main button to open the overlay
    open_button = ft.ElevatedButton(text="Open Popup", on_click=show_overlay)

    # Add the overlay and the main button to the page
    page.add(overlay, open_button)

if __name__ == '__main__':
    ft.app(target=main)
