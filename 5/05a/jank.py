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


# p_win:プレイヤー勝利数 グローバル変数として定義
p_win = c_win = draw = 0


def wol(player_hand, computer_hand):

    global p_win
    global c_win
    global draw

    # じゃんけん結果をresultに格納
    result = janken(player_hand, computer_hand)

    if result == "a":
        draw += 1
        return "あいこ"
    elif result == "p":
        p_win += 1
        return "プレイヤーの勝ち"
    elif result == "c":
        c_win += 1
        return "コンピューターの勝ち"
    else:
        sys.exit()
