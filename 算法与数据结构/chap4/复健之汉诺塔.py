# -*- coding：UTF-8 -*-
"""
Author   : Alyson
Time     : 2022年10月31日
Software : PyCharm 
"""
def moveTower (height,fromPole,withPole,toPole):
    if height>=1:
        moveTower(height-1,fromPole,toPole,withPole)
