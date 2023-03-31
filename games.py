import os,random,time

def RPC():
    win = False
    lose = False
    tied = False
    RPC_random = ["rock", "paper", "scissors"]
    choice = ""
    RPC_choice = ""
    bot = ""
    os.system('cls')
    print("Welcome to rock paper scissors")
    print("rock defeats scissors, scissors defeats paper and paper defeats rock.")
    print("choose what you want")
    print("1: rock")
    print("2: paper")
    print("3: scissors")
    print("4: random")
    choice = int(input("choose here: "))
    os.system('cls')
    if choice == 1:
        RPC_choice = "rock"
    if choice == 2:
        RPC_choice = "paper"
    if choice == 3:
        RPC_choice = "scissors"
    if choice == 4:
        RPC_choice = random.choice(RPC_random)
    print("you have chosen:", RPC_choice)
    os.system('pause')
    for a in range(random.randrange(3,6)):
        for b in RPC_random:
            os.system('cls')
            print("bot has:",b)
            time.sleep(0.25)
    time.sleep(0.75)
    os.system('cls')
    bot = random.choice(RPC_random)
    print("bot has :", bot)
    time.sleep(1)
    print("you have:", RPC_choice)
    os.system('pause')
    if RPC_choice == bot: tied = True
    if RPC_choice != bot:
        if RPC_choice == "paper" and bot == "scissors": lose = True
        if RPC_choice == "scissors" and bot == "paper" : win = True
        if RPC_choice == "rock" and bot == "paper": lose = True
        if RPC_choice == "paper" and bot == "rock": win = True
        if RPC_choice == "rock" and bot == "scissors": win = True
        if RPC_choice == "scissors" and bot == "rock": lose = True
    return tied, win, lose

def coin_flip():
    win = False
    lose = False
    H_T = 0
    bot = ""
    choice = ""
    result = ""
    H_T_random = ["heads", "tails"]
    os.system('cls')
    print("choose the side of the coin you want")
    print("if you have heads, the bot has tails")
    print("and if you have tails, then the bot has heads.")
    print("choose here:")
    print("1: heads")
    print("2: tails")
    print("3: random")
    H_T = int(input("Input here: "))
    if H_T == 1:
        choice = "heads"
        bot = "tails"
    elif H_T == 2:
        choice = "tails"
        bot = "heads"
    elif H_T == 3:
        choice = random.choice(H_T_random)
        if choice == "heads":
            bot = "tails"
        elif choice == "tails":
            bot = "heads"
    time.sleep(1)
    print("you have chosen:", choice)
    print("bot has:", bot)
    os.system("pause")
    result = random.choice(H_T_random)
    os.system('cls')
    print("side to the top is now:", result)
    for a in range(random.randrange(10,15)):
        os.system('cls')
        if result == "heads":
            result = "tails"
        else:
            result = "heads"
        print("flipping coin:")
        print(result)
        time.sleep(0.25)
    time.sleep(1)
    os.system('cls')
    print("the coin has landed on:", result)
    if result == choice:
        win = True
    if result == bot:
        lose = True
    os.system('pause')
    return win, lose
    
def slots(slot):
    small_win = False
    medium_win = False
    big_win = False
    small_big_win = False
    medium_big_win = False
    big_big_win = False
    lose = False
    win = False
    if slot == 1:
        slot_choice = ["apple", "peer", "banana"]
    if slot == 2:
        slot_choice = ["basiskader", "vmbo", "havo", "vwo"]
    for a in range(10):
        os.system('cls')
        result_1 = random.choice(slot_choice)
        print(result_1)
        time.sleep(0.25)
    print("first result")
    time.sleep(1)
    for b in range(10):
        os.system('cls')
        result_2 = (random.choice(slot_choice))
        print(result_1 + " " + result_2)
        time.sleep(0.25)
    print("second result")
    time.sleep(2)
    for c in range(9):
        os.system('cls')
        result = (result_1 + " " + result_2 + " " + random.choice(slot_choice))
        print(result)
        time.sleep(0.25)
    time.sleep(1)
    os.system('cls')
    result = (result_1 + " " + result_2 + " " + random.choice(slot_choice))
    print(result)
    time.sleep(1)
    print("last result")
    time.sleep(1)
    slot = 0
    if result.count("apple") == 2 or result.count("vmbo") == 2:
        small_win = True
        lose = True
    if result.count("apple") == 3 or result.count("vmbo") == 3:
        small_big_win = True
        win = True
    if result.count("banana") == 2 or result.count("havo") == 2:
        medium_win = True
        win = True
    if result.count("banana") == 3 or result.count("havo") == 3:
        medium_big_win = True
        win = True
    if result.count("peer") == 2 or result.count("vwo") == 2:
        big_win = True
        win = True
    if result.count("peer") == 3 or result.count("vwo") == 3:
        big_big_win = True
        win = True
    elif win != True:
        lose = True
    os.system('pause')
    
    return(
    small_win,
    medium_win,
    big_win,
    small_big_win,
    medium_big_win,
    big_big_win,
    lose,
    win
    )