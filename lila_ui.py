import kivy
import random

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.treeview import TreeView, TreeViewLabel
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.accordion import Accordion, AccordionItem
from kivy.uix.listview import ListView
from kivy.uix.label import Label

red = [1,0,0,1]
green = [0,1,0,1]
blue =  [0,0,1,1]
purple = [1,0,1,1]






class MainView(ListView):
    def __init__(self, **kwargs):
        super(MainView, self).__init__(
            item_strings=[str(index) for index in range(50)])

########################################################################
class NestedLayoutExample(App):
    """
    An example of nesting three horizontally oriented BoxLayouts inside
    of one vertically oriented BoxLayout
    """

    #----------------------------------------------------------------------
    def build(self):
        """
        Horizontal BoxLayout example
        """
        root = Accordion(orientation="horizontal")
        for x in range(3):
            ly = BoxLayout(padding=10)

            item = AccordionItem(title='Derp %d' % x)
            item.add_widget( ly )
            root.add_widget(item)
        return root
        """
        
        self.dropdown = MainView()

        main_layout = BoxLayout(padding=10, orientation="horizontal")
        tlayout = BoxLayout(padding=10, orientation="horizontal")
        colors = [red, green, blue, purple]
        self.tv = TreeView()

        a1 = self.tv.add_node(TreeViewLabel(text='My first item22222'))
        a2 = self.tv.add_node(TreeViewLabel(text='My second item'), a1)
        a3 = self.tv.add_node(TreeViewLabel(text="Derp!"), a2)

        tlayout2 = BoxLayout(padding=10, orientation="horizontal")
        colors = [red, green, blue, purple]
        self.tv2 = TreeView()

        a1b = self.tv2.add_node(TreeViewLabel(text='My first item'))
        a2b = self.tv2.add_node(TreeViewLabel(text='My second item'), a1b)
        a3b = self.tv2.add_node(TreeViewLabel(text="Derp!"), a2b)

        tlayout.add_widget( self.dropdown )
        tlayout.add_widget(self.tv)
        tlayout.add_widget(self.tv2)

        main_layout.add_widget(tlayout)


        return main_layout
        """

#----------------------------------------------------------------------
if __name__ == "__main__":
    app = NestedLayoutExample()
    app.run()