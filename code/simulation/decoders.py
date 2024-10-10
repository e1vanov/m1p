from general import Decoder

class TunnerGraph():

    def __init__(self, k, symbols):

        self.k = k

        self.edges = {
                         'packet' : [ [] for _ in range(self.k) ], 
                         'symbol' : [ [] for _ in range(len(symbols)) ] 
                     }

        for i, symbol in enumerate(symbols):
            for packet in symbol:

                self.edges['packet'][packet].append(i)
                self.edges['symbol'][i].append(packet)

    def decode(self):

        ripple = [ i for i, symbol in enumerate(self.edges['symbol']) if len(symbol) == 1 ]
        decoded = [ False ] * self.k
        
        while len(ripple):

            curr_symbol = ripple[0]

            if len(self.edges['symbol'][curr_symbol]) == 0:
                ripple = ripple[1:]
                continue

            curr_packet = self.edges['symbol'][curr_symbol][0]
            
            if not decoded[curr_packet]:

                decoded[curr_packet] = True

                for symbol in self.edges['packet'][curr_packet]:

                    self.edges['symbol'][symbol].remove(curr_packet)

                    if len(self.edges['symbol'][symbol]) == 1:
                        ripple.append(symbol)

                self.edges['packet'][curr_packet] = []

            self.edges['symbol'][curr_symbol] = []
            ripple = ripple[1:]

        ans = 0
        for el in decoded:
            ans += int(el)

        return ans
            

class LT(Decoder):

    def __init__(self, k):

        super().__init__(k)

    def __call__(self, symbols):

        tunner_graph = TunnerGraph(self.k, symbols)
        return tunner_graph.decode()
        

class OnGoing(Decoder):

    def __init__(self, k):

        super().__init__(k)

    def __call__(self, symbols):

        decoded = [ False ] * self.k

        for symbol in symbols:

            already_decoded = 0
            for packet in symbol:
                already_decoded += decoded[packet]

            if len(symbol) - already_decoded == 1:

                for packet in symbol:
                    decoded[packet] = True

        ans = 0
        for el in decoded:
            ans += int(el)

        return ans
