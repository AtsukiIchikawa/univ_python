def calc_bmi(height, weight):
    
    bmi = weight / (height/100)**2

    if bmi < 18:
        return "やせ型"
    elif bmi >= 25:
        return "肥満"
    else:
        return "普通"


print("身長を入力してください(cm)")
h = int(input())

print("体重を入力してください(kg)")
w = int(input())

print(calc_bmi(h, w))
