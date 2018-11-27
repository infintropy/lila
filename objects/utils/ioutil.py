
from __future__ import print_function
import datetime
import sys
import yaml
import os
import tempfile


class IOUtil(object):
    def __init__(self):

        self._record_base = os.path.join(tempfile.gettempdir(), "%s_%s.lla")
        self.day = datetime.datetime.now().strftime( "%Y%m%d" )

    def write(self, filename, data):
        with open(self.record_base %(self.day, filename), 'w') as outfile:
            yaml.dump(data, outfile, default_flow_style=False)

    def logs(self):
        pass

    @property
    def record_base(self):
        return self._record_base

