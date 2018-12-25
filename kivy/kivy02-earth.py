# config: utf-8

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.slider import Slider


# event callback
def on_value_change(self, v):
    im.size_hint = (sl.value, sl.value)


root = BoxLayout(orientation='vertical')

# image and layout
anchor = AnchorLayout()
im = Image(source='Earth.jpg')
anchor.add_widget(im)

# create slider
sl = Slider(min=0.0, max=1.0, step=0.01)
sl.size_hint = (1.0, 0.1)
sl.value = 1.0
sl.bind(value=on_value_change)

root.add_widget(anchor)
root.add_widget(sl)


# application class
class kivy02(App):
    def build(self):
        return root

Window.size = (500, 500)

print(im.texture_size)
ap = kivy02()
ap.run()