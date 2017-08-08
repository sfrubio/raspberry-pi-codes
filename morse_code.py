from gpiozero import LED
from time import sleep

def dot():
    green_led.on()
    unit()
    green_led.off()
    unit()

def dash():
    green_led.on()
    unit()
    unit()
    unit()
    green_led.off()
    unit()

def unit():
    sleep(0.5)

##def morseCode(word):
##    morseCodePattern = {
##        "A" : [dot(),dash()],
##        "B" : [dash(),dot(),dot(),dot()],
##        "C" : [dash(),dot(),dash(),dot()],
##        "D" : [dash(),dot(),dot()],
##        "E" : dot(),
##        "F" : [dot(),dot(),dash(),dot()],
##        "G" : [dash(),dash(),dot()],
##        "H" : [dot(),dot(),dot(),dot()],
##        "I" : [dot(),dot()],
##        "J" : [dot(),dash(),dash(),dash()],
##        "K" : [dash(),dot(),dash()],
##        "L" : [dot(),dash(),dot(),dot()],
##        "M" : [dash(),dash()],
##        "N" : [dash(),dot()],
##        "O" : [dash(),dash(),dash()],
##        "P" : [dot(),dash(),dash(),dot()],
##        "Q" : [dash(),dash(),dot(),dash()],
##        "R" : [dot(),dash(),dot()],
##        "S" : [dot(),dot(),dot()],
##        "T" : dash(),
##        "U" : [dot(),dot(),dash()],
##        "V" : [dot(),dot(),dot(),dash()],
##        "W" : [dot(),dash(),dash()],
##        "X" : [dash(),dot(),dot(),dash()],
##        "Y" : [dash(),dot(),dash(),dash()],
##        "Z" : [dash(),dash(),dot(),dot()],
##        "1" : [dot(),dash(),dash(),dash(),dash()],
##        "2" : [dot(),dot(),dash(),dash(),dash()],
##        "3" : [dot(),dot(),dot(),dash(),dash()],
##        "4" : [dot(),dot(),dot(),dot(),dash()],
##        "5" : [dot(),dot(),dot(),dot(),dot()],
##        "6" : [dash(),dot(),dot(),dot(),dot()],
##        "7" : [dash(),dash(),dot(),dot(),dot()],
##        "8" : [dash(),dash(),dash(),dot(),dot()],
##        "9" : [dash(),dash(),dash(),dash(),dot()],
##        "0" : [dash(),dash(),dash(),dash(),dash()],
##        " " : [unit(),unit(),unit(),unit()],
##    }
##    return morseCodePattern.get(word, null)

def morseCode(word):
    if word == "A":
        return [dot(),dash()]
    elif word == "B":
        return [dash(),dot(),dot(),dot()]
    elif word == "C": 
        return [dash(),dot(),dash(),dot()]
    elif word == "D":
        return [dash(),dot(),dot()]
    elif word == "E":
        return dot()
    elif word == "F":
        return [dot(),dot(),dash(),dot()]
    elif word == "G":
        return [dash(),dash(),dot()]
    elif word == "H":
        return [dot(),dot(),dot(),dot()]
    elif word == "I":
        return [dot(),dot()]
    elif word == "J":
        return [dot(),dash(),dash(),dash()]
    elif word == "K":
        return [dash(),dot(),dash()]
    elif word == "L":
        return [dot(),dash(),dot(),dot()]
    elif word == "M":
        return [dash(),dash()]
    elif word == "N":
        return [dash(),dot()]
    elif word == "O":
        return [dash(),dash(),dash()]
    elif word == "P":
        return [dot(),dash(),dash(),dot()]
    elif word == "Q":
        return [dash(),dash(),dot(),dash()]
    elif word == "R":
        return [dot(),dash(),dot()]
    elif word == "S":
        return [dot(),dot(),dot()]
    elif word == "T":
        return dash()
    elif word == "U":
        return [dot(),dot(),dash()]
    elif word == "V":
        return [dot(),dot(),dot(),dash()]
    elif word == "W":
        return [dot(),dash(),dash()]
    elif word == "X":
        return [dash(),dot(),dot(),dash()]
    elif word == "Y":
        return [dash(),dot(),dash(),dash()]
    elif word == "Z":
        return [dash(),dash(),dot(),dot()]
    elif word == "1":
        return [dot(),dash(),dash(),dash(),dash()]
    elif word == "2":
        return [dot(),dot(),dash(),dash(),dash()]
    elif word == "3":
        return [dot(),dot(),dot(),dash(),dash()]
    elif word == "4":
        return [dot(),dot(),dot(),dot(),dash()]
    elif word == "5":
        return [dot(),dot(),dot(),dot(),dot()]
    elif word == "6":
        return [dash(),dot(),dot(),dot(),dot()]
    elif word == "7":
        return [dash(),dash(),dot(),dot(),dot()]
    elif word == "8":
        return [dash(),dash(),dash(),dot(),dot()]
    elif word == "9":
        return [dash(),dash(),dash(),dash(),dot()]
    elif word == "0":
        return [dash(),dash(),dash(),dash(),dash()]
    elif word == " ":
        return [unit(),unit(),unit(),unit()]
    else:
        return null

green_led = LED(17)
message = input()
wordList = list(message)

for word in wordList:
    print(word)
    morseCode(word)
    unit()
    unit()


