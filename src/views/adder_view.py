import flet as ft
import array as arr
from widgets import NeuButton, NeuTextField

from utils import UserDatabase

class TextFieldArray:
    def __init__(self):
        self.fields = []

    def append(self, label, on_change):
        field = NeuTextField(label, on_change=on_change)
        self.fields.append(field)

    def __getitem__(self, index):
        return self.fields[index]

    def __setitem__(self, index, value):
        if isinstance(value, NeuTextField):
            self.fields[index] = value
        else:
            raise TypeError("Only NeuTextField instances can be assigned.")

    def __len__(self):
        return len(self.fields)

    def __iter__(self):
        return iter(self.fields)

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
        self.text_fields = TextFieldArray()
        self.text_fields.append("Data Structures and Algorithms", self.on_change)
        self.text_fields.append("Introduction to HDL", self.on_change)
        self.text_fields.append("Research Methods", self.on_change)
        self.text_fields.append("Mixed Signals", self.on_change)
        self.text_fields.append("Feedback", self.on_change)
        self.text_fields.append("Logic", self.on_change)
        self.text_fields.append("Fili", self.on_change)
        self.text_fields.append("CISCO", self.on_change)

        self.upload_button = NeuButton("Add Grades", "#6743f8", disabled=True, on_click=self.add_grades)
        
        self.content = ft.Column(
            controls=[
                top_row,
                title,
                *self.text_fields,
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

        # Collect grades from TextFieldArray
        grades = [int(field.value) for field in self.text_fields]
        user_database.add_grades(user_name, self.group, *grades)

        self.return_class(event)
    
    def return_class(self, event):
        views: dict = self.page.session.get("views")
        switcher: ft.AnimatedSwitcher = self.parent

        switcher.content = views["class"]
        switcher.update()
        switcher.content.load_rankings(self.group)