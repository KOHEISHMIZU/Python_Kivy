# config: utf-8

from kivy.app import App
from kivy.core.window import Window
from kivy.graphics import Color, Line, Rectangle, Ellipse
from kivy.uix.image import Image
from kivy.uix.widget import Widget


class kivy04(App):
    def build(self):
        return root


# read image and take out texture
img = Image(source='index.jpeg')
tx = img.texture

root = Widget()
# draw Rectangle
root.canvas.add(Color(1, 0, 0, 1))
root.canvas.add(Rectangle(pos=(10, 210), size=(350, 100)))
# draw Image
root.canvas.add(Color(1, 1, 1, 1))
root.canvas.add(Rectangle(pos=(0, 0), texure=tx, size=(210, 200)))
# draw Ellipse
root.canvas.add(Color(0, 1, 0, 1))
root.canvas.add(Ellipse(pos=(200, 10), size=(170, 170)))
# draw Line
root.canvas.add(Color(1, 1, 1, 1))
root.canvas.add(Line(width=10, points=[580, 25, 400, 25, 580, 160, 400, 290, 580, 290]))

# screen shot
def save_shot(self, t):
    # method1
    Window.screenshot(name='kivy04-2-1.png')
    # method2
    self.export_to_png('kivy04-2-2.png')

root.bind(on_touch_up=save_shot)

Window.size = (600, 330)
kivy04().run()