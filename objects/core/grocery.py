from objects.irl.food import *
from objects.base.object import Object
from objects.base.place import Place

class GroceryList(Object):
    def __init__(self, **kwargs):
        super(GroceryList, self).__init__(**kwargs)


class GroceryStore(Place):
    def __init__(self, **kwargs):
        super(GroceryStore, self).__init__(**kwargs)


