import os
import random

random_num = random.randint(0,10)
input_num = int(input("Enter your guess number : "))

if input_num != random_num:
    os.remove('./sample.py')
    print("Sorry but you're wrong")
else:
    print("Congratulations you're correct")

print(random_num)
