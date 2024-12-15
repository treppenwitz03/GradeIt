import flet as ft
from widgets import NeuContainer, RankItem, NeuButton, NeuTextField

from utils import UserDatabase

class AdderView(ft.Container):
    def __init__(self):
        super().__init__()
        self.padding = 16

        back_button = ft.IconButton(ft.Icons.ARROW_BACK, ft.Colors.BLACK, on_click=self.return_class)
        class_settings_btn = ft.PopupMenuButton(icon=ft.Icons.SETTINGS, icon_color=ft.Colors.BLACK, icon_size=32)

        top_row = ft.Row(
            controls = [
                back_button,
                class_settings_btn
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )

        title = ft.Text("Enter your grades", weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.START, size=24)
        self.dsa = NeuTextField("Data Structures and Algorithms", on_change=self.on_change)
        self.hdl = NeuTextField("Introduction to HDL", on_change=self.on_change)
        self.rm = NeuTextField("Research Methods", on_change=self.on_change)
        self.ms = NeuTextField("Mixed Signals", on_change=self.on_change)
        self.fb = NeuTextField("Feedback", on_change=self.on_change)
        self.logic = NeuTextField("Logic", on_change=self.on_change)
        self.fili = NeuTextField("Fili", on_change=self.on_change)
        self.cisco = NeuTextField("CISCO", on_change=self.on_change)

        self.upload_button = NeuButton("Add Grades", "#6743f8", disabled=True, on_click=self.add_grades)
        
        self.content = ft.Column(
            controls=[
                top_row,
                title,
                self.dsa,
                self.hdl,
                self.rm,
                self.ms,
                self.fb,
                self.logic, 
                self.fili,
                self.cisco,
                self.upload_button
            ],
            horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
            spacing=16,
            scroll=ft.ScrollMode.ALWAYS,
        )
    
    def on_change(self, event):
        if all([self.dsa.value, self.hdl.value, self.rm.value, self.ms.value, self.fb.value, self.logic.value, self.fili.value, self.cisco.value]):
            self.upload_button.disabled = False
        else:
            self.upload_button.disabled = True

        self.upload_button.update()
    
    def add_grades(self, event):
        user_name = self.page.session.get("user")
        self.group = self.page.session.get("group")

        user_database: UserDatabase = self.page.session.get("user_database")
        user_database.add_grades(
            user_name,
            self.group,
            int(self.dsa.value),
            int(self.hdl.value),
            int(self.rm.value),
            int(self.ms.value),
            int(self.fb.value),
            int(self.logic.value),
            int(self.fili.value),
            int(self.cisco.value)
        )

        self.return_class(event)
    
    def return_class(self, event):
        views: dict = self.page.session.get("views")
        switcher: ft.AnimatedSwitcher = self.parent

        switcher.content = views["class"]
        switcher.update()
        switcher.content.load_rankings(self.group)