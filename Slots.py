import os,time,random

playerInput = ""
playerMoney=0
incorrectInput=False

def DetermineSlotOutput():
    possibleOutputs = [">","X","<","|","^"]
    output = [[0 for x in range(3)] for y in range(3)]
    for x in range(3):
        randomInt=random.randint(0, len(possibleOutputs)-1)
        output[x][0]=possibleOutputs[randomInt]
        if possibleOutputs[randomInt] == "X":
            try:
                while True:
                    possibleOutputs.remove("X")
            except ValueError:
                pass
        else:
            possibleOutputs.pop(randomInt)
            possibleOutputs.append("X")
            possibleOutputs.append("X")
            possibleOutputs.append("X")
            possibleOutputs.append("X")
            possibleOutputs.append("X")
        randomInt=random.randint(0, len(possibleOutputs)-1)
        output[x][1]=possibleOutputs[randomInt]
        if possibleOutputs[randomInt] == "X":
            try:
                while True:
                    possibleOutputs.remove("X")
            except ValueError:
                pass
        else:
            possibleOutputs.pop(randomInt)
        randomInt=random.randint(0, len(possibleOutputs)-1)
        output[x][2]=possibleOutputs[randomInt]
        possibleOutputs = [">","X","<","|","^"]
    return output
def DisplaySlotMachine(stage,output):
    if stage == 0:
        print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
            "⣿⣿⣿⣿⣿⠿⠛⠋⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠛⠛⠿⣿⣿⣿⣿⣿\n"
            "⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿\n"
            "⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿\n"
            "⣿⣿⣿⣿⣿⣿⡇⠀⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⠀⢸⣿⣿⠛⠻⣿⣿\n"
            "⣿⣿⣿⣿⣿⣿⡇⠀⣿⡇⠀⠀⢸⡇⠀⠀⢸⡇⠀⠀⢸⣿⠀⢸⣿⣿⣤⣤⣿⣿\n"
            "⣿⣿⣿⣿⣿⣿⡇⠀⣿⡇⠀⠀⢸⡇⠀⠀⢸⡇⠀⠀⢸⣿⠀⢸⣿⣿⠈⣿⣿⣿\n"
            "⣿⣿⣿⣿⣿⣿⡇⠀⣿⡇⠀⠀⢸⡇⠀⠀⢸⡇⠀⠀⢸⣿⠀⢸⣿⠁⢸⣿⣿⣿\n"
            "⣿⣿⣿⣿⣿⣿⡇⠀⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠀⢸⣿⠀⢀⣿⣿⣿\n"
            "⣿⣿⣿⣿⣿⣿⣷⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣾⣿⣦⣼⣿⣿⣿\n"
            "⣿⣿⣿⣿⡿⠋⠀⣠⣤⣤⡄⢀⣤⣤⣤⡄⠀⠀⢠⣴⣶⣶⣤⡀⠙⢿⣿⣿⣿⣿\n"
            "⣿⣿⣿⡏⠀⠀⠚⠛⠛⠛⠁⠘⠛⠛⠛⠀⠀⠀⠈⠙⠛⠛⠉⠀⠀⠀⢹⣿⣿⣿\n"
            "⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿\n"
            "⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿\n"
            "⣿⣿⣿⣿⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣿⣿⣿⣿")
    elif stage == 1:
        print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
            "⣿⣿⣿⣿⣿⠿⠛⠋⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠛⠛⠿⣿⣿⣿⣿⣿\n"
            "⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿\n"
            "⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿\n"
            "⣿⣿⣿⣿⣿⣿⡇⠀⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⠀⢸⣿⣿⠛⠻⣿⣿\n"
            "⣿⣿⣿⣿⣿⣿⡇⠀⣿⡇"+output[0][0]+"⠀⢸⡇⠀⠀⢸⡇⠀⠀⢸⣿⠀⢸⣿⣿⣤⣤⣿⣿\n"
            "⣿⣿⣿⣿⣿⣿⡇⠀⣿⡇"+output[0][1]+"⠀⢸⡇ ⠀⢸⡇ ⠀⢸⣿⠀⢸⣿⣿⠈⣿⣿⣿\n"
            "⣿⣿⣿⣿⣿⣿⡇⠀⣿⡇"+output[0][2]+"⠀⢸⡇⠀⠀⢸⡇⠀⠀⢸⣿⠀⢸⣿⠁⢸⣿⣿⣿\n"
            "⣿⣿⣿⣿⣿⣿⡇⠀⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠀⢸⣿⠀⢀⣿⣿⣿\n"
            "⣿⣿⣿⣿⣿⣿⣷⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣾⣿⣦⣼⣿⣿⣿\n"
            "⣿⣿⣿⣿⡿⠋⠀⣠⣤⣤⡄⢀⣤⣤⣤⡄⠀⠀⢠⣴⣶⣶⣤⡀⠙⢿⣿⣿⣿⣿\n"
            "⣿⣿⣿⡏⠀⠀⠚⠛⠛⠛⠁⠘⠛⠛⠛⠀⠀⠀⠈⠙⠛⠛⠉⠀⠀⠀⢹⣿⣿⣿\n"
            "⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿\n"
            "⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿\n"
            "⣿⣿⣿⣿⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣿⣿⣿⣿")
    elif stage == 2:
        print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
            "⣿⣿⣿⣿⣿⠿⠛⠋⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠛⠛⠿⣿⣿⣿⣿⣿\n"
            "⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿\n"
            "⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿\n"
            "⣿⣿⣿⣿⣿⣿⡇⠀⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⠀⢸⣿⣿⠛⠻⣿⣿\n"
            "⣿⣿⣿⣿⣿⣿⡇⠀⣿⡇"+output[0][0]+"⠀⢸⡇"+output[1][0]+"⠀⢸⡇ ⠀⢸⣿⠀⢸⣿⣿⣤⣤⣿⣿\n"
            "⣿⣿⣿⣿⣿⣿⡇⠀⣿⡇"+output[0][1]+"⠀⢸⡇"+output[1][1]+"⠀⢸⡇ ⠀⢸⣿⠀⢸⣿⣿⠈⣿⣿⣿\n"
            "⣿⣿⣿⣿⣿⣿⡇⠀⣿⡇"+output[0][2]+"⠀⢸⡇"+output[1][2]+"⠀⢸⡇⠀ ⢸⣿⠀⢸⣿⠁⢸⣿⣿⣿\n"
            "⣿⣿⣿⣿⣿⣿⡇⠀⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠀⢸⣿⠀⢀⣿⣿⣿\n"
            "⣿⣿⣿⣿⣿⣿⣷⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣾⣿⣦⣼⣿⣿⣿\n"
            "⣿⣿⣿⣿⡿⠋⠀⣠⣤⣤⡄⢀⣤⣤⣤⡄⠀⠀⢠⣴⣶⣶⣤⡀⠙⢿⣿⣿⣿⣿\n"
            "⣿⣿⣿⡏⠀⠀⠚⠛⠛⠛⠁⠘⠛⠛⠛⠀⠀⠀⠈⠙⠛⠛⠉⠀⠀⠀⢹⣿⣿⣿\n"
            "⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿\n"
            "⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿\n"
            "⣿⣿⣿⣿⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣿⣿⣿⣿")
    elif stage == 3:
        print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
            "⣿⣿⣿⣿⣿⠿⠛⠋⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠛⠛⠿⣿⣿⣿⣿⣿\n"
            "⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿\n"
            "⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿\n"
            "⣿⣿⣿⣿⣿⣿⡇⠀⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⠀⢸⣿⣿⠛⠻⣿⣿\n"
            "⣿⣿⣿⣿⣿⣿⡇⠀⣿⡇"+output[0][0]+"⠀⢸⡇"+output[1][0]+"⠀⢸⡇"+output[2][0]+"⠀⢸⣿⠀⢸⣿⣿⣤⣤⣿⣿\n"
            "⣿⣿⣿⣿⣿⣿⡇⠀⣿⡇"+output[0][1]+"⠀⢸⡇"+output[1][1]+"⠀⢸⡇"+output[2][1]+"⠀⢸⣿⠀⢸⣿⣿⠈⣿⣿⣿\n"
            "⣿⣿⣿⣿⣿⣿⡇⠀⣿⡇"+output[0][2]+"⠀⢸⡇"+output[1][2]+"⠀⢸⡇"+output[2][2]+"⠀⢸⣿⠀⢸⣿⠁⢸⣿⣿⣿\n"
            "⣿⣿⣿⣿⣿⣿⡇⠀⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠀⢸⣿⠀⢀⣿⣿⣿\n"
            "⣿⣿⣿⣿⣿⣿⣷⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣾⣿⣦⣼⣿⣿⣿\n"
            "⣿⣿⣿⣿⡿⠋⠀⣠⣤⣤⡄⢀⣤⣤⣤⡄⠀⠀⢠⣴⣶⣶⣤⡀⠙⢿⣿⣿⣿⣿\n"
            "⣿⣿⣿⡏⠀⠀⠚⠛⠛⠛⠁⠘⠛⠛⠛⠀⠀⠀⠈⠙⠛⠛⠉⠀⠀⠀⢹⣿⣿⣿\n"
            "⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿\n"
            "⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿\n"
            "⣿⣿⣿⣿⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣿⣿⣿⣿")
    

def AdjustBalance(profit):
    currentMoney+=profit

def ClearConsole():
    for i in range(50):
        print("\n")

def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

ClearConsole()
slotOutput=DetermineSlotOutput()
print("Welcome to The Casino (TM). Time to buy in! How much ya lookin for?")
print("1=100, 2=1,000, 3=5,000, 4=10,000, 5=100,000")
while True:
    if incorrectInput == True:
        print("Hey buddy, do you not know how to follow directions? Gotta enter a value between 1-5")
    playerInput = input()
    if (RepresentsInt(playerInput)==False or int(playerInput) <1 or int(playerInput) >5):
        incorrectInput = True
    else:
        incorrectInput = False
        break
match playerInput:
    case "1":
        print("A beginner huh? Here ya go")
        playerMoney=100
    case "2":
        print("Just dippin your toes in huh? Makes it a little exciting. Enjoy")
        playerMoney=1000
    case "3":
        print("Now don't do anything crazy like go all in immediately")
        playerMoney=5000
    case "4":
        print("A seasoned vet? Or just have too much money? Just kiddin")
        playerMoney=10000
    case "5":
        print("Alright Mr. Money Bags, chill out. Throw a lil tip my way maybe ha")
        playerMoney=100000
    case _:
        print("Something is very wrong here")
time.sleep(3)
ClearConsole()
print("Current Balance: " + str(playerMoney))

currentBet = 10
while True:
    ClearConsole()
    slotOutput=DetermineSlotOutput()
    print("Current Balance: " + str(playerMoney))
    DisplaySlotMachine(0,slotOutput)
    if playerMoney < 10:
        print("Sorry, you are just too poor to play. NEXT")
        time.sleep(3)
        break
    print("Enter amount you wish to bet. Or press anything else to use current bet. 10 minimum. Q to exit")
    print("Current Bet: " + str(currentBet))
    while True:
        playerInput = input()
        if playerInput == "Q" or playerInput == "q":
            break
        time.sleep(1)
        if RepresentsInt(playerInput)==True and int(playerInput) > 9 and playerMoney >= int(playerInput):
            incorrectInput = False
            currentBet = int(playerInput)
            break
        elif RepresentsInt(playerInput)==True:
            if int(playerInput) < 10:
                incorrectInput = True
                print("Hey man, you better read more carefully. 10 is the minimum bet")
            elif playerMoney < int(playerInput):
                print("How are you gonna try to bet more than you have? Fake rich, try again")
                incorrectInput = True
        else:
            if playerMoney < int(currentBet):
                print("How are you gonna try to bet more than you have? Fake rich, try again")
                incorrectInput = True
            else:
                break
    if playerInput == "Q" or playerInput =="q":
        sys.exit("")
    if playerMoney < currentBet:
        print("Sorry, you are just too poor to play. NEXT")
        time.sleep(3)
        sys.exit("")
    playerMoney-=currentBet
    time.sleep(1)
    ClearConsole()
    print("Current Balance: " + str(playerMoney))
    DisplaySlotMachine(1,slotOutput)
    time.sleep(1)
    ClearConsole()
    print("Current Balance: " + str(playerMoney))
    DisplaySlotMachine(2,slotOutput)
    time.sleep(1)
    ClearConsole()
    print("Current Balance: " + str(playerMoney))
    DisplaySlotMachine(3,slotOutput)
    if slotOutput[0][1] == "X" and slotOutput[1][1] == "X" and slotOutput[2][1] == "X":
        print("WINNER WINNER BABY!!")
        playerMoney+=currentBet*9
    else:
        print ("LOOOOOSER")
    time.sleep(3)
