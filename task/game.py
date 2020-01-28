import sys
import diag
from tkinter import *
from tkinter import ttk, PhotoImage

# 入力された名前・誕生日から数字を生み出す
def geneInt():
    name = n.get()        # 入力された名前をnameに代入
    intName = 0           # 名前を数字変換した結果をintNameに入れる
    for c in name:
        intName += ord(c)

    birth = b.get()       # 入力された誕生日をbirthに代入
    nbsum = intName + diag.birthCount(birth)  # 計算結果をnbsumに代入

    frame.destroy()                    # 現在のframeを削除
    root.geometry('400x440')           # windowサイズ変更

    # 計算結果から画像選択
    if diag.judge(nbsum) == 'cat':
        label3.configure(image=cat, text='You are ねこ！ おめでとう！')
    elif diag.judge(nbsum) == 'chabo':
        label3.configure(image=chabo, text='君はにわとり')
    elif diag.judge(nbsum) == 'dog':
        label3.configure(image=dog, text='みんな大好きイッヌ')
    elif diag.judge(nbsum) == 'fish':
        label3.configure(image=fish, text='さかなだよ')
    elif diag.judge(nbsum) == 'liz':
        label3.configure(image=liz, text='レッドヘッドアガマ')
    elif diag.judge(nbsum) == 'peng':
        label3.configure(image=peng, text='スマホぺんぎん')
    else:
        sys.exit()
    label3.grid(row=0, column=0)


# root
root = Tk()
root.title('どうぶつ診断')
frame = ttk.Frame(root)

# get Input Text
n = StringVar()
b = StringVar()

# label & entry
label1 = ttk.Label(frame, text='名前を入力してください', foreground='green')
entry1 = ttk.Entry(frame, textvariable=n)
label2 = ttk.Label(frame, text='誕生日を入力してください（数字のみ）', foreground='green')
entry2 = ttk.Entry(frame, textvariable=b)

# animalIMAGE lalbel
label3 = Label(root, compound='top')
cat   = PhotoImage(file='img/cat.png')
chabo = PhotoImage(file='img/chabo.png')
dog   = PhotoImage(file='img/dog.png')
fish  = PhotoImage(file='img/fish.png')
liz   = PhotoImage(file='img/lizard.png')
peng  = PhotoImage(file='img/penguin.png')

# button
button = ttk.Button(frame, text='OK', command=geneInt)

# frame arrangement
frame.grid(row=0, column=0)
for child in frame.winfo_children():
    child.grid_configure(padx=5, pady=5)

root.mainloop()
