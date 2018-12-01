from __future__ import print_function
import sys
import inspect

#import base modules
from objects.base.object import *
from objects.base.group import *

from objects.core.planner import *
from objects.core.event import *
from objects.core.task import *

#let there be mind
from objects.base.object import nog

#let there be me
from objects.irl.me import *

#let there be important items
from objects.core.intake import *
from objects.core.journal import *
from objects.core.budget import *

#digital bits
from objects.digital.file import *

#create reality
global o
o = nog

#create experiencer
global me
me = Me()

for name, obj in inspect.getmembers(sys.modules[__name__]):
    if inspect.isclass(obj):
        if issubclass(obj, Object):
            setattr(o, name, obj)

