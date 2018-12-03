from objects.base.object import Object

class Place(Object):
    def __init__(self, **kwargs):
        super(Place, self).__init__(**kwargs)

        self._phone_number = 0

