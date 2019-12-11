import jank
import random

if __name__ == '__main__':

    print("あなたの手を選んでください(1:グー, 2:チョキ, 3:パー)")
    p_hand = int(input())

    c_hand = random.randint(1, 3)

    if "p" == jank.janken(p_hand, c_hand):
        print("あなたの勝ち")
    elif "c" == jank.janken(p_hand, c_hand):
        print("あなたの負け")
    else:
        print("あいこ")
