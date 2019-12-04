import sys

question1 = ["早稲田大学のキャンパスではないのは？", "所沢", "戸山", "日吉", 3]
question2 = ["早稲田大学に存在しない学部は？", "医学部", "人間科学部", "商学部", 1]
question3 = ["県ではないものは？", "新潟", "京都", "愛媛", 2]
question4 = ["システムプログラミング言語は？", "PHP", "Javascript", "Rust", 3]


# 正解/不正解ジャッジ関数
def judge():

    print("正解は？")
    res = int(input())

    if res == q_num[4]:
        print("正解")
    elif res != q_num[4]:
        print("不正解")
    else:
        sys.exit()


for i in range(4):
    # 質問指定
    exec("q_num = question%d" % (i+1))
    
    # 質問表示
    print(q_num[0])

    # 回答表示
    for j in range(3):
        print(str(j+1) + q_num[j+1])

    # 判定
    judge()
