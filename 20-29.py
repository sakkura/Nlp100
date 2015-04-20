# -*- coding: utf-8 -*-
import json
import gzip
import sys


if (sys.stdout.encoding is None):
	print >> sys.stderr, "please set python env PYTHONIOENCODING=UTF-8, example: export PYTHONIOENCODING=UTF-8, when write to stdout."
	

#20. JSONデータの読み込み
#Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．問題21-29では，ここで抽出した記事本文に対して実行せよ．
article = {}
with gzip.open("jawiki-country.json.gz", "rb") as fh:
	for line in fh.readlines():
		js = json.loads(line, "utf-8")
		article[js["title"]] = js["text"]
print(article[u"イギリス"])

#21. カテゴリ名を含む行を抽出
#記事中でカテゴリ名を宣言している行を抽出せよ．
for country,text in article.items():
	for line in text.split("\n"):
		if "Category:" in line:
			print(line)

#22. カテゴリ名の抽出
#記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．



#23. セクション構造
#記事中に含まれるセクション名とそのレベル（例えば"== セクション名 =="なら1）を表示せよ．



#24. ファイル参照の抽出
#記事から参照されているメディアファイルをすべて抜き出せ．



#25. テンプレートの抽出
#記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，辞書オブジェクトとして格納せよ．



#26. 強調マークアップの除去
#25の処理時に，テンプレートの値からMediaWikiの強調マークアップ（弱い強調，強調，強い強調のすべて）を除去してテキストに変換せよ（参考: マークアップ早見表）．



#27. 内部リンクの除去
#26の処理に加えて，テンプレートの値からMediaWikiの内部リンクマークアップを除去し，テキストに変換せよ（参考: マークアップ早見表）．



#28. MediaWikiマークアップの除去
#27の処理に加えて，テンプレートの値からMediaWikiマークアップを可能な限り除去し，国の基本情報を整形せよ．



#29. 国旗画像のURLを取得する
#テンプレートの内容を利用し，国旗画像のURLを取得せよ．（ヒント: MediaWiki APIのimageinfoを呼び出して，ファイル参照をURLに変換すればよい）




