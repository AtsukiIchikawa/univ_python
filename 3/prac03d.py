import csv

csvfile = open("prac_test.csv",encoding="utf-8")
score = []
abe = 0
beppu = 0
sida = 0
a_score = 0
a_ave = 0
b_score = 0
b_ave = 0
Aa_score = 0
Ba_score = 0
Ca_score = 0
Ab_score = 0
Bb_score = 0
Cb_score = 0

for row in csv.reader(csvfile):
    score.append(row)

for i in range(1, 19):
    if score[i][0] == "abe":
        abe += float(score[i][2])
    elif score[i][0] == "beppu":
        beppu += float(score[i][2])
    elif score[i][0] == "sida":
        sida += float(score[i][2])

print(abe)
print(beppu)
print(sida)



for j in range(1, 19):
    tmp = score[j][1].split("_", 1)
    if "a" == tmp[1]:
        a_score += float(score[j][2])

        if "A" == tmp[0]:
            Aa_score += float(score[j][2])
        if "B" == tmp[0]:
            Ba_score += float(score[j][2])
        if "C" == tmp[0]:
            Ca_score += float(score[j][2])

    elif "b" == tmp[1]:
        b_score += float(score[j][2])

        if "A" == tmp[0]:
            Ab_score += float(score[j][2])
        if "B" == tmp[0]:
            Bb_score += float(score[j][2])
        if "C" == tmp[0]:
            Cb_score += float(score[j][2])


a_ave = a_score / 9
b_ave = b_score / 9
print("a平均:" + str(a_ave))
print("b平均:" + str(b_ave))

Aa_ave = Aa_score / 3
Ba_ave = Ba_score / 3
Ca_ave = Ca_score / 3
print("Aa平均:" + str(Aa_ave))
print("Ba平均:" + str(Ba_ave))
print("Ca平均:" + str(Ca_ave))

Ab_ave = Ab_score / 3
Bb_ave = Bb_score / 3
Cb_ave = Cb_score / 3
print("Ab平均:" + str(Ab_ave))
print("Bb平均:" + str(Bb_ave))
print("Cb平均:" + str(Cb_ave))
