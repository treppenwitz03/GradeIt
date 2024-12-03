import flet as ft

class OpeningView(ft.Container):
    def __init__(self):
        super().__init__()

        icon = ft.Image(
            src="lottie/neobrutalist.jpg",
            fit=ft.ImageFit.CONTAIN,
            width=300,
            height=300
        )

        text = ft.Text("Calculate your Grades and Know your Rank.", weight=ft.FontWeight.BOLD, size=32)

        self.login_button = NeuButton("Login", "#ecc7d3")
        self.signup_button = NeuButton("Signup", "#48aaad")

        self.content = ft.Column(
            controls=[
                icon,
                text,
                self.login_button,
                self.signup_button
            ],
            horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
            spacing=16
        )

class NeuButton(ft.GestureDetector):
    def __init__(self, label: str, col: str):
        super().__init__()
        container = ft.Container()
        container.content = ft.Text(label, weight=ft.FontWeight.BOLD, color="black", text_align=ft.TextAlign.CENTER)
        container.bgcolor = col
        container.border_radius = 12
        container.border = ft.border.all(2, ft.Colors.BLACK)
        container.padding = ft.padding.all(8)
        container.animate_offset = ft.animation.Animation(250)

        self.shadow = ft.BoxShadow(
            blur_radius=12,
            color=ft.Colors.BLACK,
            offset=ft.Offset(4, 4),
            blur_style=ft.ShadowBlurStyle.SOLID,
        )

        container.shadow = self.shadow

        container.on_hover = self.__hover__
        self.on_tap_down = self.__pressed__
        self.on_tap_up = self.__released__

        self.content = container
    
    def __hover__(self, event: ft.HoverEvent):
        self.content.opacity = 0.8 if event.data == "true" else 1.0
        self.update()
    
    def __pressed__(self, event: ft.ControlEvent):
        self.shadow.offset = ft.Offset(0, 0)
        self.update()
    
    def __released__(self, event: ft.ControlEvent):
        self.shadow.offset = ft.Offset(4, 4)
        self.update()