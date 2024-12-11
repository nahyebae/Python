from modules.mylib import food

print(food.name)
food.cook()
food.eat()

from modules.mylib.food import name, cook, eat

print(name)
cook()
eat()

import bbb.cm2
print(bbb.cm2.add(1,2))

import bbb.cm2 as bc
print(bc.add(1,2))