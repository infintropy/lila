
from objects.base.group import Group

class Family(Group):

    def __init__(self, **kwargs):
        super(Family, self).__init__( realm=nog, **kwargs)