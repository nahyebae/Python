import calc_module

print(calc_module.add(2, 3))
print(calc_module.sub(2, 3))
print(calc_module.mul(2, 3))
print(calc_module.div(2, 3))


from calc_module import add # add만 가져오고 싶을 때 

print(add(1,2))
# calc_module.add() # 안됨

import calc_module as cm # 다른 이름으로 바꾸기
print(cm.add(1,2))

import math # math import
print(math.floor(3.141592))
print(math.ceil(3.141592))
print(math.sqrt(9))

from math import floor, ceil # math에서 특정 함수만 import
print(math.floor(3.141592))
print(math.ceil(3.141592))

import random
print(random.randint(1,5))
print(random.uniform(1,5))
print(random.random())
print(random.randrange(1,3))
print(random.randrange(1,5,2))