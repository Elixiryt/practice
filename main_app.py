from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from login import LoginScreen
from main import MainScreen

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(MainScreen(name='main'))
        return sm

if __name__ == '__main__':
    MyApp().run()
