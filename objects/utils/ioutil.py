
from __future__ import print_function
import datetime
import sys
import yaml
import os
import tempfile
from tinydb import TinyDB, Query

rec = Query()

class IOUtil(object):
    def __init__(self):

        self._db = {}
        self._record_base = tempfile.gettempdir()
        self.day = datetime.datetime.now().strftime( "%Y%m%d" )


        self.map_tables()

    def update_table(self, object):
        table = self.get_table(object)
        if not table:
            self._db[object.type] = TinyDB(os.path.join( self.record_base, "_lila_rec_%s.lla" %object.type ))
            table = self._db[object.type]
        table.upsert(object.serialize(), rec.id == object.id)

    def get_table(self, object):
        path = os.path.join( self.record_base, "_lila_rec_%s.lla" %object.type )
        if os.path.isfile( path ):
            if not self._db.get( object.type ):
                self._db[object.type] = TinyDB(os.path.join( self.record_base, "_lila_rec_%s.lla" %object.type ))
            return self._db[object.type]
        else:
            print("no table for %s found" %object.type)

    @property
    #returns all lila dbs kept in temp.
    def dbs(self):
        return sorted([i for i in os.listdir( self.record_base ) if i.startswith("_lila_rec_")])

    def map_tables(self):
        for table in self.dbs:
            dbname = table.split("_rec_")[-1].split('.')[0]
            self._db[dbname] = TinyDB(os.path.join(self.record_base, table))

    def logs(self):
        pass

    def entity_from_record(self, id, cls):
        pass


    @property
    def record_base(self):
        return self._record_base






