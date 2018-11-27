from objects.base.object import Object

class LivingOrganism(Object):
    def __init__(self, **kwargs):
        super(LivingOrganism, self).__init__(**kwargs)
        self._domain = None
        self._kingdom = None
        self._phylum = None
        self._class = None
        self._order = None
        self._family = None
        self._genus = None
        self._species = None

