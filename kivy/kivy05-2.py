# config: utf-8

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.actionbar import ActionBar, ActionView, ActionPrevious, \
                                            ActionGroup, ActionButton
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput


class kivy05(App):
    def build(self):
        return root


Window.size = (400, 200)

root = BoxLayout(orientation='vertical')

txt = TextInput()

# action bar
AcBar = ActionBar()
AcView = ActionView()
AcPrev = ActionPrevious(title='Thr Action bar')
AcGrp = ActionGroup(text='Buttons', mode='spinner')
AcBtn1 = ActionButton(text='Button_1')
AcBtn2 = ActionButton(text='Button_2')
AcBtn3 = ActionButton(text='Button_3')

# make
root.add_widget(txt)
AcGrp.add_widget(AcBtn1)
AcGrp.add_widget(AcBtn2)
AcGrp.add_widget(AcBtn3)
AcView.add_widget(AcGrp)
AcView.add_widget(AcPrev)
AcBar.add_widget(AcView)
root.add_widget(AcBar)


# callback_function
def callback1(self):
    txt.text = 'Button_1 is clicked'


def callback2(self):
    txt.text = 'Button_2 is clicked'


def callback3(self):
    txt.text = 'Button_3 is clicked'


AcBtn1.bind(on_release=callback1)
AcBtn2.bind(on_release=callback2)
AcBtn3.bind(on_release=callback3)

ap = kivy05()
ap.run()