class User(object):

    def __init__(self):
        self.observers = []
        self.sent_messages = []
        self.observed_messages = []

    def post_message(self, msg):
        self.sent_messages.append(msg)
        self.notify_observers()
        
    def update(self, msg):
        self.observed_messages.append(msg)

    def add_observer(self, o):
        self.observers.append(o)

    def remove_observer(self, o):
        self.observers.remove(o)

    def notify_observers(self):
        for o in self.observers:
            # Update observers with last added message
            o.update(self.sent_messages[-1])


