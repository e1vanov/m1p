from general import Encoder
import random
import numpy as np

class Systematic_Encoder(Encoder):

    def __init__(self, n, k):

        self.k = k
        self.n = n
        self.cnt = 0

    def generate(self):

        pass

    def __next__(self):

        if self.cnt >= self.n:
            raise StopIteration

        if self.cnt < self.k:
            ind = self.cnt
            self.cnt += 1
            return [ind]
        
        self.cnt += 1

        return self.generate()


class Systematic_Poisson(Systematic_Encoder):

    def __init__(self, n, k, Lambda):

        super().__init__(n, k)
        self.Lambda = Lambda

    def generate(self):

        d = np.random.poisson(self.Lambda) + 1
        if d > self.k:
            d = self.k

        return list(np.random.choice(self.k, d, replace=False))


class Systematic_Binomial(Systematic_Encoder):

    def __init__(self, n, k, p):

        super().__init__(n, k)
        self.p = p
        
    def generate(self):

        d = np.random.binomial(self.k, self.p)

        return list(np.random.choice(self.k, d, replace=False))


class Systematic_All_At_D(Systematic_Encoder):

    def __init__(self, n, k, d):

        super().__init__(n, k)
        self.d = d

    def generate(self):

        return list(np.random.choice(self.k, self.d, replace=False))
