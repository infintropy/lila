from __future__ import print_function
import os
import sys
import uuid
import datetime
from operator import itemgetter
from itertools import groupby
"""
1.  Existence (Witness)
2.  Entropy - 
3.  Novelty + 
4.  Reality 
5.  Macro-Entropy
6.  Metanovelty
"""

class UniqueObjectException(Exception):
    pass

class Object(object):
    def __init__(self, realm=None, name=None):
        self._parent = None
        self._realm = None
        self._name = None
        self.id = str(uuid.uuid4())
        self._relation = "_val"
        self._unique_class = None
        self._val = 0

        self._x = 0
        self._y = 0
        self._z = 0

        self._created = datetime.datetime.now()


        if name:
            self._name = name
        else:
            self._name = self.__class__.__name__

        if realm:
            self._realm = realm
            self.__repr__()
            methere = self._realm.reify(self)
            return methere


    def __repr__(self):
        ext = ""
        if self._name:
            ext = " NAME:: %s" %self._name
        return "%s:: ID: %s. Living inside %s%s" %(self.__class__.__name__, self.id, self._realm.__class__.__name__, ext)

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

    @location.setter
    def location(self, location):
        if location.type == "Location":
            self._location = location

    def created(self):
        return self._created



class Group(Object):
    def __init__(self, **kwargs):
        super(Group, self).__init__(realm=nog, **kwargs)
        self._objects = []

    @property
    def objects(self):
        return self._objects

    def add(self, object):
        self._objects.append( object )







class Realm(object):
    """
    This is where an object can be exhibited
    """

    def __init__(self):
        self._description = None
        self.inf = {}
        self._contains_classes = []
        self._unique_classes = ["Me"]

    def __repr__(self):
        return "Realm: %s, containing %d objects.\n" %(self.__class__, len(self.inf.keys())) + "\n".join([str(v) for k,v in self.inf.iteritems()])

    def reify(self, object):
        first = None
        make = None
        if object.__class__.__name__ not in self._contains_classes:
            self._contains_classes.append(object.__class__.__name__)
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
            print(self.inf[object.id])
            return self.inf[object.id]

    def next_class_index(self, classname):
        len()

    def get_all(self, classname):
        return [v for k,v in self.inf.iteritems() if v.__class__.__name__ == classname]







class Noggin(Realm):
    def __init__(self):
        super(Noggin, self).__init__()
        self._description = "An entirely mental realm"



class Universe(Realm):
    def __init__(self):
        super(Universe, self).__init__()
        self._description = "Physical existence as we know it"

    @classmethod
    def egocentric(cls):
        me = Me()
        return cls


#############################################################
##############################################################
# Let there be light
global uni
global nog

uni = Universe()
nog = Noggin()








class Planner(Object):
    def __init__(self, **kwargs):
        super(Planner, self).__init__(realm=nog, **kwargs)

        self._minute_increments = 15
        self._multiplier = 60 / self._minute_increments
        self._day_range = set(xrange(0, 24*(60/self._minute_increments)))

        self._events = []
        self._tasks = []
        self._periods = {"rest"    : [(0, 5.5)],
                         "work"    : [(9.5,13), (14,18.5)],
                         "project" : [(22,24)],
                         "family"  : [(6.5,8.5),(19,22)],
                         "core"    : [(5.5,6.5)],
                         "travel"  : [(9.25,9.5), (18.5,18.75)]
                         }

    @property
    def events(self):
        return self._events

    def add_event(self, name):
        self._events.append( Event(name=name)  )

    @property
    def tasks(self):
        return self._tasks

    def add_task(self, name):
        self._tasks.append( Task(name=name)  )


    def hour_to_unit(self, hour):
        return hour*self._multiplier

    @property
    def increment(self):
        return self._minute_increments

    @increment.setter
    def increment(self, value):
        self._minute_increments = value
        self._multiplier = 60/self._minute_increments

    def request(self, tup):
        self._day_range -= set(xrange(int(tup[0]*self._multiplier), int(tup[1]*self._multiplier)))

    def reservations(self):
        for k,v in self._periods.iteritems():
            for i in v:
                self.request( i )

    def timeslot_to_hour(self, slot):
        periods = 24*(60/self._minute_increments)
        strtime = str((float(slot) / float( periods )) * 24)
        hour = float(strtime.split(".")[0])
        dec = float("0." + strtime.split(".")[1])
        return "%02d:%02d" %( int(hour), int(dec*60) )

    def free(self):
        free_periods = []
        data = self._day_range
        for k, g in groupby(enumerate(data), lambda (i, x): i - x):
            e = map(itemgetter(1), g)
            free_periods.append(e)
        print( "There are %d free points of time in your day." %len(free_periods) )
        for period in free_periods:
            print("%s-%s (%d minutes) " %(self.timeslot_to_hour( period[0]),  self.timeslot_to_hour( period[-1]+1), len(period)*self.increment ))

    def schedule(self):
        pass


    def analyze_day(self):
        day_total = 0.0
        for name, periods  in self._periods.iteritems():
            period_total = sum([i[1]-i[0] for i in periods])
            day_total += period_total
            print("%s: %.2f total hours" %( name, period_total))
        idle_total = 24.0 - day_total
        print("IDLE: %.2f total hours" %idle_total)


    def insert_event(self):
        pass






class Realigner(Planner):
    def __init__(self, **kwargs):
        super(Realigner, self).__init__(**kwargs)
        self._realign_time = []


    def set_realign_time(self, period):
        self._realign_time.append(period)


class Location(Object):
    def __init__(self, **kwargs):
        super(Location, self).__init__(realm=nog, **kwargs)



class Event(Object):
    def __init__(self, start=None, **kwargs):
        super(Event, self).__init__(realm=nog, **kwargs)

        self._description = ""
        self._length = 60

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, time):
        if time in [15, 30, 60, 120, 240]:
            self._length = time





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









class LivingOrganism(Object):
    def __init__(self, **kwargs):
        super(LivingOrganism, self).__init__(realm=uni, **kwargs)
        self._domain = None
        self._kingdom = None
        self._phylum = None
        self._class = None
        self._order = None
        self._family = None
        self._genus = None
        self._species = None


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

        self.noggin = nog



    @property
    def height(self):
        return self._height_in

    @height.setter
    def height(self, value):
        self._height_in = float(value)
        self._height_cm = float(value)*2.54






class Me(Human):

    def __init__(self, **kwargs):
        super(Me, self).__init__(**kwargs)
        self._name = 'Donald'
        self.height = 71

        self.planner = Planner()



class Family(Group):

    def __init__(self, **kwargs):
        super(Family, self).__init__( realm=nog, **kwargs)
