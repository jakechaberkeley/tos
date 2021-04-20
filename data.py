#given a "sentence", get meaningful information out of it

players = [] #list of players


while True:
    sentence = input("Input the next sentence: ")

    #start by categorizing the sentence
    msg = sentence.split(":")
    if len(msg) == 1:
        print("Not a player!")
        continue
    print(msg[0]) #player
    print(msg[1]) #contents

    #pseudo-code
    player = findPlayer(msg[0])
    if not player:
        print("Error, no player of this name was found!")
    player.addMessage(msg[1])
    
    def findPlayer(name):
        #given the name, find the player. If not found, return false
        #might want to do some fuzzy search to account for OCR errors
    
    def addMessage(self, message):
        #class method
        #append the message to the player. This will be a set to ensure that duplicate data is not inputted





