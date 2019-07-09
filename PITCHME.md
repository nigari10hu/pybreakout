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
+++
配列
```
hoge=[1,2,3,4,5]
```
```
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
ループ
```
    while True:
        #画面を黒色(#000000)に塗りつぶし
        screen.fill((0,0,0))
        #描画
        ...
        #画面を更新
        pygame.display.update()
        #イベント処理
        for event in pygame.event.get():
            #閉じるボタンが押されたら終了
            if event.type == QUIT:
                #pygameの終了(画面閉じられる)
                pygame.quit()
                return
            #ボタンが押されたら
            if event.type==KEYDOWN:
                if event.key==K_SPACE:
                  ...

```
+++
```
  # まる
  pygame.draw.circle(screen,(255,255,255),(int(boll_x),int(boll_y)),boll_r)
  #しかく
  pygame.draw.rect(screen,(255,255,255),(bar_x,380,bar_length,10))
  ```
---
終わり
