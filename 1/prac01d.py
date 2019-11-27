import random
num = random.randint(1, 3)

for i in range(1, 4):
    if num == 1:
        print(i + 1 + 10)
    elif num == 2:
        print(10 - i + 5)
    elif num == 3:
        print(10 * i + 3)
    else:
        print("Error!")
