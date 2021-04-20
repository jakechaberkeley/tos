class Player:
    def __init__(self, number, name):
        self.number = number
        self.name = name
        self.role = False
        self.sus = False
        self.dead = False
    def setRole(self, role):
        self.role = role
    def fDead(self):
        self.dead = not self.dead

playersList = []
line = "----------------------------\n"
debug = False
debug_list = [
    "Jake",
    "John",
    "Kenton",
    "Eileen",
    "Kenneth",
    "Andrea",
    "Ace",
    "Kayla",
    "Smith",
    "Tom",
    "Robert",
    "Daisy",
    "Mario",
    "Luigi",
    "Waluigi"
]
#init the players
if not debug:
    for i in range(15):
        index = i + 1
        playersList.append(Player(index, input("Name of Player " + str(index) + ": ").lower()))
else :
    for i in range(15):
        index = i + 1
        playersList.append(Player(index, debug_list[i].lower()))

def printStatus():
    for player in playersList:
        if not player.dead and player.role:
            lst = [str(player.number) + ")" + str(player.name), "claims", str(player.role)]
            print(" ".join(lst))

def getPlayerByName(name):
    for player in playersList:
        if player.name == name:
            return player
    return False

print("\n")
printStatus()
print(line)

while True:
    phrase = input()
    print("\n")
    #player role role_name
    #player sus
    #player dead
    commands = phrase.split(" ")
    player = getPlayerByName(commands[0])
    if commands[0] == "exit":
        break
    if not player:
        print("Player not found")
        continue
    if commands[1] == "role":
        player.setRole(commands[2])
    elif commands[1] == "dead":
        player.fDead()
    else:
        print("Command not found")
    printStatus()
    print(line)


    

    
