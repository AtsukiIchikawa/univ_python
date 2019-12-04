list = [[5, 3, 12], [2, 1, 9], [11, 10, 7]]

print("何行目？")
row = int(input()) - 1

print("何列目？")
col = int(input()) - 1

number = list[row][col]
print(str(row+1) + "行目" + str(col+1) + "列目の値は" + str(number))
