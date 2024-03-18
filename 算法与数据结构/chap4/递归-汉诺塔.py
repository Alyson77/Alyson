def moveTower(height,fromPole,withPole,toPole):
    if height>=1:
        moveTower(height-1,fromPole,toPole,withPole) #从开始柱经由目标柱移至中间柱
        moveDisk(height,fromPole,toPole) #记录每一步移盘片的操作
        moveTower(height-1,withPole,fromPole,toPole) #从中间柱经由开始柱移至目标柱

def moveDisk(disk,fromPole,toPole):
    print(f'Moving disk[{disk}] from {fromPole} to {toPole}')

moveTower(3,'#1','#2','#3')

