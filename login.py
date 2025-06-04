from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import json

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation="vertical", padding=20, spacing=10)

        self.input_username = TextInput(hint_text="Введіть логін")
        self.input_password = TextInput(hint_text="Введіть пароль")

        layout.add_widget(self.input_username)
        layout.add_widget(self.input_password)

        button_login = Button(text="Увійти")
        button_login.bind(on_press=self.login)
        layout.add_widget(button_login)

        self.add_widget(layout)

    def login(self, instance):
        username = self.input_username.text.strip()
        password = self.input_password.text.strip()
        login_list = {"username": username, "password": password}

        try:
            with open("files/cake.json", "r", encoding="utf-8") as file:
                data = json.load(file)
                if login_list in data:
                    self.manager.current = "main"
                else:
                    print("❌ Невірний логін або пароль")
        except Exception as e:
            print("❌ ПОМИЛКА:", e)
