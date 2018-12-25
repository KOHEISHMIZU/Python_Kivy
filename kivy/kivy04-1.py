# config utf-8

import math
from kivy.app import App
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
from kivy.uix.widget import Widget


class kivy04(App):
    def build(self):
        return root


root = Widget()

root.canvas.add(Color(1, 0, 0, 1))
x = 0.0
while x < 6.28:
    y = 100.0 * math.sin(x)
    # y = 100.0 * math.cos(x)
    # y = 100.0 * math.tan(x)
    root.canvas.add(Rectangle(pos=(32.0*x+5.0, y+105.0), size=(3, 3)))
    x += 0.005

Window.size = (210, 210)
kivy04().run()