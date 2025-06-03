from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class RecordApp(App):
    def build(self):
        self.records = []

        # Головне вертикальне розміщення
        self.main_layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        # Введення
        self.name_input = TextInput(hint_text='Імʼя учня', size_hint_y=None, height=40)
        self.record_input = TextInput(hint_text='Досягнення', size_hint_y=None, height=40)
        add_button = Button(text='Додати запис', size_hint_y=None, height=40)
        add_button.bind(on_press=self.add_record)

        self.main_layout.add_widget(self.name_input)
        self.main_layout.add_widget(self.record_input)
        self.main_layout.add_widget(add_button)

        # Таблиця з GridLayout (2 колонки)
        self.table = GridLayout(cols=2, spacing=10, size_hint_y=None)
        self.table.bind(minimum_height=self.table.setter('height'))  # для адаптивності

        # Додаємо заголовки
        self.table.add_widget(Label(text='Імʼя', bold=True))
        self.table.add_widget(Label(text='Досягнення', bold=True))

        self.main_layout.add_widget(self.table)

        return self.main_layout

    def add_record(self, instance):
        name = self.name_input.text.strip()
        record = self.record_input.text.strip()
        if name and record:
            self.table.add_widget(Label(text=name))
            self.table.add_widget(Label(text=record))
            self.name_input.text = ''
            self.record_input.text = ''

if __name__ == '__main__':
    RecordApp().run()
