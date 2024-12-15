import flet as ft
import os

import views
import utils

def main(page: ft.Page):
    page.bgcolor = "#fffada"
    page.window.title_bar_hidden = False if "ANDROID_BOOTLOGO" in os.environ else True
    page.theme_mode = ft.ThemeMode.LIGHT
    page.scroll = ft.ScrollMode.ALWAYS
    page.padding = 0
    page.fonts = {
        "Bahnschrift" : "fonts/Bahnschrift.ttf"
    }

    page.theme = ft.Theme(
        font_family= "Bahnschrift"
    )

    views_dict = dict()
    views_dict["opening"] = views.OpeningView()
    views_dict["login"] = views.LoginView()
    views_dict["signup"] = views.SignupView()
    views_dict["home"] = views.HomeView()
    views_dict["class"] = views.ClassView()
    views_dict["calc"] = views.AdderView()

    page_switcher = ft.AnimatedSwitcher(
        views_dict["opening"],
        duration=200,
        reverse_duration=200,
        transition=ft.AnimatedSwitcherTransition.SCALE
    )
    page.session.set("views", views_dict)

    user_database = utils.UserDatabase()
    page.session.set("user_database", user_database)

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

    page.add(
        ft.SafeArea(
            page_switcher,
            minimum_padding=16
        )
    )


ft.app(main, assets_dir="assets")