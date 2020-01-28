animals = ["cat", "chabo", "dog", "fish", "liz", "peng"]

# 誕生日の各桁を足し合わせる
def birthCount(n):
    s = str(n)
    array = list(map(int, s))
    return sum(array)

# 名前・誕生日に応じて動物を返す
def judge(sumInt):
    rem = sumInt % 6
    return animals[rem]
