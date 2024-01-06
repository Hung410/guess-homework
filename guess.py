# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 20:47:08 2024

@author: DELL-USER
"""

import random 

ans=random.randint(1,100)

guess=0
count=0

minv=1
maxv=100

while ans !=guess and count<5:
    guess=int(input('輸入1~100之間的整數:'))
    if guess > ans:
        print(guess,'太大了,請猜小一點')
        maxv=guess
        print(minv,'到',maxv,'之間的數值')
        
        
    elif guess < ans:
        print(guess,'太小了,請猜大一點')
        minv=guess
        print(minv,'到',maxv,'之間的數值')
        
    count+=1    
    
if ans==guess:
    print('答對了 !!!')
    
else:
    print('猜的次數過多,不給猜了 ')
    
    



