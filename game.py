from mss import mss
import cv2
from PIL import Image
import numpy as np
from time import time
import pytesseract
import re
from difflib import SequenceMatcher

mon = {'top': 479, 'left':9, 'width':340, 'height':307}

#pytesseract.pytesseract.tesseract_cmd = r'C:\Users\USER\AppData\Local\Tesseract-OCR\tesseract.exe'
sct = mss()

#extract list of players as the source of truth
player_mon = {'top': 500, 'left':606, 'width':148, 'height':235}

sct_img = sct.grab(player_mon)
img = Image.frombytes('RGB', (sct_img.size.width, sct_img.size.height), sct_img.rgb)
img_bgr = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_bgr, 127, 255, cv2.THRESH_BINARY)
thresh = cv2.bitwise_not(thresh)

player_sentences = pytesseract.image_to_string(thresh).strip().split("\n")

# cv2.imshow('test', np.array(img))
# cv2.waitKey(0)
# cv2.destroyAllWindows()

class Player:
    def __init__(self, name):
        self.name = name
        self.messages = set()
    def print(self):
        print("Name: " + self.name, "Messages: ", self.messages)
    def addMessage(self, message):
        self.messages.add(message)
        

players = {} #dictionary of players

def getPlayer(player):

    bestKey = None
    bestValue = 0

    for key in players.keys():
        value = SequenceMatcher(None, player, key).ratio()
        if value > bestValue:
            bestValue = value
            bestKey = key
    
    return players[key]


#initializing the players
for player in player_sentences:
    if len(player) != 0:
        players[player] = Player(player)

for player in players.keys():
    print(players[player])

while True:
    #begin_time = time()
    sct_img = sct.grab(mon)
    img = Image.frombytes('RGB', (sct_img.size.width, sct_img.size.height), sct_img.rgb)
    img_bgr = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(img_bgr, 127, 255, cv2.THRESH_BINARY)
    thresh = cv2.bitwise_not(thresh)
    
    
    # imgbox = pytesseract.image_to_boxes(img_bgr)
    # imgH, imgW, _ = img_bgr.shape
    # for boxes in imgbox.splitlines():
    #     boxes = boxes.split(' ')
    #     x,y,w,h = int(boxes[1]), int(boxes[2]), int(boxes[3]), int(boxes[4])
    #     cv2.rectangle(img_bgr, (x,imgH - y), (w, imgH- h), (0,0,255), 3)
    
    #cv2.imshow('test', np.array(thresh))
    #print('This frame takes {} seconds.'.format(time()-begin_time))
    sentences = pytesseract.image_to_string(thresh).strip().split("\n")
    for sentence in sentences:
        msg = sentence.split(":")
        if len(msg) == 1:
            continue
        player = getPlayer(msg[0])
        player.addMessage(msg[1])


    #print the dudes
    for player in players.keys():
        players[player].print()
    
    print("------------------- \n")
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break