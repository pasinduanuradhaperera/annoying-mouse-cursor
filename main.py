import pyautogui as g;
import time;
import fun;

g.FAILSAFE = False

# take the screen size 
sWidth, sHeight = g.size() 

#move the mouse in to the start possition 
g.moveTo(0,0)

count = 0
dir = 20
loop = 3
fun.moveC(dir,sHeight,sWidth,count,loop)
print("Hello")# this line not working only for checking      
       

    