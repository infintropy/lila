from objects.base.group import Group
from objects.irl.food import *

class Recipe(Group):
    def __init__(self, **kwargs):
        super(Recipe, self).__init__(**kwargs)

class FoodJournal(Group):
    def __init__(self, **kwargs):
        super(FoodJournal, self).__init__(**kwargs)

