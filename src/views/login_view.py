import flet as ft
from widgets import NeuButton, NeuTextField

from utils import UserDatabase

class LoginView(ft.Container):
    def __init__(self):
        super().__init__()
        self.padding = 16

        signin_text = ft.Container(
            ft.Text(
                "SIGN IN",
                weight=ft.FontWeight.BOLD,
                color=ft.Colors.BLACK,
                text_align=ft.TextAlign.CENTER,
                size=24,
                spans=[ft.TextSpan("\nWelcome back, you've been missed!", style=ft.TextStyle(size=16))]
            ),
            margin=ft.margin.symmetric(48, 0)
        )

        self.email_tf = NeuTextField("Enter your Username", False, on_change=self.on_change)

        self.password_tf = NeuTextField("Enter your Password", True, on_change=self.on_change)

        self.forgot_password = ft.TextButton("Forgot Password?", style=ft.ButtonStyle(color=ft.Colors.BLACK, text_style=ft.TextStyle(weight=ft.FontWeight.BOLD)))

        self.proceed_button = NeuButton("Sign In", "#fa8128", on_click=self.login, disabled=True)

        self.register_text = ft.Text(
            spans=[
                ft.TextSpan(
                    "Register Now",
                    style=ft.TextStyle(
                        color=ft.Colors.BLUE,
                        weight=ft.FontWeight.BOLD,
                        decoration=ft.TextDecoration.UNDERLINE
                    )
                )
            ]
        )
        
        self.content = ft.Column(
            controls=[
                signin_text,
                self.email_tf,
                self.password_tf,
                ft.Row([self.forgot_password], alignment=ft.MainAxisAlignment.END),
                self.proceed_button,
                ft.Container(ft.Row([
                    ft.Text("Haven't Registered Yet?", weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK),
                    ft.GestureDetector(self.register_text, on_enter=self.register_hovered, on_exit=self.register_hovered, on_tap=self.to_signup)
                ], alignment=ft.MainAxisAlignment.CENTER), margin=ft.margin.only(0, 32, 0, 0))
            ],
            spacing=16,
            horizontal_alignment=ft.CrossAxisAlignment.STRETCH
        )
    
    def on_change(self, event):
        if all([self.email_tf.value, self.password_tf.value]):
            self.proceed_button.disabled = False
        else:
            self.proceed_button.disabled = True
        self.proceed_button.update()

    def register_hovered(self, event: ft.HoverEvent):
        self.register_text.spans[0].style.color = ft.Colors.PINK if "enter" in event.name else ft.Colors.BLUE
        self.page.update()
    
    def to_signup(self, event):
        views: dict = self.page.session.get("views")
        switcher: ft.AnimatedSwitcher = self.parent

        switcher.content = views["signup"]
        switcher.update()
    
    def login(self, event):
        user_database: UserDatabase = self.page.session.get("user_database")
        success = user_database.existing(self.email_tf.value, self.password_tf.value)

        if success == "PW wrong":
            self.notify("Password is wrong...")
        elif success:
            self.notify("Login successful! Welcome back!")
            self.page.session.set("user", self.email_tf.value)
            views: dict = self.page.session.get("views")
            switcher: ft.AnimatedSwitcher = self.parent

            switcher.content = views["home"]
            switcher.update()

            switcher.content.set_name(self.email_tf.value)
        else:
            self.notify("Login failed: Invalid username or password.")

    def notify(self, message: str):
        self.page.snack_bar = ft.SnackBar(ft.Text(message), duration=1000)
        self.page.snack_bar.open = True
        self.page.update()