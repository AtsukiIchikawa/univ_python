def judge_multiple3(num):
    
    remainder = num % 3
    
    if remainder == 0:
        print(str(num) + "は3の倍数")
    elif remainder == 1:
        print(str(num) + "は3の倍数でない" + "(余り:" + str(remainder) + ")")
    elif remainder == 2:
        print(str(num) + "は3の倍数でない" + "(余り:" + str(remainder) + ")")


print("整数を入力してください")
input_num = int(input())

judge_multiple3(input_num)
