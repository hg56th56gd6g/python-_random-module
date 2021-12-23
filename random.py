from time import time
class RandomObject:
    def __init__(self):
        index=1
        state=[int(time())&4294967295]+[None]*623
        while index<624:
            state[index]=(1812433253*(state[index-1]^(state[index-1]>>30))+index)&4294967295
            index=index+1
    def seed(self,a):
        assert type(a)==int,"seed must be a int"
        index=1
        state=[a&4294967295]+[None]*623
        while index<624:
            state[index]=(1812433253*(state[index-1]^(state[index-1]>>30))+index)&4294967295
            index=index+1
    def int32(self):
        a=0
        if 624<=index:
            b=0
            while b<227:
                a=(state[b]&2147483648)|(state[b+1]&2147483647)
                state[b]=state[b+397]^(a>>1)^((a&1)*2567483615)
                b=b+1
            while b<623:
                a=(state[b]&2147483648)|(state[b+1]&2147483647)
                state[b]=state[b-227]^(a>>1)^((a&1)*2567483615)
                b=b+1
            a=(state[623]&2147483648)|(state[0]&2147483647)
            state[623]=state[396]^(a>>1)^((a&1)*2567483615)
            index=1
            return state[1]^(a>>11)^((a<<7)&2636928640)^((a<<15)&4022730752)^(a>>18)
        index=index+1
        return state[index]^(a>>11)^((a<<7)&2636928640)^((a<<15)&4022730752)^(a>>18)
    random=lambda self:((int32()>>5)*67108864+(int32()>>6))/9007199254740992.0
index=1
state=[int(time())&4294967295]+[None]*623
while index<624:
    state[index]=(1812433253*(state[index-1]^(state[index-1]>>30))+index)&4294967295
    index=index+1
def seed(a):
    assert type(a)==int,"seed must be a int"
    global index,state
    index=1
    state=[a&4294967295]+[None]*623
    while index<624:
        state[index]=(1812433253*(state[index-1]^(state[index-1]>>30))+index)&4294967295
        index=index+1
def int32():
    global index,state
    a=0
    if 624<=index:
        b=0
        while b<227:
            a=(state[b]&2147483648)|(state[b+1]&2147483647)
            state[b]=state[b+397]^(a>>1)^((a&1)*2567483615)
            b=b+1
        while b<623:
            a=(state[b]&2147483648)|(state[b+1]&2147483647)
            state[b]=state[b-227]^(a>>1)^((a&1)*2567483615)
            b=b+1
        a=(state[623]&2147483648)|(state[0]&2147483647)
        state[623]=state[396]^(a>>1)^((a&1)*2567483615)
        index=1
        return state[1]^(a>>11)^((a<<7)&2636928640)^((a<<15)&4022730752)^(a>>18)
    index=index+1
    return state[index]^(a>>11)^((a<<7)&2636928640)^((a<<15)&4022730752)^(a>>18)
random=lambda:((int32()>>5)*67108864+(int32()>>6))/9007199254740992.0