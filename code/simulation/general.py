class DataTransmission:

    def __init__(self, n, k, encoder, channel, decoder, verbose=False):

        self.n = n
        self.k = k
        self.encoder = encoder
        self.channel = channel
        self.decoder = decoder
        self.verbose = verbose

    def __call__(self, data=None):

        symbols = list(self.encoder)
        if self.verbose:
            print(symbols)

        transmitted_symbols = [ symbol for symbol in symbols if self.channel(symbol) is not None ]
        if self.verbose:
            print(transmitted_symbols)

        return self.decoder(transmitted_symbols)


class Encoder:

    def __init__(self, n, k):

        self.k = k
        self.n = n

    def __iter__(self):
        
        return self

    def __next__(self):

        pass


class Channel:

    def __init__(self):

        pass
    
    def __call__(self, entity):

        pass


class Symbol:

    def __init__(self, data, ind):

        self.data = data
        self.ind = ind


class Decoder:

    def __init__(self, k):

        self.k = k

        pass

    def __call__(self, symbols):

        pass
