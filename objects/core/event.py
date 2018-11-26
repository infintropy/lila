from objects.base.object import Object
from objects.utils.ghosts import nog


class Event(Object):
    def __init__(self, start=None, **kwargs):
        super(Event, self).__init__(realm=nog, **kwargs)

        self._description = ""
        self._length = 60 #minutes
        self._category = "Default"
        self._hour_start = 0.0


    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, time):
        if time in [15, 30, 60, 120, 240]:
            self._length = time
