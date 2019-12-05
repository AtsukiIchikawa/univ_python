# 合計算出関数
def calc_sum(list, length):

    sum = 0

    for i in range(length):
        sum += list[i]

    return sum


# 平均算出関数
def calc_ave(list, length, sum):

    ave = sum / length
    return ave


# 分散算出関数
def calc_var(list, length, average):

    variance = 0
    tmp = 0

    for i in range(length):
        tmp += (list[i] - average)**2

    variance = tmp / length
    return variance




# 空のリスト定義
list = []

# リストの長さ設定
print("何個の数字？")
list_num = int(input())

# リストに追加
for i in range(list_num):
    print(str(i+1) + "個めの数字を入力してください")
    list += [float(input())]

# 変数list_lengthにリストの長さ格納
list_length = len(list)


# 合計
list_sum = calc_sum(list, list_length)
print("合計:" + str(list_sum))

# 平均
list_ave = calc_ave(list, list_length, list_sum)
print("平均:" + str(list_ave))

# 分散
print("分散:" + str(calc_var(list, list_length, list_ave)))
