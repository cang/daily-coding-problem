'''
This problem was asked by Twitter.
You run an e-commerce website and want to record the last N order ids in a log. Implement a data structure to accomplish this, with the following API:

record(order_id): adds the order_id to the log get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N. You should be as efficient with time and space as possible.
'''

class LogN:
    def __init__(self,logsize):
        self.logsize = logsize
        self.buffer = [None]*self.logsize
        self.lastidx=0

    def record(self,order_id):
        self.buffer[self.lastidx]=order_id
        self.lastidx= (self.lastidx+1)%self.logsize

    def get_last(self,i):
        idx = (self.lastidx - i + self.logsize)%self.logsize
        return self.buffer[idx]

    def records(self,orders):
        for x in orders:
            self.record(x)

logn = LogN(5)
logn.records([1,2,3,4,5,6,7,8,9,10])
assert logn.get_last(2)==9
