# config: utf-8

from kivy.app import App
from kivy.uix.label import Label


class kivy01(App):
    def build(self):
        self.lb1 = Label(text='This is a test of kivy')
        return self.lb1


ap = kivy01()
ap.run()