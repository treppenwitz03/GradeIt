import flet as ft
from widgets import NeuContainer, NeuTextField, RankItem

class HomeView(ft.Container):
    def __init__(self):
        super().__init__()

        greeting = ft.Text("Warm greetings,\n", style=ft.TextStyle(color=ft.Colors.BLACK, size=16), spans=[ft.TextSpan("OWEN", style=ft.TextStyle(weight=ft.FontWeight.BOLD, size=24))])
        user_image = ft.Icon(ft.Icons.PERSON_3, color=ft.Colors.BLACK, size=32)

        top_row = ft.Row(
            controls = [
                greeting,
                user_image
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )

        search_bar = NeuTextField("Search for your classes...", False, self.search)

        news_container = NeuContainer(
            ft.Column(
                controls=[
                    ft.Text("A new class has added you.", color="#c334eb", size=14, weight=ft.FontWeight.BOLD),
                    ft.Row(
                        controls=[
                            ft.Text("Add my grades to see rank", color = ft.Colors.BLACK, size=18, weight=ft.FontWeight.BOLD),
                            ft.IconButton(ft.Icons.NAVIGATE_NEXT, "#c334eb", icon_size=32, on_click=self.to_class)
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.START
            ),
            "#e8c6f5",
            "#c334eb",
            ft.padding.all(16),
            ft.margin.symmetric(16, 0)
        )

        classes_title = ft.Text("Classes", weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.START, size=24)

        classes_row = ft.Row(scroll=ft.ScrollMode.ALWAYS, spacing=16)
        classes_row.controls.append(ClassCard("USA", "america.svg", self.to_class))
        classes_row.controls.append(ClassCard("France", "french.jpg", self.to_class))
        classes_row.controls.append(ClassCard("Japan", "japan.jpg", self.to_class))
        classes_row.controls.append(ClassCard("Philippines", "philippines.jpg", self.to_class))

        prev_title = ft.Text("Previous Rankings", weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.START, size=24)

        old_rankings = ft.Column(spacing=0)
        old_rankings.controls.append(RankItem("Araling Panlipunan", "1st"))
        old_rankings.controls.append(RankItem("Physical Education", "2nd"))
        old_rankings.controls.append(RankItem("Science and Tech", "1st"))
        old_rankings.controls.append(RankItem("Values Education", "43rd"))
        old_rankings.controls.append(RankItem("Mixed Signals", "1st"))
        old_rankings.controls.append(RankItem("Research Methods", "1st"))
        old_rankings.controls.append(RankItem("Data Structures", "1st"))

        self.content = ft.Column(
            controls=[
                top_row,
                search_bar,
                news_container,
                classes_title,
                classes_row,
                prev_title,
                NeuContainer(old_rankings, bgcolor="#fffada", padding=ft.padding.all(0), margin=ft.margin.all(0))
            ],
            horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
            spacing=16,
            scroll=ft.ScrollMode.ALWAYS,
            expand=True
        )
    
    def search(self, event):
        pass

    def to_class(self, event):
        views: dict = self.page.session.get("views")
        switcher: ft.AnimatedSwitcher = self.parent

        switcher.content = views["class"]
        switcher.update()

        switcher.content.show_nav_bar()

class ClassCard(NeuContainer):
    def __init__(self, class_name: str, banner_img: str, on_click: callable = None):
        super().__init__(
            padding=ft.padding.all(0),
        )

        self.width = 200
        self.height = 200

        banner = ft.Image(banner_img, width=200, height=150, fit=ft.ImageFit.FILL, border_radius=12)
        title = ft.Text(class_name, weight=ft.FontWeight.BOLD)
        self.border = ft.border.all(4, ft.Colors.BLACK)

        self.content = ft.Column(
            controls=[
                banner,
                title
            ], 
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )

        self.on_click = lambda e: on_click(e)