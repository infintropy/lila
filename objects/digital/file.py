from objects.base.object import Object

class File(Object):
    def __init__(self, **kwargs):
        super(File, self).__init__(**kwargs)
        self._path = None
        self._extension

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, path):
        self._path = path
