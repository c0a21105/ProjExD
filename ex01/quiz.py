from random import choice
from datetime import datetime

def shutudai(qa_lst):
    qa = choice(qa_lst)
    print("問題："+qa["q"])
    return qa["a"]

def kaitou(ans_lst):
    ans = input("回答：")
    ed = datetime.now()
    if ans in ans_lst:
        print("正解！")
    else:
        print("不正解...")
    print("所要回答時間："+str((ed-st).seconds)+" 秒")

if __name__ == "__main__":
    qa_lst = [
        {"q":"サザエの旦那の名前は？", "a":["マスオ", "ますお"]},
        {"q":"カツオの妹の名前は？", "a":["ワカメ", "わかめ"]},
        {"q":"タラオはカツオから見てどんな関係？", "a":["甥", "おい", "甥っ子", "おいっこ"]}
    ]

    ans_lst = shutudai(qa_lst)
    st = datetime.now()
    kaitou(ans_lst)