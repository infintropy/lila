from objects.base.object import Object

class JournalEntry(Object):
    def __init__(self, **kwargs):
        super(JournalEntry, self).__init__(**kwargs)

class Journal(Object):
    def __init__(self, **kwargs):
        super(Journal, self).__init__(**kwargs)

    def write(self, msg):
        r = JournalEntry()
        r.category = msg

        self.add_link( r )