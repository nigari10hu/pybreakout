# pybreakout
---
pythonの書き方
---
変数
```
hoge=0
hogehoge="aiueo"
```
+++
配列
```
hoge=[1,2,3,4,5]

hogehoge=[i for i in range(5)]
```
+++
関数
```
def foo():
  ...
```
+++
条件分岐
```
if a>0:
  ...
 
if a>0 or b<0:
  ...

if not a==0:
  ...
```
+++
ループ
```
for i in range(10):
  ...

a=[1,2,3,4,5]
for i in a:
  ...

while b==True:
  ...
```
---
pybreakoutのコードを書き換える
+++
ブロックのいろを変える
```
color=[[(255,0,0) for i in range(10)] for j in range(10)]
```
```
color=[[(0,255,0)] for i in range(10)] for j in range(10)]
```
RGB=赤、緑、青
+++
バーの長さを変える
```
bar_length = 60
```
```
bar_length=120
```
---
pygameの使い方
+++

+++
---
終わり
