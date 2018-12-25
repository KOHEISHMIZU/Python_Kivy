# config: utf-8

from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.carousel import Carousel
from kivy.uix.label import Label


class kivy05(App):
    def build(self):
        return root


# create Carousel
root = Carousel(direction='right')
lb1 = Label(text='Slide_1')
lb2 = Label(text='Slide_2')
lb3 = Label(text='Slide_3')
root.add_widget(lb1)
root.add_widget(lb2)
root.add_widget(lb3)
root.loop = True


# Auto swipe
# callback function
def auto_swipe(dt):
    print(dt)
    root.load_next()
    return True


# schedule
tm = Clock.schedule_interval(auto_swipe, 3)
print(type(tm))


# callback function to cancel
def cancel_swipe(self, t):
    print('auto swipe canceled')
    Clock.unschedule(tm)


root.bind(on_touch_up=cancel_swipe)

Window.size = (300, 150)
ap = kivy05()
ap.run()