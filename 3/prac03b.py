import statistics as st

listA = [139,254,"3,200",440,"300","1,000",500]

for i in range(0, 7):
    # str型だったら中身をintに
    if str == type(listA[i]):
        listA[i] = int(listA[i].replace(",", ""))

print("平均:" + str(st.mean(listA)))
print("母分散:" + str(st.pvariance(listA)))
print("標準偏差:" + str(st.pstdev(listA)))
print("標本分散:" + str(st.variance(listA)))
print("標本の標準偏差:" + str(st.stdev(listA)))
