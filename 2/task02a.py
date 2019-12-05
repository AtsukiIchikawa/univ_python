import random
import sys

def janken(p_hand, c_hand):

    # playerの手がグー
    if p_hand == 1:

        # a:あいこ, p:プレイヤー勝ち, c:コンピューター価値
        if c_hand == 1:
            return "a"
        elif c_hand == 2:
            return "p"
        elif c_hand == 3:
            return "c"

    # playerの手がチョキ
    elif p_hand == 2:

        if c_hand == 1:
            return "c"
        elif c_hand == 2:
            return "a"
        elif c_hand == 3:
            return "p"

    # playerの手がパー
    elif p_hand == 3:

        if c_hand == 1:
            return "p"
        elif c_hand == 2:
            return "c"
        elif c_hand == 3:
            return "a"



# p_win:プレイヤー勝利数
p_win = 0
c_win = 0

for i in range(3):

    print("手を決めてください  1:グー, 2:チョキ, 3:パー")
    player_hand = int(input())
    computer_hand = random.randint(1, 3)

    print("プレイヤーの手:" + str(player_hand) + " コンピューターの手:" + str(computer_hand))

    # じゃんけん結果をresultに格納
    result = janken(player_hand, computer_hand)

    if result == "a":
        print("あいこ")
    elif result == "p":
        print("プレイヤーの勝ち")
        p_win += 1
    elif result == "c":
        print("コンピューターの勝ち")
        c_win += 1
    else:
        sys.exit()

    # 2周目でどちらかが2勝していたら結果表示して終了
    if i == 1:
        if p_win == 2:
            print("playerが2勝したので終了です")
            sys.exit()
        elif c_win == 2:
            print("computerが2勝したので終了です")
            sys.exit()


print(str(p_win) + "勝" + str(c_win) + "敗" + str(3 - p_win - c_win) + "あいこ")
