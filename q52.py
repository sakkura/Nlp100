# -*- coding: utf-8 -*-
import sys
from stemming.porter2 import stem
# 51. 単語の切り出し
# 空白を単語の区切りとみなし，50の出力を入力として受け取り，1行1単語の形式で出力せよ．ただし，文の終端では空行を出力せよ．

stdinData = sys.stdin.read()
for line in stdinData.split("\n"):
	print stem(line)
