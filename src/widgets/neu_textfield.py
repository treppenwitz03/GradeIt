import flet as ft

class NeuTextField(ft.CupertinoTextField):
    def __init__(self, hint: str, is_password: bool = False, on_change: callable = None):
        super().__init__()

        self.placeholder_text = hint
        self.password = is_password
        self.can_reveal_password = True if self.password else False
        self.bgcolor = ft.Colors.WHITE
        self.border = ft.border.all(2, ft.Colors.BLACK)
        self.border_color = ft.Colors.BLACK
        self.cursor_color = ft.Colors.BLACK
        self.color = ft.Colors.BLACK
        self.placeholder_style = ft.TextStyle(color=ft.Colors.BLACK)

        self.shadow = ft.BoxShadow(
            blur_radius=12,
            color=ft.Colors.BLACK,
            offset=ft.Offset(4, 4),
            blur_style=ft.ShadowBlurStyle.SOLID,
        )