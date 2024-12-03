import flet as ft
import os

import views

class Main(ft.Page):
    def __init__(self, page: ft.Page):
        self = page
        self.bgcolor = "#fffada"
        self.window.title_bar_hidden = False if "ANDROID_BOOTLOGO" in os.environ else True
        self.fonts = {
            "Bahnschrift" : "fonts/Bahnschrift.ttf"
        }

        self.theme = ft.Theme(
            font_family= "Bahnschrift"
        )

        opening_view = views.OpeningView()

        page_switcher = ft.AnimatedSwitcher(
            opening_view,
            duration=250,
            reverse_duration=250
        )

        def minimize():
            self.window.minimized = True
            self.update()
        
        def maximize():
            self.window.maximized = not self.window.maximized
            self.update()

        if not "ANDROID_BOOTLOGO" in os.environ:
            self.add(ft.WindowDragArea(
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
                            on_click=lambda _: self.window.close()
                        )
                    ]
                )
            ))

        self.add(page_switcher)


ft.app(Main, assets_dir="assets", view=ft.AppView.WEB_BROWSER)
