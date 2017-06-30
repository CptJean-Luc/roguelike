# imports, global vars, and classes
from random import randint

map_size = range(30)
screen_size = range(21) #must be odd

player_name = "Samus" #input("Player Name: ") # Commented for debugging 
if player_name.lower() == "graham":
    player_name = "A stupid dork"

class Character(object):
    def __init__(self, name, posy, posx, health_max, health_current):
        self.name = name
        self.posy = posy
        self.posx = posx
        self.health_max = health_max
        self.health_current = health_current

playeryrand = randint(0, len(map_size)) # must match map size - 21
playerxrand = randint(0, len(map_size)) # must match map size - 21
player = Character(player_name, playeryrand, playerxrand, 100.0, 100.0)

#view functions
def clear():
    print("\n" * 50)

#""" the real initmap function
def initmap():
    size = map_size
    for height in size:
        mapx.append(["."] * len(size))
#"""

""" Debug initmap function 
iteration_call_number = 0

def initmap():
    size = map_size
    for height in size:
        mapx.append([get_iteration()] * len(size))
        
def get_iteration():
    global iteration_call_number
    iteration1 = iteration_call_number % 26
    iteration2 = iteration_call_number // 26
    alphamap = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    iteration_call_number = iteration_call_number + 1
    return "%s%s" % (alphamap[iteration2], alphamap[iteration1])     
#"""

def initscreen():
    size = screen_size
    for height in size:
        screen.append(["|"] * len(size))

def refscreen():
    clear()
    posy = player.posy - (len(screen_size) // 2) # Sets the top left corner of the screen as an offset of the player
    posx = player.posx - (len(screen_size) // 2) #
    """ Debugging """
    print("x:", player.posx, "y:", player.posy)
    """ """
    print(player.name, "   ", "Health:", get_health_player_percent(), "%", get_player_health_bar())
    print("")
    for y in screen_size:
        for x in screen_size:
            try:
                screen[y][x] = mapx[posy + y][posx + x]
            except:
                IndexError
                screen[y][x] = "*"

    screen[(len(screen_size) // 2)][(len(screen_size) // 2)] = "@"
    """ Debuggng """
    #print(screen)
    #print(mapx)
    """ """
    for height in screen:
        print(" ".join(height))

def get_health_player_percent():
    return 100 * (player.health_current / player.health_max)

def get_player_health_bar():
    healthlst = ["["]
    health = get_health_player_percent()
    for x in range(10):
        if health >= 10:
            healthlst.append("|")
            health = health - 10
        else:
            healthlst.append("-")
    healthlst.append("]")
    return "".join(healthlst)

# movement
def move_left():
        player.posy = player.posy
        player.posx = player.posx - 1
        refscreen()
        map_action(input("Action: "))

def move_down():
        player.posy = player.posy + 1
        player.posx = player.posx
        refscreen()
        map_action(input("Action: "))

def move_right():
        player.posy = player.posy
        player.posx = player.posx + 1
        refscreen()
        map_action(input("Action: "))

def move_up():
        player.posy = player.posy - 1
        player.posx = player.posx
        refscreen()
        map_action(input("Action: "))

def move_up_right():
        player.posy = player.posy - 1
        player.posx = player.posx + 1
        refscreen()
        map_action(input("Action: "))

def move_up_left():
        player.posy = player.posy - 1
        player.posx = player.posx - 1
        refscreen()
        map_action(input("Action: "))

def move_down_right():
        player.posy = player.posy + 1
        player.posx = player.posx + 1
        refscreen()
        map_action(input("Action: "))

def move_down_left():
        player.posy = player.posy + 1
        player.posx = player.posx - 1
        refscreen()
        map_action(input("Action: "))

# menus
def help_screen_intro():
    print("""______________________________________________________
|                                                    |
|   Hello, welcome to the Help Screen.               |
|                                                    |
|   This screen will show you available commands.    |
|                                                    |
|                                                    |""")

def menu_outro():
    print("""|                                                    |
|____________________________________________________|""")
    pause = input("""


    Press ENTER to continue""")

# inventory managment

def open_inventory():
    for key in inventory:
        print("|", key, ":", inventory[key])
    menu_outro()
    refscreen()
    map_action(input("Action: "))

# actions
def map_action(a):
    if a == "a" or a == "A" or a == "4":
        move_left()
    elif a == "s" or a == "S" or a == "2":
        move_down()
    elif a == "d" or a == "D" or a == "6":
        move_right()
    elif a == "w" or a == "W" or a == "8":
        move_up()
    elif a == "9":
        move_up_right()
    elif a == "7":
        move_up_left()
    elif a == "1":
        move_down_left()
    elif a == "3":
        move_down_right()
    elif a == "i" or a == "I":
        open_inventory()
    elif a == "?":
        clear()
        help_screen_intro()
        print("""|   ?            This menu                           |
|                                                    |
|   8 / w        up                                  |
|   4 / a        left                                |
|   2 / s        down                                |
|   6 / d        right                               |
|   7            up and left                         |
|   9            up and right                        |
|   1            down and left                       |
|   3            down and right                      |
|                                                    |
|   exit         End Program (debugging console)     |""")
        menu_outro()
        refscreen()
        map_action(input("Action: "))
    # debugging tool
    elif a == "exit":
        pass
    # end tool
    else:
        refscreen()
        print("Not a valid direction/action.")
        map_action(input("Action: "))
        

# Map/Screen dict & initialization

mapx = []
screen = []
inventory = {"key": "A key", "sword": "a sword", "banana": "a banana", "Muffins": "your trusty kitty companion"}
backpack = {}
initmap()
initscreen()

# Live area

mapx[5][5] = "X" # debugging reference
mapx[player.posy + 3][player.posx + 3] = "B" # debugging reference
refscreen()
#print(len(mapx))
map_action(input("Action: "))
