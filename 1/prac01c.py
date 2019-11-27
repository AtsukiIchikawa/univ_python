import sys

# 再帰版
"""
def judge():
    print("1か2か3を半角で入力してください")
    res = input()
    res = int(res)

    if res in range(1, 4):
        sys.exit()
    else:
        judge()

judge()
"""


# while版
print("1か2か3を半角で入力してください")
res = input()

while True:
    # 数字以外が入力されたとき終了
    if res.isdigit() == True:
        res = int(res)
    else:
        print("数字以外は入力できません")
        sys.exit()
    
    if res in range(1, 4):
        break;
    else:
        res = input()
        continue;
