import flet as ft

class RankItem(ft.Container):
    def __init__(self, subject: str, ranking: str):
        super().__init__()
        self.height = 48
        self.content = ft.Row(
            controls = [
                ft.Container(ft.Text(subject, weight=ft.FontWeight.BOLD, size=14, expand=True), padding=ft.padding.only(16, 8, 0, 8), expand=True),
                ft.VerticalDivider(2, thickness=2, color=ft.Colors.BLACK),
                ft.Container(ft.Text(ranking, weight=ft.FontWeight.BOLD, width=32, size=14, text_align=ft.TextAlign.CENTER), padding=ft.padding.symmetric(8, 16))
            ],
            alignment = ft.MainAxisAlignment.SPACE_BETWEEN
        )
        self.border = ft.border.only(ft.BorderSide(0), ft.BorderSide(0), ft.BorderSide(0), ft.BorderSide(2, ft.Colors.BLACK))