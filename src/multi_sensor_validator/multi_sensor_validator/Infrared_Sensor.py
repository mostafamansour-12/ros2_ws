import random

class Infrared:
    def __init__(self):
        self.distance = None
    
    def getDistance(self):
        self.distance = random.randint(10,200)
        return self.distance