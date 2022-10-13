from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
import os


class ContaMensal(Screen):
    pass


GUI = Builder.load_file('main.kv')


class MyContasApp(App):
    def build(self):
        return GUI


if __name__ == '__main__':
    MyContasApp().run()