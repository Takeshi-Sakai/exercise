# -*- coding: utf-8 -*-

##　python


##　リスト

# リストの作成
xs = ["A", "B", "C"]

xs[-1]
#→[-1]最後の要素を示す

# スライス
['a', 'b', 'c', 'd', 'e'][1:3]
#→['b', 'c']						# インデックスの範囲を指定してリストを切り出すことができる

# リストの連結
xs = [1, 2, 3]
xs = xs + ["a", "b", "c"]
#→[1, 2, 3, 'a', 'b', 'c']

# len関数
len([1, 2])						# リストの長さを調べることができる
#→2

# in演算子
1 in [1, 3]						# ある値がリストに含まれているか調べる
#→True
2 in [1, 3]
#→False

# リストのメソッド
xs.append(1)					# リストの末尾に値を一つ追加

xs.extend([3, 4])				# リストの末尾にいくつかの要素を追加

xs.pop()						# リストの要素を取り除く（末尾の）

xs.pop(1)						# リストの要素を取り除く（1番目の要素）

xs.index(3)						# 3の値が存在する場所のインデックスを取得

xs.sort()						# リストをソートする


## 辞書

# 辞書の作成
x = {"Jan":1, "Feb":2, "Mar":3}
x["Mar"]						# キーを指定して値を取り出す
x["Mar"] = "three"				# キー"Mar"の値を"three"に上書きする
"Mar" in x 						# キー"Mar"が存在するか調べる
#→True

# 辞書のメソッド
x.get("Jan")					# キーによる値の取得を行う
#→1
x.get("Jun")					# キーが存在しない場合"Noneが返ってくる"
#"None"を表示させたい場合は print x.get("Jun") とすると"None"が表示される

x.keys()						# キーの一覧をリストで取得する

x.values()						# すべての値をリストを取得する

x.items()						# すべてのキーと値からなるリストを取得する

len(x)							# 辞書のキーの数を調べる


## 制御構文

# for文
fruits = ["Apple", "Orange", "Banana"]
for fruit in fruits:
	print fruit

# if文
a = 0
if a < 0:
	print "Negative"
elif a == 0:
	print "Zero"
elif a == 1:
	print "One"
else:
	print "Many"


## 関数

# 関数の宣言
def say_hello(name):
	return "Hello, " + name + "!"

print say_hello("World")

# 引数のデフォルト値
def say_hello2(name, greed="Hi"):		# 引数にデフォルト値を与えることも可能。その場合関数の呼び出し時に引数の指定を省略することもできる。
	return greed + ", " + name + "!"

print say_hello2("brother")

# キーワード引数
def who_have_what(who, what):
	print who + " have " + what + "."

who_have_what(what="a pen", who="I")	# 関数の呼び出し時に引数と値の組み合わせを指定することによって任意の順で引数を指定することができる


def f(a, b, c):
	print a + b + c

f("c", "a", "b")
