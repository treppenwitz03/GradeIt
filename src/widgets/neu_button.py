import flet as ft

class NeuButton(ft.GestureDetector):
    def __init__(self, content: str | ft.Icons | ft.Control, col: str = None, on_click: callable = None, padding: ft.Padding = ft.padding.all(0)):
        super().__init__()
        cont = ft.Container()

        if content is ft.Icons:
            cont.content = ft.Icon(content)
        elif type(content).__name__ in ['Column', 'Container', 'Control', 'Text', 'Image']:
            cont.content = content
        else:
            cont.content = ft.Text(content, weight=ft.FontWeight.BOLD, color="black", text_align=ft.TextAlign.CENTER)

        cont.bgcolor = col
        cont.border_radius = 12
        cont.border = ft.border.all(2, ft.Colors.BLACK)
        cont.padding = ft.padding.all(8)
        cont.margin = ft.margin.only(padding.left, padding.top, padding.right, padding.bottom)
        cont.animate_offset = ft.animation.Animation(250)
        self.clicked_callable = on_click

        self.shadow = ft.BoxShadow(
            blur_radius=12,
            color=ft.Colors.BLACK,
            offset=ft.Offset(4, 4),
            blur_style=ft.ShadowBlurStyle.SOLID,
        )

        cont.shadow = self.shadow

        cont.on_hover = self.__hover__
        self.on_tap_down = self.__pressed__
        self.on_tap_up = self.__released__

        self.content = cont
    
    def __hover__(self, event: ft.HoverEvent):
        self.content.opacity = 0.8 if event.data == "true" else 1.0
        self.update()
    
    def __pressed__(self, event: ft.ControlEvent):
        self.shadow.offset = ft.Offset(0, 0)
        self.update()

        if self.clicked_callable is not None:
            self.clicked_callable(event)
    
    def __released__(self, event: ft.ControlEvent):
        self.shadow.offset = ft.Offset(4, 4)
        self.update()