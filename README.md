# python-_random-module

### https://github.com/python/cpython/blob/main/Modules/_randommodule.c

将上面的核心算法改(ctrl+c)写(ctrl+v)成python

### 使用:

a=random.RandomObject()#默认种子是int(time.time())

a.seed(seed)#相当于random.seed()

a.int32()#python random的核心算法,应该是返回0-2^32-1之间的数字,但没有暴露在random和_random模块里

a.random()#相当于random.random()

写这个主要是自己平时用着方便
