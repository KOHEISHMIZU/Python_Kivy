# config: utf-8

import sys
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.graphics import Color, Line
from kivy.core.window import Window


# application class
class kivy03(App):
    def build(self):
        return root


Window.size = (600, 400)
Window.clearcolor = (1, 1, 1, 1)

# create top layout
root = BoxLayout(orientation='vertical')

# create button panel
btnpanel = BoxLayout(orientation='horizontal')
btnClear = Button(text='Clear')
btnQuit = Button(text='Quit')
btnpanel.add_widget(btnClear)  # btnClear install
btnpanel.add_widget(btnQuit)  # btnQuit install
btnpanel.size_hint = (1.0, 0.1)  # btnpanel_size change
root.add_widget(btnpanel)  # btnpanel install for main_widet

# draw area create
drawArea = Widget()
root.add_widget(drawArea)


# Function to erase draw area
def callback_clear(self):
    drawArea.canvas.clear()
    drawArea.canvas.add(Color(0.4, 0.4, 0.4, 1))
    drawArea.lineObject = Line(points=[], width=10)
    drawArea.canvas.add(drawArea.lineObject)


btnClear.bind(on_release=callback_clear)


# Function to quit application
def callback_quit(self):
    sys.exit()


btnQuit.bind(on_release=callback_quit)


# Function to draw
def callback_draw_start(self, t):
    self.canvas.add(Color(0.4, 0.4, 0.4, 1))
    self.lineObject = Line(points=(t.x, t.y), width=10)
    self.canvas.add(self.lineObject)


def callback_draw_move(self, t):
    self.lineObject.points += (t.x, t.y)


def callback_draw_end(self, t):
    pass


drawArea.bind(on_touch_down=callback_draw_start)
drawArea.bind(on_touch_move=callback_draw_move)
drawArea.bind(on_touch_up=callback_draw_end)

ap = kivy03()
ap.run()