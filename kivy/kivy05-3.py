# config: utf-8

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem


class kivy05(App):
    def build(self):
        return root


# Tab panel
root = TabbedPanel()
root.do_default_tab = False
# Tab1
tb_item1 = TabbedPanelItem(text='Tab1')
lb1 = Label(text='Tab 1')
tb_item1.add_widget(lb1)
root.add_widget(tb_item1)
# Tab2
tb_item2 = TabbedPanelItem(text='Tab2')
lb2 = Label(text='Tab 2')
tb_item2.add_widget(lb2)
root.add_widget(tb_item2)

root.default_tab = tb_item1

Window.size = (300, 150)
ap = kivy05()
ap.run()