import flet as ft
from widgets import NeuButton, NeuTextField

class SignupView(ft.Container):
    def __init__(self):
        super().__init__()

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

        uname_tf = NeuTextField("Username", False, on_change=self.on_change)
        email_tf = NeuTextField("Enter your Email", False, on_change=self.on_change)
        password_tf = NeuTextField("Enter your Password", True, on_change=self.on_change)
        confirm_password_tf = NeuTextField("Confirm your Password", True, on_change=self.on_change)

        self.agree_eula = ft.Checkbox("I agree to the Terms and Conditions", check_color=ft.Colors.BLACK, label_style=ft.TextStyle(color=ft.Colors.BLACK, weight=ft.FontWeight.BOLD))

        self.proceed_button = NeuButton("Sign Up", "#fa8128")

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
                uname_tf,
                email_tf,
                password_tf,
                confirm_password_tf,
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
        pass

    def register_hovered(self, event: ft.HoverEvent):
        self.register_text.spans[0].style.color = ft.Colors.PINK if "enter" in event.name else ft.Colors.BLUE
        self.page.update()
    
    def to_login(self, event):
        views: dict = self.page.session.get("views")
        switcher: ft.AnimatedSwitcher = self.parent

        switcher.content = views["login"]
        switcher.update()