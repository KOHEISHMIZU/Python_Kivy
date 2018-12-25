# config: utf-8

from kivy.app import App
from kivy.config import Config
from kivy.core.window import Window
from kivy.graphics import Color, Fbo, Rectangle
from kivy.uix.widget import Widget
Config.set('graphics', 'resizable', False)


class kivy04(App):
    def build(self):
        return root


root = Widget()

# create frame buffer and register Canvas
fb = Fbo(size=(300, 150))
root.canvas.add(fb)

# draw frame buffer
fb.add(Color(1, 0, 0, 1))
fb.add(Rectangle(pos=(0, 0), size=(100, 150)))
fb.add(Color(0, 1, 0, 1))
fb.add(Rectangle(pos=(100, 0), size=(100, 150)))
fb.add(Color(0, 0, 1, 1))
fb.add(Rectangle(pos=(200, 0), size=(200, 150)))
fb.add(Color(1, 1, 1, 1))
fb.add(Rectangle(pos=(0, 75), size=(300, 75)))
# draw Canvas
root.canvas.add(Rectangle(size=(300, 150), texture=fb.texture))


# get color value
def pick_color(self, t):
    # get window size
    (win_width, win_height) = Window.size
    # get touched_coordinate
    (touch_x, touch_y) = t.spos
    # frame buffer coordinate
    frame_buf_x = int(win_width * touch_x)
    frame_buf_y = int(win_height * touch_y)
    # get pixel on frame buffer coordinate
    pixel_value = fb.get_pixel_color(frame_buf_x, frame_buf_y)
    print('位置:\t', (frame_buf_y, frame_buf_x), '\tピクセル:', pixel_value)


root.bind(on_touch_up=pick_color)

Window.size = (300, 150)
kivy04().run()