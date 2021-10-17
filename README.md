# python-_random-module
简单的python _random模块使用(不是random模块)
通过简单的加密来一行实现random(((
使用:

import random
random.random()#返回0-1之间的小数

random.random是random.a的一个方法,random.a=random.Random(),random.Random=_random.Random
该模块包含了_random.Random的所有方法并作为一个简单的使用例子,可以改写Random的一些方法:

class Random(random.Random):#或_random.Random,_random是built-in模块
  pass#def一些函数来改写,例如random,seed等

写这个主要是自己平时用着方便
