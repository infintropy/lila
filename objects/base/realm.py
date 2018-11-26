
from __future__ import print_function

import uuid
from objects.utils.ioutil import IOUtil



class Realm(object):
    """
    This is where an object can be exhibited
    """

    def __init__(self):
        self._description = None
        self.inf = {} #collects it all
        self.id = str(uuid.uuid4())
        self.io = IOUtil()

        self._unique_classes = ["Me"]
        self._class = {}

    def __repr__(self):
        return "Realm: %s, containing %d objects.\n" %(self.__class__, len(self.inf.keys())) + "\n".join([str(v) for k,v in self.inf.iteritems()])

    def __str__(self):
        return self.id

    def reify(self, object):
        first = None
        make = None
        if object.__class__.__name__ not in self._class.keys():
            self._class[ object.__class__.__name__ ] = []
            first = True
            print('this is the first one of these made:: %s' %object.__class__.__name__)

        if object.__class__.__name__ in self._unique_classes:
            print("This is being called out as a unique class")
            if first:
                make = True
            else:
                make = False
                raise UniqueObjectException("You cannot create more than one %s class." %(object.__class__.__name__) )

        else:
            make = True
        if make is True:
            self.inf[object.id] = object
            self._class[object.__class__.__name__].append( object.id )
            print(self.inf[object.id])
            self.serialize()

            return self.inf[object.id]



    def class_categories(self, classname=None):
        if classname:
            return sorted(list(set([self.inf[f].category for f in self._class[classname]])))
        else:
            return sorted(list(set([v.category for i,v in self.inf.iteritems()])))

    def get_objects_from_category(self, category):
        return [v for i,v in self.inf.iteritems() if v.category == category]

    def serialize(self):
        sout = []
        for i, o in self.inf.iteritems():
            sout.append( o.serialize() )
        self.io.write( self.__class__.__name__.lower(), sout )
        return sout

