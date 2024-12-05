import flet as ft

class NeuContainer(ft.Container):
    def __init__(self, content: ft.Control = None, bgcolor: ft.Colors = ft.Colors.WHITE, color: ft.Colors = ft.Colors.BLACK, padding: ft.Padding = ft.padding.all(8), margin: ft.Margin = ft.margin.all(8)):
        super().__init__()
        self.bgcolor = bgcolor
        self.border_radius = 12
        self.border = ft.border.all(2, color)
        self.padding = padding
        self.margin = margin
        self.content = content

        self.shadow = ft.BoxShadow(
            blur_radius=16,
            color=color,
            offset=ft.Offset(4, 4),
            blur_style=ft.ShadowBlurStyle.SOLID,
        )