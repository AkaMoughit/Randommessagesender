#By https://github.com/AkaMoughit 
import time
import random
import pyautogui as pg
message = ["Hi","How are you guys!","hello","Goodbye","GoodLuck guys!!!","keep up","All right"]
for i in range(100):
    pg.write(random.choice(message))
    pg.press('Enter')
    time.sleep(3600)

