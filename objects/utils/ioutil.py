
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

    def update_table(self, object):
        table = self.get_table(object)
        if not table:
            #make a new db
            self._db[object.type] = TinyDB(os.path.join( self.record_base, "_lila_rec_%s.lla" %object.type ))
            table = self._db[object.type]
        table.upsert(object.serialize(), rec.id == object.id)

    def get_table(self, type):
        path = os.path.join( self.record_base, "_lila_rec_%s.lla" %type )
        if os.path.isfile( path ):
            return self._db[type]
        else:
            print("no table for %s found" %type)

    def logs(self):
        pass



    @property
    def record_base(self):
        return self._record_base

