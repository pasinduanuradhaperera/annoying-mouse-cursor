import pyautogui as g
import time;

# prep length variable
def createVar(l, d):
   return l - (l % d)

# move cursor
def moveC(d, h, w, c):
    
    print("hello world")
    
# move curser to one dir 
def move(l, d):
    for i in range(l-11):    
        cMX, cMY = g.position()
        g.moveTo(cMX + d, cMY)
    