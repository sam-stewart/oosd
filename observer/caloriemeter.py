class CalorieMeter(object):

    def __init__(self, subject):
        self.subject = subject
        self.calories = 0
        subject.add_observer(self)

    def update(self, rpms):
        self.calories = 3 * rpms
