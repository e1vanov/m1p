import random
from general import Channel

class BEC(Channel):

    def __init__(self, p):

        self.p = p

    def __call__(self, entity):

        return entity if random.uniform(0., 1.) > self.p else None
