class User(object):

    def __init__(self):
        self.observers = []
        self.messages = []

    def update(self, msg):
        self.messages.append(msg)
        self.notify_observers()

    def add_observer(self, o):
        self.observers.append(o)

    def remove_observer(self, o):
        self.observers.remove(o)

    def notify_observers(self):
        for o in self.observers:
            # Update observers with last added message
            o.update(self.messages[-1])


