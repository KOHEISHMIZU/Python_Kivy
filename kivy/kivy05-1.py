# config: utf-8

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen


class kivy05(App):
    def build(self):
        return root


Window.size = (300, 100)

root = ScreenManager()
# screen
sc1 = Screen(name='screen_1')
sc2 = Screen(name='screen_2')
# layout
al1 = AnchorLayout()
al2 = AnchorLayout()
# label
lb1 = Label(text='This is Screen-1\nSwitch to Screen-2')
lb2 = Label(text='This is Screen-2\nSwitch to Screen-1')
# make
al1.add_widget(lb1)
al2.add_widget(lb2)
sc1.add_widget(al1)
sc2.add_widget(al2)
root.add_widget(sc1)
root.add_widget(sc2)

root.current = ('screen_1')


# callback_function
def callback1(self, t):
    root.transition.direction = 'left'
    root.transition.duration = 3
    root.current = 'screen_2'


def callback2(self, t):
    root.transition.direction = 'right'
    root.transition.duration = 0.4
    root.current = 'screen_1'


# label object
lb1.bind(on_touch_up=callback1)
lb2.bind(on_touch_up=callback2)

ap = kivy05()
ap.run()