from random import sample
from random import randint
from datetime import datetime

CHR_Q = 10
MAX_CONT = 5
cont_n = 0

def play():
    global mis_chr_q, chr_lst, mis_chr_lst
    mis_chr_q = randint(1,5)

    chr_lst = alp_gen()
    mis_chr_lst = sample(chr_lst, mis_chr_q)
    ask()
    return ans()

def alp_gen():
    alp_lst = [chr(ord("A")+i) for i in range(26)]
    return sample(alp_lst, CHR_Q)

def ask():
    print("対象文字：")
    for i in range(len(chr_lst)):
        print(chr_lst[i], end=" ")
    print("\n表示文字：")
    shuffled_lst = sample(chr_lst, len(chr_lst))
    for i in range(len(chr_lst)):
        if shuffled_lst[i] in mis_chr_lst:
            continue
        else:
            print(shuffled_lst[i], end=" ")
    print()

def ans():
    ask_chr_q = input("\n欠損文字はいくつあるでしょうか？：")
    if int(ask_chr_q) == mis_chr_q:
        print("正解です！\n具体的な欠損文字を１つずつ入力してください。")
        for i in range(mis_chr_q):
            ask_mis_chr = input(f"{i+1}文字目を入力：")
            if ask_mis_chr.upper() in mis_chr_lst:
                mis_chr_lst.remove(ask_mis_chr.upper())
            else:
                return False
        ed = datetime.now()
        print("おめでとう！クリア！！！！")
        print(f"クリア所要時間：{(ed-st).seconds} 秒")
        return True
    else:
        return False

if __name__ == "__main__":
    st = datetime.now()
    for i in range(MAX_CONT):
        ret = play()
        cont_n += 1
        if ret:
            break
        else:
            if MAX_CONT <= cont_n:
                print("残念！クリアできず・・・")
                break
            print("-"*20)
            print("不正解！もう一度チャレンジしてね！")
            print(f"残りコンティニュー回数：{MAX_CONT-cont_n} 回")
            print("-"*20)
            continue