from kivy.app import App
from kivy.lang import Builder

GUI = Builder.load_file('main.kv')


class MyApp(App):
    def build(self):
        return GUI


if __name__ == '__main__':
    MyApp().run()