class Speedometer(object):

    def __init__(self, subject):
        self.subject = subject
        self.wheel_circum = 205
        subject.add_observer(self)

    def update(self, rpms):
        self.speed = 60 * ((rpms * self.wheel_circum) / 100000.0)
