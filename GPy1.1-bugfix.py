import keyboard
import time
class Square:
    def __init__(self, area):
        if(area < 2):
            quit("User error in drawer module: Drawer can't handle sizes smaller than 2.")
        self.area = area;
class Button:
    def __init__(self, x, y, text):
        self.x = x;
        self.y = y;
        self.text = text
def drawer(type, object):
    if type == "square":
        lines = ""
        for z in range(object.area):
            lines = lines+"__"
            linz = ""
        print(f" {lines} ")
        for i in range(object.area-1):
            for j in range(object.area*2):
                linz = linz+" "
            print(f"|{linz}|")
            linz = ""
        print(f"|{lines}|")
        lines = ""
    if type == "rectangle":
        lines = ""
        for z in range(object.x):
            lines = lines+"__"
            linz = ""
        print(f" {lines} ")
        for i in range(object.y-1):
            for j in range(object.x*2):
                linz = linz+" "
            print(f"|{linz}|")
            linz = ""
        print(f"|{lines}|")
        lines = ""
def buttonHandler(object):
    xx = ""
    xx2 = ""
    for i in range(object.x):
        xx = xx+"_"
        xx2 = xx2+" "
    print(f" {xx} ")
    for i in range(object.y):
        if i == object.y/2:
            print(f"|{object.text}|")
        print(f"|{xx2}|")
    print(f"|{xx}|")
class Rectangle:
    def __init__(self, x, y):
            self.x = x;
            self.y = y;
def eventHandlerClick(object, number, function, afterfunc):
    while True:
        try:
            if keyboard.read_key() == str(number):
                function()
                time.sleep(0.5)
            time.sleep(0.5)
            afterfunc()
        except(KeyboardInterrupt):
            break
def refresh():
    import os
    os.system("cls")
