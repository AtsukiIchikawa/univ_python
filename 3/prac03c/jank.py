def janken(p_hand, c_hand):

    # playerの手がグー
    if p_hand == 1:

        # a:あいこ, p:プレイヤー勝ち, c:コンピューター勝ち
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
