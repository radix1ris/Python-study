import message
print (message.hello("田中"))
print (message.goodbye("田中"))

from message import hello
print(hello("田中"))

import random
number = random.randint(1,100)
print(number)

import math
print(math.sqrt(81))

from random import randint
print(randint(1,6))

import calculation
print(calculation.add(10,5))
print(calculation.multiply(10,5))
print(calculation.subtract(10,5))

scores = [80,95,50,70]
import score_utils as su
print(f"平均点は{su.calculate_average(scores):.1f}点です")

for score in scores:
    if su.is_passed(score):
        print(f"{score}点は合格です")
    else:
        print(f"{score}点は不合格です")

numbers = [3,8,11,14]
import number_utils as nu
print(f"合計は{nu.calculate_total(numbers)}です")
