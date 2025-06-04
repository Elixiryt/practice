from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
import json

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        self.name_input = TextInput(hint_text='Введи імʼя учня', multiline=False)
        self.record_input = TextInput(hint_text='Введи досягнення учня', multiline=False)

        self.output_label = Label(text='Тут будуть рекорди учнів')

        add_button = Button(text='Додати досягнення')
        add_button.bind(on_press=self.add_record)

        layout.add_widget(self.name_input)
        layout.add_widget(self.record_input)
        layout.add_widget(add_button)
        layout.add_widget(self.output_label)

        self.records = []
        self.add_widget(layout)

    def add_record(self, instance):
        name = self.name_input.text.strip()
        record = self.record_input.text.strip()
        if name and record:
            entry = f"{name}: {record}"
            self.records.append(entry)
            self.output_label.text = '\n'.join(self.records)
            self.name_input.text = ''
            self.record_input.text = ''
            self.save_to_file(name, record)
        else:
            self.output_label.text = 'Будь ласка, введи і імʼя, і досягнення.'

    def save_to_file(self, name, record):
        try:
            try:
                with open("files/records.json", "r", encoding="utf-8") as file:
                    content = file.read()
                    if content.strip() == "":
                        data = []
                    else:
                        data = json.loads(content)
                        if not isinstance(data, list):
                            data = [data]
            except FileNotFoundError:
                data = []

            data.append({"name": name, "record": record})

            with open("files/records.json", "w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)

            print("✅ Успішно збережено!")
        except Exception as e:
            print("❌ ПОМИЛКА:", e)
