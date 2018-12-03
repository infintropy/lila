from objects.base.object import Object


class FoodItem(Object):
    def __init__(self, **kwargs):
        super(FoodItem, self).__init__(**kwargs)

        self._calories = 0
        self._protein = 0
        self._fat = 0
