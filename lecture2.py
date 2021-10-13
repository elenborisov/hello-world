# # print("Hello World!")
# # print(2+2)
# # print(50-5*6)
# # print((50-5)*6)
# # print((50-5*6)/4)
# # print(8/5)
# # print(17/3)
# # print(17//3)
# # print(17%3)
# # print(2**3)

# # # 0=> ()
# # # 1=> **
# # # 2=> *,/,//,%
# # # 3=> +,-

# # width=4
# # height=5
# # print(width*height)

# # width = int(input("Въведете широчина = "))
# # height = int(input("Въведете височина = "))
# # print("Лицето на правоъгълника е : ")

# # width = float(input('a = '))
# # height = float(input('b = '))
# # area = width * height
# # print('S = a*b = ', area)

# print(complex(2,3))
# print(complex(4))

import random

random.seed()
width = random.random()*10
height = random.random()*10
print("a = ", width)
print("b = ", height)

print(random.randrange(-5, 10, 3))
print(random.uniform(-5, 10))

print(width, "                 =>               ", round(width, 2))

import math

print(math.sqrt(4))