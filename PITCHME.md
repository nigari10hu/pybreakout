# pybreakout
---
pythonの書き方
---
変数
```
hoge=0
```
```
hogehoge="aiueo"
```
型を書く必要はありません
+++
配列
```
hoge=[1,2,3,4,5]
```
```
hogehoge=[i for i in range(5)]
```
pythonの配列はリストです
+++
関数
```
def foo():
  print("foo関数が呼び出されました")

#foo関数を呼び出す
foo()
```
+++
条件分岐
```
if a>0:
  print("a>0")
```
```
if a>0 or b<0:
  print("a>0 または b<0")
```
```
if not a==0:
  print("aは0でない")
```
+++
ループ
```
for i in range(10):
  print(i)
```
10回ループします
```
a=[1,2,3,4,5]
for i in a:
  print(i)
```
iに順にaの要素が入ります(5回ループ)
```
while b==True:
  print("bは真")
```
bが真なら繰り返します
---
pygameをインストールする
+++
コマンドプロントで実行
```
pip install pygame
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
上から２、左から３のブロックの色を(0,0,255)に変える
```
color[2][3]=(0,0,255)
```
+++
バーの長さを変える
```
bar_length=60
```
```
bar_length=120
```
---
pygameの使い方
+++
初期化
```
#Pygameの初期化
pygame.init()
#大きさ400*400の画面を生成
screen = pygame.display.set_mode((400, 400))
#タイトルバーに表示する文字
pygame.display.set_caption("Test")
```
+++
描画
```
#画面を黒色(#000000)に塗りつぶし
screen.fill((0,0,0))
#描画
#円を描画
pygame.draw.circle(screen,(255,255,255),(x,y),r)
...
#画面を更新
pygame.display.update()
```
+++
円と四角
```
#円を描画
pygame.draw.circle(screen,(255,255,255),(x,y),r)
#四角を描画
pygame.draw.rect(screen,(255,255,255),(x,y,width,height))
```
+++
キー入力イベント
```
#イベント処理
for event in pygame.event.get():
    #閉じるボタンが押されたら終了
    if event.type == QUIT:
         #pygameの終了(画面閉じられる)
         pygame.quit()
         sys.exit(0)
    #ボタンが押されたら
     if event.type==KEYDOWN:
         if event.key==K_SPACE:
             print("スペースキーが押された")
             ...
```
+++
描画処理とキーイベントをループ処理で繰り返そう
```
while True:
  #描画処理
  ...
  #キーイベント処理
  ...
  #変数の更新
  ...
```
---
参考になるサイト
+++
pygameの関数リファレンス(英語)
https://www.pygame.org/docs/

(日本語訳)
http://westplain.sakuraweb.com/translate/pygame/
+++
チュートリアルっぽいサイト
https://algorithm.joho.info/programming/python/pygame/
https://riptutorial.com/ja/pygame
+++
分からなくなったらとりあえずググろう！
---
終わり
