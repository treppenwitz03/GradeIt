import flet as ft
from widgets import NeuContainer, NeuTextField, RankItem, NeuButton
from utils import UserDatabase

class HomeView(ft.Container):
    def __init__(self):
        super().__init__()
        self.padding = 16

        self.user_text = ft.TextSpan("", style=ft.TextStyle(weight=ft.FontWeight.BOLD, size=24))

        greeting = ft.Text("Warm greetings,\n", style=ft.TextStyle(color=ft.Colors.BLACK, size=16), spans=[self.user_text])
        user_image = ft.Icon(ft.Icons.PERSON_3, color=ft.Colors.BLACK, size=32)

        top_row = ft.Row(
            controls = [
                greeting,
                user_image
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )

        self.add_class = NeuButton("Add a Class", "#48aaad", on_click=self.create_class, padding=ft.padding.symmetric(16, 0))

        classes_title = ft.Row(
            controls = [
                ft.Text("Classes", weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.START, size=24),
                self.add_class
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )

        self.classes_row = ft.ResponsiveRow(run_spacing=16)

        self.content = ft.Column(
            controls=[
                top_row,
                classes_title,
                self.classes_row
            ],
            horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
            spacing=16,
            scroll=ft.ScrollMode.ALWAYS,
            expand=True
        )
    
    def create_class(self, event):
        group_name = NeuTextField("Enter Class name")
        self.page.dialog = ft.AlertDialog(
            title=ft.Text("Add Class"),
            content=group_name,
            actions=[
                ft.TextButton("Submit", on_click= lambda e: self.add_new_class(group_name.value))
            ]
        )

        self.page.dialog.open = True
        self.page.update()
    
    def add_new_class(self, group_name):
        self.page.dialog.open = False
        self.page.update()

        self.user_database.create_group_for_user(self.user_text.text, group_name)
        groups = self.user_database.get_groups_for_user(self.user_text.text)

        self.load_groups(groups)

    def to_class(self, name):
        views: dict = self.page.session.get("views")
        switcher: ft.AnimatedSwitcher = self.parent

        switcher.content = views["class"]
        switcher.update()

        switcher.content.load_rankings(name)
    
    def set_name(self, name):
        self.user_text.text = name
        self.user_text.update()

        self.user_database: UserDatabase = self.page.session.get("user_database")
        self.groups = self.user_database.get_groups_for_user(name)

        if not self.groups:
            self.notify("No classes joined yet. Add one.")
            return

        self.load_groups(self.groups)
    
    def load_groups(self, groups):
        self.classes_row.controls = []
        group: dict = None
        for index, group in enumerate(groups):
            name = list(group.keys())[0]
            self.classes_row.controls.append(ClassCard(name, on_click=lambda e: self.to_class(e.control.class_name)))
            self.classes_row.update()
    
    def notify(self, message: str):
        self.page.snack_bar = ft.SnackBar(ft.Text(message))
        self.page.snack_bar.open = True
        self.page.update()

class ClassCard(NeuContainer):
    def __init__(self, class_name: str, on_click: callable = None):
        super().__init__(
            padding=ft.padding.all(0),
        )

        self.width = 200
        self.height = 200
        self.col = {"sm": 6, "md": 4, "xl": 2}
        self.class_name = class_name

        banner = ft.Image("class.png", width=200, height=150, fit=ft.ImageFit.FILL, border_radius=12)
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