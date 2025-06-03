from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class RecordApp(App):
    def build(self):
        # Головний вертикальний макет
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        # Поле вводу імені
        self.name_input = TextInput(hint_text='Введи імʼя учня', multiline=False, size_hint_y=None, height=50, size_hint_x=None, width=400)
        layout.add_widget(self.name_input)

        # Поле вводу досягнення
        self.record_input = TextInput(hint_text='Введи досягнення учня', multiline=False, size_hint_y=None, height=50, size_hint_x=None, width=400)
        layout.add_widget(self.record_input)

        # Кнопка додавання запису
        add_button = Button(text='Додати досягнення', size_hint_x=None, width=400)
        add_button.bind(on_press=self.add_record)
        layout.add_widget(add_button)

        # Вивід результатів
        self.output_label = Label(text='Тут будуть рекорди учнів', halign='left', valign='top')
        layout.add_widget(self.output_label)

        # Список збережених записів
        self.records = []

        return layout

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
        with open("records.txt", "a", encoding="utf-8") as file:
            file.write(f"{name}-{record}\n")

if __name__ == '__main__':
    RecordApp().run()
