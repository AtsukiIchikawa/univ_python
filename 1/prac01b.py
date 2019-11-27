import random
num = random.randint(0, 50)

print("生成された数字:" + str(num))

if 0 <= num <= 10:
    print("「0超10以下」")
elif 10 < num <= 20:
    print("「10超20以下」")
elif 20 < num <= 30:
    print("「20超30以下」")
elif 30 < num <= 40:
    print("「30超40以下」")
elif 40 < num <= 50:
    print("「40超50以下」")
else:
    print("Error!")
