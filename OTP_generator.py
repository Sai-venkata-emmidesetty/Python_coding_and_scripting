import random
import math

number="0123456789"
otp=""

for i in range(6):
 otp+=number[round(random.random()*10)]

print(otp)

