from time import time
class RandomObject:
    def __init__(self):
        self.index=1
        self.state=[None]*624
        self.state[0]=int(time())&4294967295
        while self.index<624:
            self.state[self.index]=(1812433253*(self.state[self.index-1]^(self.state[self.index-1]>>30))+self.index)&4294967295
            self.index=self.index+1
    def seed(self,a):
        assert type(a)==int,"seed must be a int"
        self.index=1
        self.state=[None]*624
        self.state[0]=a&4294967295
        while self.index<624:
            self.state[self.index]=(1812433253*(self.state[self.index-1]^(self.state[self.index-1]>>30))+self.index)&4294967295
            self.index=self.index+1
    def int32(self):
        a=0
        if 624<=self.index:
            b=0
            while b<227:
                a=(self.state[b]&2147483648)|(self.state[b+1]&2147483647)
                self.state[b]=self.state[b+397]^(a>>1)^((a&1)*2567483615)
                b=b+1
            while b<623:
                a=(self.state[b]&2147483648)|(self.state[b+1]&2147483647)
                self.state[b]=self.state[b-227]^(a>>1)^((a&1)*2567483615)
                b=b+1
            a=(self.state[623]&2147483648)|(self.state[0]&2147483647)
            self.state[623]=self.state[396]^(a>>1)^((a&1)*2567483615)
            self.index=1
            return self.state[self.index]^(a>>11)^((a<<7)&2636928640)^((a<<15)&4022730752)^(a>>18)
        self.index=self.index+1
        return self.state[self.index]^(a>>11)^((a<<7)&2636928640)^((a<<15)&4022730752)^(a>>18)
    random=lambda self:((self.int32()>>5)*67108864+(self.int32()>>6))/9007199254740992.0