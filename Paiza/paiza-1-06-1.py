﻿# coding: utf-8

'''
演習課題「1から6のサイコロを作る」
randint関数を使用して「サイコロの目は**です。」と出力をしてください。
**のところには、1 ～ 6のランダムな数字が入るように作成してください。

プログラムを実行して、正しく出力されれば演習課題クリアです！

 期待する出力値
サイコロの目はxです。

'''

import random
print("サイコロの目は**です。")

# coding: utf-8

#数の表示とサイコロ

import random

number = random.randint(1,6)

print("サイコロの目は" + str(number) + "です。")