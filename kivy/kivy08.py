# config: utf-8

from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window


root = Label(text='This is a sample.')


class kivy08(App):
    def build(self):
        print('0) create instance of application')
        return root

    def on_start(self):
        print('1) start application')

    def on_stop(self):
        print('2) stop application')


Window.size = (250, 50)
kivy08().run()