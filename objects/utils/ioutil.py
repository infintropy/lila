
from __future__ import print_function
import datetime

import yaml


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

