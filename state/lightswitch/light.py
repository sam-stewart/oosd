import states

class Light(object):
    
    def __init__(self):
        self.state = states.OffState()

    def switch(self):
        self.state = self.state.switch()

    def show_state(self):
        return self.state
