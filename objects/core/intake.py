from objects.base.group import Group


class Recipe(Group):
    def __init__(self, **kwargs):
        super(Recipe, self).__init__(**kwargs)

class FoodJournal(Group):
    def __init__(self, **kwargs):
        super(FoodJournal, self).__init__(**kwargs)

