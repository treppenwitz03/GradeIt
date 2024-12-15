import flet as ft
from widgets import NeuButton, NeuTextField
from utils import UserDatabase

class SignupView(ft.Container):
    def __init__(self):
        super().__init__()
        self.padding = 16

        signin_text = ft.Container(
            ft.Text(
                "SIGN UP",
                weight=ft.FontWeight.BOLD,
                color=ft.Colors.BLACK,
                text_align=ft.TextAlign.CENTER,
                size=24,
                spans=[ft.TextSpan("\nWelcome! Let's get you settled.", style=ft.TextStyle(size=16))]
            ),
            margin=ft.margin.symmetric(48, 0)
        )

        self.uname_tf = NeuTextField("Username", False, on_change=self.on_change)
        self.email_tf = NeuTextField("Enter your Email", False, on_change=self.on_change)
        self.password_tf = NeuTextField("Enter your Password", True, on_change=self.on_change)
        self.confirm_password_tf = NeuTextField("Confirm your Password", True, on_change=self.on_change)

        self.agree_eula = ft.Checkbox("I agree to the Terms and Conditions", check_color=ft.Colors.BLACK, label_style=ft.TextStyle(color=ft.Colors.BLACK, weight=ft.FontWeight.BOLD))

        self.proceed_button = NeuButton("Sign Up", "#fa8128", disabled=True, on_click=self.register)

        self.register_text = ft.Text(
            spans=[
                ft.TextSpan(
                    "Sign In",
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
                self.uname_tf,
                self.email_tf,
                self.password_tf,
                self.confirm_password_tf,
                ft.Row([self.agree_eula], alignment=ft.MainAxisAlignment.START),
                self.proceed_button,
                ft.Container(ft.Row([
                    ft.Text("Already have an account?", weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK),
                    ft.GestureDetector(self.register_text, on_enter=self.register_hovered, on_exit=self.register_hovered, on_tap=self.to_login)
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
    
    def to_login(self, event):
        views: dict = self.page.session.get("views")
        switcher: ft.AnimatedSwitcher = self.parent

        switcher.content = views["login"]
        switcher.update()
    
    def register(self, event: ft.ControlEvent):
        if self.password_tf.value != self.confirm_password_tf.value:
            self.notify("Passwords don't match")
            return

        user = {
            self.uname_tf.value : {
                "email" : self.email_tf.value,
                "password" : self.password_tf.value
            }
        }

        user_database: UserDatabase = self.page.session.get("user_database")
        success = user_database.add(user)

        if not success:
            self.notify("Signup failed: Account already exists.")
        else:
            self.notify("Signup successful!")
            self.to_login(ft.ControlEvent('', '', '', '', ''))
    
    def notify(self, message: str):
        self.page.snack_bar = ft.SnackBar(ft.Text(message))
        self.page.snack_bar.open = True
        self.page.update()