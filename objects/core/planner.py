
from __future__ import print_function
from operator import itemgetter
from itertools import groupby

#main boilerplate for making an object
from objects.base.object import Object
from objects.core.event import Event


class Planner(Object):
    def __init__(self, **kwargs):
        super(Planner, self).__init__(**kwargs)

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