class LightState(object):
    def switch(self):
        raise NotImplementedError("")

class OnState(LightState):
   
    def switch(self):
        return OffState()

    def __str__(self):
        return "Light is bright"

class OffState(LightState):

    def switch(self):
        return OnState()

    def __str__(self):
        return "Light is dark"
