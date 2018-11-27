from objects.base.object import Object

class Group(Object):
    def __init__(self, **kwargs):
        super(Group, self).__init__(**kwargs)
        self._objects = []

    @property
    def objects(self):
        return self._objects

    def add(self, object):
        self._objects.append( object )
