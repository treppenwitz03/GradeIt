import flet as ft
import os

import views

def main(page: ft.Page):
    page.bgcolor = "#fffada"
    page.window.title_bar_hidden = False if "ANDROID_BOOTLOGO" in os.environ else True
    page.fonts = {
        "Bahnschrift" : "fonts/Bahnschrift.ttf"
    }

    page.theme = ft.Theme(
        font_family= "Bahnschrift"
    )

    opening_view = views.OpeningView()

    page_switcher = ft.AnimatedSwitcher(
        opening_view,
        duration=250,
        reverse_duration=250
    )

    def minimize():
        page.window.minimized = True
        page.update()
    
    def maximize():
        page.window.maximized = not page.window.maximized
        page.update()

    if not "ANDROID_BOOTLOGO" in os.environ:
        page.add(ft.WindowDragArea(
            ft.Row(
                alignment=ft.MainAxisAlignment.END,
                controls=[
                    ft.IconButton(
                        ft.CupertinoIcons.MINUS,
                        icon_color=ft.Colors.BLACK,
                        icon_size=24,
                        width = 32,
                        height = 32,
                        on_click=lambda _: minimize()
                    ),
                    ft.IconButton(
                        ft.CupertinoIcons.SQUARE,
                        icon_color=ft.Colors.BLACK,
                        icon_size=24,
                        width = 32,
                        height = 32,
                        on_click=lambda _: maximize()
                    ),
                    ft.IconButton(
                        ft.CupertinoIcons.XMARK,
                        icon_color=ft.Colors.BLACK,
                        icon_size=24,
                        width = 32,
                        height = 32,
                        on_click=lambda _: page.window.close()
                    )
                ]
            )
        ))

    page.add(page_switcher)


ft.app(main, assets_dir="assets")