# config: utf-8
#
# from kivy.app import App
# from kivy.core.window import Window
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.button import Button
# from kivy.uix.textinput import TextInput
#
#
# def func_button(self):
#     tx2.text = 'result: Button was touched'
#
#
# def func_text_input(self, v):
#     tx2.text = 'result: ' + self.text
#
#
# # GUI'vertical')
# root = BoxLayout(orientation='vertical')
# bt1 = Button(text='Button1')
# bt1.bind(on_release=func_button)
# tx1 = TextInput()
# tx1.bind(text=func_text_input)
# tx2 = TextInput()
# root.add_widget(bt1)
# root.add_widget(tx1)
# root.add_widget(tx2)
#
#
# class KivyKV01App(App):
#     def build(self):
#         return root
#
#
# Window.size = (300, 100)
# KivyKV01App().run()

############################
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout

# GUI
class RootW(BoxLayout):

    # callback function
    def func_button(self, tx2, t):
        tx2.text = 'result: Button1 was touched'

    def func_text_input(self, tx2, t):
        tx2.text = 'result: ' + t


class kivyKV01App(App):
    def build(self):
        return RootW()


Window.size = (300, 100)
kivyKV01App().run()