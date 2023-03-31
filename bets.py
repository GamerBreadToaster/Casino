import os
def bets(bet, money, minimum_bet, bet_limit):
    exit_bets = False
    exit_bet = False
    while exit_bets == False:
        os.system('cls')
        print(f"You are betting: {bet}, minimum bet: {minimum_bet}")
        print(f"You have: {money} dollar, bet limit: {bet_limit}")
        print("how much do you want to bet? (0 for exit)")
        print("1: 1     11: -1")
        print("2: 5     12: -5")
        print("3: 10    13: -10")
        print("4: 25    14: -25")
        print("5: 50    15: -50")
        print("6: 100   16: -100")
        print("7: 500   17: -500")
        print("8: 1000  18: -1000")
        print("9: enter 19: max bet")
        print("10: clear bet")
        choice_bet = int(input("choose here: "))
        if choice_bet == 0:
            exit_bet = True
            exit_bets = True
        if choice_bet == 1:
            bet += 1
        if choice_bet == 2:
            bet += 5
        if choice_bet == 3:
            bet += 10
        if choice_bet == 4:
            bet += 25
        if choice_bet == 5:
            bet += 50
        if choice_bet == 6:
            bet += 100
        if choice_bet == 7:
            bet += 500
        if choice_bet == 8:
            bet += 1000
        if choice_bet == 10:
            bet = 0
        if choice_bet == 11:
            bet -= 1
        if choice_bet == 12:
            bet -= 5
        if choice_bet == 13:
            bet -= 10
        if choice_bet == 14:
            bet -= 25
        if choice_bet == 15:
            bet -= 50
        if choice_bet == 16:
            bet -= 100
        if choice_bet == 17:
            bet -= 500
        if choice_bet == 18:
            bet -= 1000
        if choice_bet == 19:
            bet = money
        if choice_bet == 9:
            if bet <0:
                print("dont have an negative number as bet")
            if bet > bet_limit:
                print(f"the bet limit is {bet_limit}. Don't go over it.")
                bet = 0
            if bet < minimum_bet:
                print("You have bet to little, you need to bet more.")
            if bet <= bet_limit and bet <= money and bet >= minimum_bet:
                print("bet has been set, you will continue")
                exit_bets = True
            if bet > money:
                print("you cannot bet more than you have.")
            os.system('pause')
    return bet, exit_bet