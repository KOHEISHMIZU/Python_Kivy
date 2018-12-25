# config: utf-8

from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window


class MyLabel(Label):
    def on_touch_move(self, touch):
        print(self.events())
        print('touch down :', touch.spos)

    def on_touch_up(self, touch):
        print('touch up :', touch.spos)


class kivy01(App):
    def build(self):
        self.lb1 = MyLabel(text='This is a test of Kivy')
        return self.lb1


Window.size = (400, 100)

ap = kivy01()
ap.run()