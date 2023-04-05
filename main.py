import pyautogui as g;
import time;

g.FAILSAFE = False

# take the screen size 
sWidth, sHeight = g.size() 

#move the mouse in to the start possition 
g.moveTo(0,0)

count = 0
print("Start")
while True:
    print("Start")
    for i in range(sWidth-11):  
        print("Start")      
        cMX, cMY = g.position()
        g.moveTo(cMX + 1, cMY)
        
    for i in range(sHeight-11):  
        print("Start")      
        cMX, cMY = g.position()
        g.moveTo(cMX, cMY + 1)
        
    for i in range(sWidth-11):
        print("Start")        
        cMX, cMY = g.position()
        g.moveTo(cMX-1, cMY)
        
    swidth =- 10 
    sHeight =- 10
    
    for i in range(sHeight-21): 
        print("Start")      
        cMX, cMY = g.position()
        g.moveTo(cMX, cMY-1)
    
    count =+ 1 
    if count == 3:
        exit()
          
       

    