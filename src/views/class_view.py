import flet as ft
from widgets import NeuContainer, RankItem, NeuButton

class ClassView(ft.Container):
    def __init__(self):
        super().__init__()

        back_button = ft.IconButton(ft.Icons.ARROW_BACK, ft.Colors.BLACK, on_click=self.return_home)
        class_settings_btn = ft.PopupMenuButton(icon=ft.Icons.SETTINGS, icon_color=ft.Colors.BLACK, icon_size=32)

        top_row = ft.Row(
            controls = [
                back_button,
                class_settings_btn
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )

        title = ft.Text("Rankings", weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.START, size=24)
        rankings = ft.Column(spacing=0, scroll=ft.ScrollMode.AUTO)
        rankings.controls.append(RankItem("Araling Panlipunan", "1st"))
        rankings.controls.append(RankItem("Physical Education", "2nd"))
        rankings.controls.append(RankItem("Science and Tech", "1st"))
        rankings.controls.append(RankItem("Values Education", "43rd"))
        rankings.controls.append(RankItem("Mixed Signals", "1st"))
        rankings.controls.append(RankItem("Research Methods", "1st"))
        rankings.controls.append(RankItem("Data Structures", "1st"))
        rankings.controls.append(RankItem("Araling Panlipunan", "1st"))
        rankings.controls.append(RankItem("Physical Education", "2nd"))
        rankings.controls.append(RankItem("Science and Tech", "1st"))
        rankings.controls.append(RankItem("Values Education", "43rd"))
        rankings.controls.append(RankItem("Mixed Signals", "1st"))
        rankings.controls.append(RankItem("Research Methods", "1st"))
        rankings.controls.append(RankItem("Data Structures", "1st"))

        calc_grades = NeuButton("Add my Grades", "#48aaad", on_click=self.to_calcu, padding=ft.padding.symmetric(16, 0))

        self.navigation_pane = ft.CupertinoNavigationBar(
            destinations=[
                ft.NavigationBarDestination(
                    icon = NavigationIcon(ft.Icons.CLASS_OUTLINED, "Rankings"),
                    selected_icon = NavigationIcon(ft.Icons.CLASS_, "Rankings")
                ),
                ft.NavigationBarDestination(
                    icon = NavigationIcon(ft.Icons.PERSON_2_OUTLINED, "Members"),
                    selected_icon = NavigationIcon(ft.Icons.PERSON_2, "Members")
                )
            ],
            height=80,
            bgcolor="#fffada",
            border=ft.border.only(top=ft.BorderSide(2, ft.Colors.BLACK)),
            active_color="#c334eb",
            inactive_color=ft.Colors.BLACK
        )

        self.content = ft.Column(
            controls=[
                top_row,
                ft.Row([title, calc_grades], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                NeuContainer(rankings, bgcolor="#fffada", padding=ft.padding.all(0), margin=ft.margin.all(0)),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
            spacing=16,
            scroll=ft.ScrollMode.ALWAYS,
        )
    
    def return_home(self, event):
        self.page.navigation_bar = None
        self.page.update()
        
        views: dict = self.page.session.get("views")
        switcher: ft.AnimatedSwitcher = self.parent

        switcher.content = views["home"]
        switcher.update()
    
    def show_nav_bar(self):
        self.page.navigation_bar = self.navigation_pane
        self.page.update()
    
    def to_calcu(self, event):
        print("HAHAHA")

class NavigationIcon(ft.Container):
    def __init__(self, icon: ft.Icons = None, label: str = None):
        super().__init__()
        self.content = ft.Column(
            controls=[
                ft.Icon(icon),
                ft.Text(label, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK)
            ],
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=4
        )
        self.margin=ft.margin.only(top=8)
        self.padding=ft.padding.all(8)
        self.border_radius = 12
        self.border = ft.border.all(2, ft.Colors.BLACK)
        self.bgcolor = "#fffada"

        self.shadow = ft.BoxShadow(
            blur_radius=12,
            color=ft.Colors.BLACK,
            offset=ft.Offset(4, 4),
            blur_style=ft.ShadowBlurStyle.SOLID
        )