import pyautogui as g
import time;

# prep length variable
def createVar(l, d):
   return (l - (l % d)) / d
   

# move cursor
def moveC(d, h, w, c, Loop):
    w = createVar(w, d)
    h = createVar(h, d)    
    while True:
        move(w, d, 0)
        if d < 0:
            h =- d
            w =- d
        move(h, 0, d)        
        d = d * (-1)
        c = c + 1
        if Loop < c :
            exit()
        print(c)
    
    
    
   
    
# move curser to one dir 
def move(l, d1, d2):
    l = int(l)
    for i in range(l-11):    
        cMX, cMY = g.position()
        g.moveTo(cMX + d1, cMY+d2)
    