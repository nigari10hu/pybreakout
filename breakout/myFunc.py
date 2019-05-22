import math

#跳ね返った方向を返す
def bounce_angle(angle,b_x=False,b_y=False):
    sin_angle=math.sin(angle)
    cos_angle=math.cos(angle)
    
    #x方向を入れ替える
    if b_x:
        cos_angle*=-1
    #y
    if b_y:
        sin_angle*=-1

    return math.atan2(sin_angle,cos_angle)


#ぶつかったか計算する
#x_y,1=横からぶつかった,-1=縦からぶつかった,0=それ以外
def collision(point,r,rect):
    #pointの座標
    point_x=point[0]
    point_y=point[1]
    #四角形の座標
    rect_x=rect[0]
    rect_y=rect[1]
    rect_width=rect[2]
    rect_height=rect[3]
    #どの方向からぶつかったか保存する
    x_y=0
    
    #x座標
    if point_x>rect_x+rect_width:
        point_lx=rect_x+rect_width
        x_y+=1
    elif point_x<rect_x:
        point_lx=rect_x
        x_y+=1
    else:
        point_lx=point_x
    #y座標
    if point_y>rect_y+rect_height:
        point_ly=rect_y+rect_height
        x_y-=1
    elif point_y<rect_y:
        point_ly=rect_y
        x_y-=1
    else:
        point_ly=point_y
    #ぶつかったか判定    
    if (point_ly-point_y)**2+(point_lx-point_x)**2< r**2:
        return True,x_y
    
    return False,x_y
