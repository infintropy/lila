
from __future__ import print_function
import uuid
import datetime
import pprint
from objects.base.realm import Realm

global nog
nog = Realm()


class Object(object):
    def __init__(self, name=None):
        self._parent = None
        self._realm = None
        self._name = None
        self.id = str(uuid.uuid4())
        self._relation = "_val"
        self._unique_class = None
        self._val = 0
        self._category = "Unknown"
        self._links = []

        self.save_info = ["_x", "_y", "_z", "_created", "_name", "id", "_category", "_relation", "_realm", "_location"]

        self._x = 0
        self._y = 0
        self._z = 0

        self._created = datetime.datetime.now()




        self._realm = nog

        if name:
            self._name = name
        else:
            self._name = self.autoname()


        methere = self._realm.reify(self)
        return methere


    def __repr__(self):
        ext = ""
        if self._name:
            ext = " NAME:: %s" %self._name
        return "%s:: ID: %s. %s" %(self.__class__.__name__, self.id, ext)

    def __str__(self):
        return self.__repr__()

    def __lt__(self, other):
        return getattr(self, self._relation) < getattr(other, self._relation)

    def __eq__(self, other):
        return getattr(self, self._relation) == getattr(other, self._relation)

    @property
    def type(self):
        return self.__class__.__name__

    @property
    def relation(self):
        return self._relation

    @relation.setter
    def relation(self, val):
        if type(val) == str:
            self._relation = val

    @property
    def realm(self):
        return self._realm

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def location(self):
        if self._location:
            return self._location

    @property
    def category(self):
        return self._category

    @property
    def links(self):
        pass

    @links.setter
    def links(self, link):
        pass

    def autoname(self):
        ind = 1
        if self.realm._class.get( self.__class__.__name__ ):
            ind = len(self.realm._class[self.__class__.__name__])+1
        return self.__class__.__name__ + "%d" %ind


    @category.setter
    def category(self, category):
        self._category = category
        if self._category in self.realm.class_categories( self.__class__.__name__ ):
            print("There are others with this category!")

    @location.setter
    def location(self, location):
        if location.type == "Location":
            self._location = location

    def created(self):
        return self._created

    def serialize(self):
        s_obj = {}
        for i in self.save_info:
            if hasattr(self, i):
                a2d = getattr(self, i)
                if hasattr(a2d, "id"):
                    s_obj[i] = a2d.id
                else:
                    s_obj[i] = a2d
        s_obj['name'] = self.name
        s_obj['class'] = self.__class__.__name__
        return s_obj

    def describe(self):
        pprint.pprint( self.serialize() )


