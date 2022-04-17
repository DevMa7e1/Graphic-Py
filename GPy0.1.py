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
def drawer(type, x, y):
    if type == "square":
        lines = ""
        for z in range(x):
            lines = lines+"__"
            linz = ""
        print(f" {lines} ")
        for i in range(x-1):
            for j in range(x*2):
                linz = linz+" "
            print(f"|{linz}|")
            linz = ""
        print(f"|{lines}|")
        lines = ""
    if type == "rectangle":
        lines = ""
        for z in range(x):
            lines = lines+"__"
            linz = ""
        print(f" {lines} ")
        for i in range(y-1):
            for j in range(x*2):
                linz = linz+" "
            print(f"|{linz}|")
            linz = ""
        print(f"|{lines}|")
        lines = ""
def buttonHandler(x, y, text):
    xx = ""
    xx2 = ""
    for i in range(x):
        xx = xx+"_"
        xx2 = xx2+" "
    print(f" {xx} ")
    for i in range(y):
        if i == y/2:
            print(f"|{text}|")
        print(f"|{xx2}|")
    print(f"|{xx}|")
class Rectangle:
    def __init__(self, x, y):
            self.x = x;
            self.y = y;
def eventHandlerClick(object, number, function):
    while True:
        try:
            if keyboard.read_key() == str(number):
                function()
                time.sleep(0.5)
                break
        except(KeyboardInterrupt):
            break
