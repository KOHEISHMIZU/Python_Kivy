# config: utf-8

import sys
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.graphics import Color
from kivy.graphics import Line
from kivy.core.window import Window


class kivy03(App):
    def build(self):
        return root


class BtnClear(Button):
    def on_release(self):
         drawArea.canvas.clear()


class BtnQuit(Button):
    def on_release(self):
        sys.exit()


class DrawArea(Widget):
    def on_touch_up(self, t):
        self.canvas.add(Color(0.4, 0.4, 0.4, 1))
        self.lineObject = Line(points=(t.x, t.y), width=10)
        self.canvas.add(self.lineObject)

    def on_touch_move(self, t):
        self.lineObject.points += (t.x, t.y)

    def on_touch_down(self, t):
        pass


Window.size = (600, 400)
Widget.clearcolor = (1, 1, 1, 1)

root = BoxLayout(orientation='vertical')

btnpanel = BoxLayout(orientation='horizontal')
btnClear = BtnClear(text='Clear')
btnQuit = BtnQuit(text='Quit')
btnpanel.add_widget(btnClear)
btnpanel.add_widget(btnQuit)
btnpanel.size_hint = (1.0, 0.1)
root.add_widget(btnpanel)

drawArea = DrawArea()
root.add_widget(drawArea)

ap = kivy03()
ap.run()