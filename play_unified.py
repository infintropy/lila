from __future__ import print_function
import os
import sys
import uuid
import datetime
from operator import itemgetter
from itertools import groupby
import pprint
import yaml

"""
1. Existence (Witness)
2.  Entropy - 
3.  Novelty + 
4. Reality 
5.  Macro-Entropy
6.  Metanovelty

Event
Project







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
        self._category = "Unknown"
        self._links = []

        self.save_info = ["_x", "_y", "_z", "_created", "_name", "id", "_category", "_relation", "_realm", "_location"]


        self._x = 0
        self._y = 0
        self._z = 0

        self._created = datetime.datetime.now()


        if name:
            self._name = name

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

    @property
    def category(self):
        return self._category

    @property
    def links(self):
        pass

    @links.setter
    def links(self, link):
        pass


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

        self._minute_increments = 15 #minutes
        self._multiplier = 60 / self._minute_increments
        self._day_range = set(xrange(0, 24*(60/self._minute_increments)))
        self._responsibility_minimum = 2 #hours

        self._day_attributions = {}

        self._sleep_event = Event(name="SleepyTime")
        self._hygiene_event = Event(name="Bathroom")
        self._exercise_event = Event(name="Exercise")





        self._rest = []
        self._work = []
        self._project = []
        self._family = []
        self._core = []
        self._travel = []

        self._events = []
        self._tasks = []

        self._periods = {"rest"    : [(0, 5.5)],
                         "work"    : [(9.5,13), (14,18.5)],
                         "project" : [(22,24)],
                         "family"  : [(6.5,8.5),(19,22)],
                         "core"    : [(5.5,6.5)],
                         "travel"  : [(9.25,9.5), (18.5,18.75)]
                         }


        self.save_info.extend( ["_periods", "_minute_increments" ] )

    @property
    def events(self):
        return self._events

    def add_event(self, name, type=None):

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

    def reset_day_expectations(self):
        self._day_range = set(xrange(0, 24 * (60 / self._minute_increments)))

    def request(self, start, end, event=None):
        request = set(xrange(int(start*self._multiplier), int(end*self._multiplier) ) )
        req_bool = True
        unavailable_time = []
        for i in request:
            if i not in self._day_range:
                req_bool = False
                unavailable_time.append( i )
        if req_bool == True:
            self._day_range -= set(xrange(int(start*self._multiplier), int(end*self._multiplier) ) )
            if not event:
                event = Event(name="Event")
            for i in request:
                self._day_attributions[i] = event.id
        else:
            print( "Looks like you dont have time to grant this request. The following hours were unavailable within your request: [%s]" %(", ".join(sorted([str(i) for i in unavailable_time]))) )


    def map_reservations(self):
        unique_events = sorted(list(set([v for i,v in self._day_attributions.iteritems()])))
        return dict((e, self.group_time([k for k,v in self._day_attributions.iteritems() if v == e])) for e in unique_events)

    def lookup_group_entity(self, hour):
        try:
            print(nog.inf[self._day_attributions[hour]].name)
            return [l for l in [[i for i in v if hour in i] for k,v in self.map_reservations().iteritems() ] if l !=[]][0][0]
        except:
            return None


    def group_time(self, list):
        periods = []
        for k, g in groupby(enumerate(sorted(list)), lambda (i, x): i - x):
            e = map(itemgetter(1), g)
            periods.append(e)
        return periods

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

    def group_range(self):
        free_periods = []
        data = self._day_range
        for k, g in groupby(enumerate(data), lambda (i, x): i - x):
            e = map(itemgetter(1), g)
            free_periods.append(e)
        pout = []
        for period in free_periods:
            b = "%s-%s (%d minutes)" % (self.timeslot_to_hour(period[0]), self.timeslot_to_hour(period[-1] + 1), len(period) * self.increment)
            pout.append( b )
        return pout

    def free(self):
        free_periods = []
        data = self._day_range
        for k, g in groupby(enumerate(data), lambda (i, x): i - x):
            e = map(itemgetter(1), g)
            free_periods.append(e)
        print( "There are %d free points of time in your day." %len(free_periods) )
        for period in free_periods:
            print("%s-%s (%d minutes) " %(self.timeslot_to_hour( period[0]),  self.timeslot_to_hour( period[-1]+1), len(period)*self.increment ))

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


    def test_day(self):
        self.request( 2,7, self._sleep_event )
        self.request( 7,8, self._hygiene_event )


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
        self._length = 60 #minutes
        self._category = "Default"
        self._hour_start = 0.0


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
        self.planner.category = "My Planner"



class Family(Group):

    def __init__(self, **kwargs):
        super(Family, self).__init__( realm=nog, **kwargs)



############################################################
############################################################

class Recipe(Group):
    def __init__(self, **kwargs):
        super(Recipe, self).__init__( realm=nog, **kwargs)


class FoodJournal(Group):
    def __init__(self, **kwargs):
        super(FoodJournal, self).__init__( realm=nog, **kwargs)

