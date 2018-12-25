# config: utf-8

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView


Window.size = (320, 240)
root = ScrollView(bar_width=10)

# create BoxLayout
bx = BoxLayout(orientation='vertical',
               size_hint=(None, None),
               size=(1040, 1500))

# create button(A0-Z49)
al = [chr(i) for i in range(65, 65+26)]
# create button array(0-49 raw)
for m in range(50):
    bx2 = BoxLayout(orientation='horizontal')
    # create button_array(An-Zn column)
    for n in al:
        # create button(size 40*30)
        bx2.add_widget(Button(text=n+str(m), font_size=12,
                              size_hint=(None, None), size=(40, 30)))
    bx.add_widget(bx2)
root.add_widget(bx)


class kivy06(App):
    def build(self):
        return root


kivy06().run()