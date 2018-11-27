from objects.irl.organism import LivingOrganism

class Human(LivingOrganism):
    def __init__(self, **kwargs):
        super(Human, self).__init__(**kwargs)

        self._domain =   "Eukarya"
        self._kingdom =  "Animalia"
        self._phylum =   "Chordata"
        self._class =    "Mammalia"
        self._order =    "Primates"
        self._family =   "Hominidae"
        self._genus =    "Homo"
        self._species =  "sapiens"

        #relation
        self._height_cm = 0
        self._height_in = 0
        self._weight_kg = 0
        self._weight_lb = 0


    @property
    def height(self):
        return self._height_in

    @height.setter
    def height(self, value):
        self._height_in = float(value)
        self._height_cm = float(value)*2.54
