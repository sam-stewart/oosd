class Bicycle(object):

    def __init__(self):
        self.observers = []
        self.rpms = 0

    @property
    def rpms(self):
        return _rpms

    @rpms.setter
    def rpms(self, value):
        self._rpms = value
        self.notify_observers()
        
    def add_observer(self, o):
        self.observers.append(o)

    def remove_observer(self, o):
        self.observers.remove(o)

    def notify_observers(self):
        for o in self.observers:
            o.update(self._rpms)
