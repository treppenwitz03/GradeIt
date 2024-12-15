import flet as ft
from widgets import NeuContainer, RankItem, NeuButton, NeuTextField
from utils import UserDatabase, ordinalize
import heapq

class BSTNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key, value):
        def _insert(node, key, value):
            if not node:
                return BSTNode(key, value)
            if key < node.key:
                node.left = _insert(node.left, key, value)
            elif key > node.key:
                node.right = _insert(node.right, key, value)
            return node

        self.root = _insert(self.root, key, value)

    def search(self, key):
        def _search(node, key):
            if not node or node.key == key:
                return node
            if key < node.key:
                return _search(node.left, key)
            return _search(node.right, key)

        result = _search(self.root, key)
        return result.value if result else None

class ClassView(ft.Container):
    def __init__(self):
        super().__init__()
        self.padding = 16

        back_button = ft.IconButton(ft.Icons.ARROW_BACK, ft.Colors.BLACK, on_click=self.return_home)
        class_settings_btn = ft.PopupMenuButton(icon=ft.Icons.SETTINGS, icon_color=ft.Colors.BLACK, icon_size=32)

        top_row = ft.Row(
            controls=[
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

        self.groups_bst = BinarySearchTree()

    def return_home(self, event):
        views: dict = self.page.session.get("views")
        switcher: ft.AnimatedSwitcher = self.parent

        switcher.content = views["home"]
        switcher.update()

    def load_rankings(self, name):
        self.ranking_column.controls = []
        self.user_database: UserDatabase = self.page.session.get("user_database")
        current_user = self.page.session.get("user")

        # Load groups into BST if not already loaded
        if not self.groups_bst.root:
            groups = self.user_database.get_groups_for_user(current_user)
            for group in groups:
                for key, value in group.items():
                    self.groups_bst.insert(key, value)

        current_group = self.groups_bst.search(name)
        if not current_group:
            return

        self.page.session.set("group", name)

        if current_group.get(current_user, {}) == {}:
            self.calc_grades.visible = True
        else:
            self.calc_grades.visible = False
        self.calc_grades.update()

        average_list = []

        for person, grades in current_group.items():
            all_grades = list(dict(grades).values())
            if len(all_grades) > 0:
                average = sum(all_grades) / len(all_grades)
                heapq.heappush(average_list, (-average, person))

        while average_list:
            index = len(self.ranking_column.controls)
            average, person = heapq.heappop(average_list)
            rank = ordinalize(index + 1)
            self.ranking_column.controls.append(RankItem(person, rank))
            self.ranking_column.update()

    def to_calcu(self, event):
        views: dict = self.page.session.get("views")
        switcher: ft.AnimatedSwitcher = self.parent

        switcher.content = views["calc"]
        switcher.update()