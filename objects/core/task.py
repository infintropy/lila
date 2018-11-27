
from objects.core.event import Event

class Task(Event):
    def __init__(self, **kwargs):
        super(Task, self).__init__(**kwargs)
        self._complete = False
        self._assigned_to = None
        self._level = 0
        self._required = False

    @property
    def complete(self):
        return self._complete

    @complete.setter
    def complete(self, val):
        if type(val) == type(True):
            self._complete = val
        else:
            raise TypeError("Must use a boolean type to set Task's completion")

    def remind(self):
        pass


