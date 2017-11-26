# -*- coding: utf-8 -*-
import csv

x = [] #x軸の値
sin = [] #y軸の値(3つ分)
ans = [] #答えのy軸の値

#sin波のcsvファイルを開く
sin_file = open("sin.csv", "r")

#リーダを取得
sin_reader = csv.reader(sin_file)
#読み込んでリストに入れていく
for row in sin_reader:
    x.append(row[0])
    sin.append(row[1:])

#ファイルは必ず閉じる
sin_file.close()

for r in sin:
    a = float(r[0])+float(r[1])+float(r[2])
    ans.append(a)


ans_file = open("ans.csv", "w")

writer = csv.writer(ans_file, lineterminator='\n')
for i in range(len(ans)):
    writer.writerow([i, ans[i]])

ans_file.close()
