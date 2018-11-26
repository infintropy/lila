from __future__ import print_function
import os
import sys
import uuid
import datetime
from operator import itemgetter
from itertools import groupby
import pprint
import yaml

from objects.base.object import Object
from objects.base.group import Group
from objects.base.realm import Realm

from objects.core.planner import Planner


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

class IOUtil(object):
    def __init__(self):
        self.record_base = "C:/Users/dstrubler/Desktop/openlife/store/%s_%s.lla"
        self.record_base = "C:/Users/dstrubler/Desktop/openlife/store/%s_%s.lla"
        self.day = datetime.datetime.now().strftime( "%Y%m%d" )


    def write(self, filename, data):
        with open(self.record_base %(self.day, filename), 'w') as outfile:
            yaml.dump(data, outfile, default_flow_style=False)

    def logs(self):
        pass






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

