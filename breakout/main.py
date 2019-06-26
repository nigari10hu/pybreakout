#モジュールをインポート
import pygame
from pygame.locals import*
import math
import random
import myFunc
from myFunc import*

#bollの変数定義
#drawWindowの中身を描く
#collision系の関数を呼ぶ

#グローバル変数

#ブロック
#色
block = [[(255,0,0) for i in range(10)] for j in range(10)]
#壊れたか
breaked=[[False for i in range(10)] for j in range(10)]

#ボールの座標、半径
boll_x = 200
boll_y = 340
boll_r = 2
#ボールの向き,速さ
boll_angle = 0
boll_spead = 3
#バーの座標、長さ
bar_x = 170;
bar_length = 60;
#ゲームの開始
gameStart = False

#初期化
def gameInit():
    global boll_x
    boll_x=200
    global boll_y
    boll_y=340
    global boll_angle
    boll_angle=(math.pi/2*3)+(math.pi/180*random.randint(-45,45))
    global boll_spead
    boll_spead=3
    global block
    block = [[(255,0,0) for i in range(10)] for j in range(10)]
    global breaked
    breaked=[[False for i in range(10)] for j in range(10)]

   

#描画
def drawWindow(screen):
    #ボールを描画
    pygame.draw.circle(screen,(255,255,255),(int(boll_x),int(boll_y)),boll_r)
    
    #バーを描画
    pygame.draw.rect(screen,(255,255,255),(bar_x,380,bar_length,10))

    #ブロックを描画
    for y in range(10):
        for x in range(10):
            if not breaked[y][x]:
                pygame.draw.rect(screen,block[y][x],(40*x,20*y,39,19))

#更新
def update():
    #グローバル宣言
    global boll_x
    global boll_y

    #ボールを動かす
    boll_x+=math.cos(boll_angle)*boll_spead
    boll_y+=math.sin(boll_angle)*boll_spead

    #ブロックとの当たり判定
    block_collision()
    bar_collision()
    window_collison()

#当たり判定

#ブロックのあたり判定
def block_collision():
    global boll_angle

    #ブロックとの当たり判定
    for y in range(10):
        for x in range(10):
            #壊されていないなら
            if not breaked[y][x]:
                #collision(ボール座標,ボール半径、長方形(座標、高さ幅))
                coll,xy = collision((boll_x,boll_y),boll_r,(40*x,20*y,39,19))
                if coll:
                    if xy==-1 or xy==0:
                        #b_y=True、y軸を反転
                        boll_angle=bounce_angle(boll_angle,b_y=True)
                    elif xy==1:
                        boll_angle=bounce_angle(boll_angle,b_x=True)
                    #スピードを上げる
                    #boll_spead*=1.001
                    #if boll_spead>=10:
                        #boll_spead=10
                    breaked[y][x]=True
                    break
        #2重ループを抜ける
        else:
            continue
        break

#バー
def bar_collision():
    global boll_x
    global boll_y
    global boll_angle

    #バーとの当たり判定
    coll_bar,xy=collision((boll_x,boll_y),boll_r,(bar_x,380,bar_length,10))
    if coll_bar:
        boll_angle=bounce_angle(boll_angle,b_y=True)
        boll_y = 380-boll_r

#ウインドウ
def window_collison():
    global boll_angle

    #ボールが画面の外にでたら
    #横
    if boll_x<0 or boll_x>400:
         boll_angle=bounce_angle(boll_angle,b_x=True)
    #上
    if boll_y<0:
         boll_angle=bounce_angle(boll_angle,b_y=True)
    #下
    if boll_y>410:
        gameStart=False

#main関数
def main():
    global bar_x
    global gameStart
    
    #Pygameの初期化
    pygame.init()
    #大きさ400*400の画面を生成
    screen = pygame.display.set_mode((400, 400))
    #タイトルバーに表示する文字
    pygame.display.set_caption("Test")
    #fpsの制御
    clock = pygame.time.Clock()

    while True:
        #画面を黒色(#000000)に塗りつぶし
        screen.fill((0,0,0))
        #描画
        drawWindow(screen)
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
                    #初期化
                    gameInit()
                    gameStart=True

        #長押しの処理
        pressed_key=pygame.key.get_pressed()
        if pressed_key[K_LEFT]:
            bar_x-=2
        if pressed_key[K_RIGHT]:
            bar_x+=2

        #ゲームがスタートしているなら
        if gameStart:
            update()
        
        #fps60に固定
        clock.tick(60)

if __name__ == "__main__":
    main()
