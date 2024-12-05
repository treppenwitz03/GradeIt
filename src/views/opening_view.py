import flet as ft
from widgets import NeuButton

class OpeningView(ft.Container):
    def __init__(self):
        super().__init__()

        image = ft.Image(
            src="neobrutalist.jpg",
            width=250,
            height=250
        )

        label = ft.Text("Calculate your Grades and Know your Rank.", weight=ft.FontWeight.BOLD, size=32, color=ft.Colors.BLACK)

        self.login_button = NeuButton(
            content="Login",
            col="#ecc7d3",
            on_click=self.login
        )
        self.signup_button = NeuButton(
            "Signup",
            "#48aaad",
            on_click=self.signup
        )

        app_icon = ft.Container(
            ft.Image(
                "company.png",
                width=150,
                height=100,
                fit=ft.ImageFit.SCALE_DOWN
            )
        )

        self.content = ft.Column(
            controls=[
                image,
                label,
                self.login_button,
                self.signup_button,
                app_icon
            ],
            horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
            spacing=16
        )
    
    def login(self, event: ft.ControlEvent):
        views: dict = self.page.session.get("views")
        switcher: ft.AnimatedSwitcher = self.parent

        switcher.content = views["login"]
        switcher.update()
    
    def signup(self, event: ft.ControlEvent):
        views: dict = self.page.session.get("views")
        switcher: ft.AnimatedSwitcher = self.parent

        switcher.content = views["signup"]
        switcher.update()