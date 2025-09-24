import random

class Ultrasonic:
    def __init__(self):
        self.distance = None
    
    def getDistance(self):
        self.distance = random.randint(10,200)
        return self.distance