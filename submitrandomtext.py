#By https://github.com/AkaMoughit
import time
import random
import pyautogui as pg
def ChoseTime(x) :
    if x == 1 :
        return 5
    if x == 2 :
        return 10
    if x == 3 :
        return 30
    if x == 4 :
        return 60
    if x == 5 :
        return 300
    if x == 6 :
        return 900
    if x == 7 :
        return 1800
    if x == 8 :
        return 2700
    if x == 9 :
        return 3600
    if x == 10 :
        return 10800

print("By Moughit, Welcome")
print("pick a time:\n")
x = int(input("1: 5s\n2: 10s\n3: 30s\n4: 1min\n5: 5min\n6: 15min\n7: 30min\n8: 45min\n9: 1h\n10: 3h\n"))
message = ["Hi","How ru g!","hello","GL guys!!!","keep up","All right?","Any new update ?","thx","morning :)",":D",":laughing:",":sunglasses:","y","make sense"]
ms = "Hi"
for i in range(1000):
    msg = random.choice(message)
    if msg != ms :
        ms = msg
    pg.write(ms)
    time.sleep(1)
    pg.press('Enter')
    time.sleep(ChoseTime(x))