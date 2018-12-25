# config: utf-8

from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.core.window import Window


# create top layout
root = AnchorLayout()

# create button
btn1 = Button(text='Delete This Button!')


# Function to remove button from top layout
def delete_btn(self):
    root.remove_widget(btn1)


btn1.bind(on_release=delete_btn)

# Register btn
root.add_widget(btn1)


class kivy07(App):
    def build(self):
        return root


Window.size = (250, 50)
kivy07().run()