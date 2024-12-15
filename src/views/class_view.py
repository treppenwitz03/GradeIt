import flet as ft
from widgets import NeuContainer, RankItem, NeuButton
from utils import UserDatabase, ordinalize

class ClassView(ft.Container):
    def __init__(self):
        super().__init__()
        self.padding = 16

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
        self.ranking_column = ft.Column(spacing=0, scroll=ft.ScrollMode.AUTO)

        self.calc_grades = NeuButton("Add my Grades", "#48aaad", on_click=self.to_calcu, padding=ft.padding.symmetric(16, 0))

        self.content = ft.Column(
            controls=[
                top_row,
                ft.Row([title, self.calc_grades], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                NeuContainer(self.ranking_column, bgcolor="#fffada", padding=ft.padding.all(0), margin=ft.margin.all(0)),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
            spacing=16,
            scroll=ft.ScrollMode.ALWAYS,
        )
    
    def return_home(self, event):
        views: dict = self.page.session.get("views")
        switcher: ft.AnimatedSwitcher = self.parent

        switcher.content = views["home"]
        switcher.update()
    
    def load_rankings(self, name):
        self.ranking_column.controls = []
        self.user_database: UserDatabase = self.page.session.get("user_database")
        current_user = self.page.session.get("user")

        self.groups = self.user_database.get_groups_for_user(current_user)
        current_group:dict = None
        for group in self.groups:
            for g in group:
                if g == name:
                    current_group = group
        
        self.page.session.set("group", name)
        
        if current_group[name][current_user] == {}:
            self.calc_grades.visible = True
        else:
            self.calc_grades.visible = False
        self.calc_grades.update()

        average_list = []

        for person, grades in current_group[name].items():
            all_grades = list(dict(grades).values())
            if len(all_grades) > 0:
                average = sum(all_grades)/len(all_grades)
                average_list.append((person, average))
        
        ranking = sorted(average_list, key=self.sort_func, reverse=True)
        for index, item in enumerate(ranking):
            rank = ordinalize(index + 1)
            person = item[0]
            self.ranking_column.controls.append(RankItem(person, rank))
            self.ranking_column.update()
    
    def sort_func(self, item):
        return int(item[1])
    
    def to_calcu(self, event):
        views: dict = self.page.session.get("views")
        switcher: ft.AnimatedSwitcher = self.parent

        switcher.content = views["calc"]
        switcher.update()