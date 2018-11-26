from objects.base.object import Object
from objects.utils.ghosts import nog

class Group(Object):
    def __init__(self, **kwargs):
        super(Group, self).__init__(realm=nog, **kwargs)
        self._objects = []

    @property
    def objects(self):
        return self._objects

    def add(self, object):
        self._objects.append( object )
        print "HELL YEAH!!!"