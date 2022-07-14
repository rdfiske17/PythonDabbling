import random
cards = ["A♠","2♠","3♠","4♠","5♠","6♠","7♠","8♠","9♠","10♠","J♠","Q♠","K♠","A♥","2♥","3♥","4♥","5♥","6♥","7♥","8♥","9♥","10♥","J♥","Q♥","K♥","A♣","2♣","3♣","4♣","5♣","6♣","7♣","8♣","9♣","10♣","J♣","Q♣","K♣","A♦","2♦","3♦","4♦","5♦","6♦","7♦","8♦","9♦","10♦","J♦","Q♦","K♦"]
playerHand = []
dealerHand = []

def shuffleDeck():
    global cards
    random.shuffle(cards)

def initialDeal(pCardSet,dCardSet):
    card1 = drawCard(); pCardSet.append(card1)
    card2 = drawCard(); dCardSet.append(card2)
    card3 = drawCard(); pCardSet.append(card3)
    card4 = drawCard(); dCardSet.append(card4)
    

def drawCard():
    global  cards
    keepDrawing = True
    while keepDrawing:
        if len(cards) > 0:
            newCard = cards.pop(0)
            keepDrawing=False
        else:
            print("Ran out of cards. Reshuffling Deck.")
            cards = ["A♠","2♠","3♠","4♠","5♠","6♠","7♠","8♠","9♠","10♠","J♠","Q♠","K♠","A♥","2♥","3♥","4♥","5♥","6♥","7♥","8♥","9♥","10♥","J♥","Q♥","K♥","A♣","2♣","3♣","4♣","5♣","6♣","7♣","8♣","9♣","10♣","J♣","Q♣","K♣","A♦","2♦","3♦","4♦","5♦","6♦","7♦","8♦","9♦","10♦","J♦","Q♦","K♦"]
            for x in playerHand:
                cards.remove(x)
            for x in dealerHand:
                cards.remove(x)
            shuffleDeck()
    return newCard

def printHand(hand):
    largeString = ""
    for x in hand:
        largeString = largeString + x
    return largeString

def hit(hand):
    newCard = drawCard()
    hand.append(newCard)    

def canKeepPlaying(hand):
    n = checkValue(hand)
    bool = False
    if n < 21:
        bool = True
    return bool

def checkValue(hand):
    sum = 0
    for x in hand:
        if "2" in x:
            sum = sum + 2
        elif "3" in x:
            sum = sum + 3
        elif "4" in x:
            sum = sum + 4
        elif "5" in x:
            sum = sum + 5
        elif "6" in x:
            sum = sum + 6
        elif "7" in x:
            sum = sum + 7
        elif "8" in x:
            sum = sum + 8
        elif "9" in x:
            sum = sum + 9
        elif "10" in x or "J" in x or "Q" in x or "K" in x:
            sum = sum + 10
    
    totalAs=0
    for x in hand:
        if "A" in x:
            totalAs = totalAs + 1

    if sum + 11 + totalAs - 1 > 21:
        sum = sum + totalAs
    else:
        sum = sum + 11 + totalAs - 1
    
    return sum       

def dealerMove(dHand):
    while checkValue(dHand) < 17:
        hit(dHand)

def play():
    shuffleDeck()
    print(cards)
    playgame = True
    playerChips = 100
    wagerAmt=0
    print("Welcome to BlackJack!")
    wagerAmt = input("You have " + str(playerChips) + " chips. How many would you like to wager?\n")
    wagerAmt = int(wagerAmt)
    while wagerAmt < 0 or wagerAmt > playerChips:
        wagerAmt = input("Invalid amount. Please try again using positive numbers less than or equal to your total.\n")
        wagerAmt = int(wagerAmt)
    while(playgame):
        #print(cards)
        playerHand=[]
        dealerHand=[]
        initialDeal(playerHand,dealerHand)
        notStayed = True
        while checkValue(playerHand) < 21 and checkValue(dealerHand) != 21 and notStayed:
            playerInput = input("Dealer has " + dealerHand[0] + "\nYou have " + printHand(playerHand) + "\nHit or stay?\n")
            if playerInput == "Hit" or playerInput == "hit":
                hit(playerHand)
            elif playerInput == "Stay" or playerInput == "stay":
                notStayed = False
            else:
                print("Misunderstood Input.")
        if checkValue(playerHand) > 21:
            print("You went over 21 and lost! (Your Final Hand: " + printHand(playerHand) + " vs. Dealer Final Hand: " + printHand(dealerHand) + ")")
            playerChips = playerChips - wagerAmt
        else:
            dealerMove(dealerHand)
            finalHands = "(Your Final Hand: " + printHand(playerHand) + " vs. Dealer Final Hand: " + printHand(dealerHand) + ")"
            if checkValue(dealerHand) > 21:
                print("The dealer went over 21 and lost! " + finalHands)
                playerChips = playerChips + wagerAmt
            elif checkValue(playerHand) == checkValue(dealerHand):
                print("It's a draw! " + finalHands)
            elif checkValue(playerHand) > checkValue(dealerHand):
                print("Congratulations! You beat the dealer!" + finalHands)
                playerChips = playerChips + wagerAmt
            else:
                print("The dealer beat you. (Your Final Hand: " + finalHands)
                playerChips = playerChips - wagerAmt
        if playerChips == 1:
            print("You currently have " + str(playerChips) + " chip remaining.")    
        else:
            print("You currently have " + str(playerChips) + " chips remaining.")
        pInput = ""
        while pInput != "Yes" and pInput != "yes" and pInput != "no" and pInput != "No" and playerChips > 0:
            pInput = input("Play Again?\n")
        if pInput == "no" or pInput == "No" or playerChips <= 0:
            playgame=False
        else:
            wagerAmt = input("How many chips would you like to wager?\n")
            wagerAmt = int(wagerAmt)
            while wagerAmt < 0 or wagerAmt > playerChips:
                wagerAmt = input("Invalid amount. Please try again using positive numbers less than or equal to your total.\n")
                wagerAmt = int(wagerAmt)
        notStayed = True
    print("You walked away with " + str(playerChips) + " chips. Thanks for playing!")
play()