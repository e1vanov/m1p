from general import Encoder
import random
import numpy as np

class Dummy(Encoder):

    def __init__(self, n, k):

        super().__init__(n, k)
        self.cnt = 0

    def __next__(self):

        if self.cnt >= self.n:
            raise StopIteration

        ind = self.cnt
        self.cnt += 1

        return [ind % self.k]


class All_At_Once(Encoder):

    def __init__(self, n, k):

        super().__init__(n, k)
        self.cnt = 0
        
    def __next__(self):

        if self.cnt >= self.n:
            raise StopIteration

        self.cnt += 1
        return [random.randint(0, self.k - 1)]
