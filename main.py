# made by GamerBreadToaster
# for more go to https://github.com/GamerBreadToaster/

# imports
import os,random,time
from games import slots, coin_flip, RPC
from bets import bets

# variables
# player data
money = 0
wins = 0
loses = 0
GameOver = False
bet = 0
games_played = 0
money_won = 0
money_lost = 0
money_won_total = 0
money_lost_total = 0
time_played_begin = time.time()
# winning
small_win = False
medium_win = False
big_win = False
small_big_win = False
medium_big_win = False
big_big_win = False
lose = False
exit_bets = False
# save file
path = "SafeFile.txt"
path_gamestats = "Game stats.txt"
path_time_played = "time played.txt"
games_played += 1

def clear_and_see(): # this def makes it clear how much money, wins and loses you have.
    os.system('cls') # clearing
    print("money:", money, "| wins :", wins)       # 
    print("bet  :", bet, "| loses:", loses)        # 
    print("total games played:", games_played)     # this is to display most of your stats
    print("total money won   :", money_won_total)  # 
    print("total money lost  :", money_lost_total) # 
    print(" ") # to make some space

def save(): # a define for saving to make it easier to save.
    with open(path, "w") as file: # opens save file
        file.write(f"{money:.0f}\n{bet:.0f}\n{wins:.0f}\n{loses:.0f}\n{money_won_total:.0f}\n{money_lost_total:.0f}\n{games_played:.0f}") # writes the money, wins and loses in the SafeFile.txt
        
for b in range(2):
    if os.path.isfile(path): # to search for the save file at je beginning of the program
        with open(path, "r") as file: # opens the safe file
            readlines = file.readlines() # reads all the lines
            
    else: # if there is no file it will make one
        money = 500 # beginning money
        time_played_total = 0
        save()

# reads the lines to assign the money, wins and loses to the player.
money = int(readlines[0])
bet = int(readlines[1])
wins = int(readlines[2])
loses = int(readlines[3])
money_won_total = int(readlines[4])
money_lost_total = int(readlines[5])
games_played = int(readlines[6])

# the beginning of the programm
while GameOver == False: # so the program will always continue until gameover
    clear_and_see() # this makes the terminal clear and shows money, bet, wins and loses
    save()
    print("choose your room")
    print("0: exit program")
    print("1: minigames")
    print("2: slots")
    choose = int(input("choose here: ")) # here you chose what you want to do
    
    if choose == 0: # saves and exits the terminal
        save()
        break
    
    # minigames
    while choose == 1: # fully done, is the minigame
        if money <= 0: # checks if money is or is under 0.
            GameOver = True # makes GameOver True and after breaks to exit program
            break
        
        clear_and_see()
        save()
        print("choose what slot you want to do")
        print("0: exit")
        print("1: coin flip")
        print("2: rock paper scissors")
        minigame = int(input("put in here: ")) # here you can choose what type of minigame you want to do.
        
        if minigame == 0: # if you choose 0 it will exit the minigame and go to the main.
            break

        if minigame == 1:
            bet, exit_bet = bets(bet, money, 1, 500) # here it gives the bets import the amount you've alreade bet, your money, bet minimum and bet limit.

        if minigame == 2:
            bet, exit_bet = bets(bet, money, 1, 500) # same here as with above.
            
        if exit_bet == True:
            break
        
        money -= bet # after you have bet the money you have will be subtracted from the bet.
        money_lost = bet # dont know why its here, but it works so i won't touch it
        exit_bets = False
        
        if minigame == 1: # this is the coin flipping
            
            win, lose = coin_flip() # for returning if there is an win or lose
            
            # if you have won from the bot
            if win == True:
                wins += 1           # 
                games_played += 1   # for counting
                money_won = bet * 2 # to make sure you get your money back
                money += money_won  # gives you the money
                money_won = bet / 2 # to correct the amount of money you actually won
                clear_and_see()
                print("you have won!")
                print("your bet has been doubled")
                print("you won the amount of:", (money_won * 2)) # so you can see how much you have won
            
            # if you lose from the bot
            if lose == True:
                loses += 1        # 
                games_played += 1 # more counting
                clear_and_see()
                money_lost = bet  # repeat? won't touch it because it just works
                print("you lost :(")
                print("and you have lost:", money_lost)   # to visualise the amount of money you lost
                print("your bet is now in the backrooms") # haha funny
            money_won_total += money_won   #
            money_lost_total += money_lost # for counting
            os.system('pause') # pauses so you can actually see what there is on screen
        
        # Rock Paper Scissors
        if minigame == 2:
        
            # basically all the same as above exept you can tie with the bot
            tied, win, lose = RPC()
            if win == True:
                wins += 1
                games_played += 1
                money_won = bet * 2
                money += money_won
                money_won = bet / 2
                clear_and_see()
                print("you have won!")
                print("your bet has been doubled")
                print("you won the amount of:", (money_won * 2))
            if lose == True:
                loses += 1
                games_played += 1
                clear_and_see()
                money_lost = bet
                print("you lost :(")
                print("and you have lost:", money_lost)
                print("your bet is now in the backrooms")
            if tied == True:
                games_played += 1
                money_lost = bet
                money += money_lost # corrected mistake
                money_lost = 0 # you dont actually lose money if you tie, so the amount lost is actually 0 then.
                clear_and_see()
                print("You have tied with the bot")
                print("you get your bet back")
            money_won_total += money_won
            money_lost_total += money_lost
            os.system('pause')
            
    
    # slot machines
    while choose == 2:
        if money <= 0: # checks if money is or is under 0.
            GameOver = True # makes GameOver True and after breaks to exit program
            break
        
        clear_and_see()
        save()
        print("choose what slot you want to do")
        print("0: exit")
        print("1: fruit slot - medium risk, medium reward")
        print("2: Dutch school system - high risk, high reward")
        slot = int(input("put in here: ")) # here you can choose what type of slots you want to do.
        
        if slot == 0: # if you choose 0 it will exit the slots and go to the main.
            break
        if slot == 1:
            bet, exit_bet = bets(bet, money, 50, 1000) # here it gives the bets import the amount you've alreade bet, your money, bet minimum and bet limit.
        if slot == 2:
            bet, exit_bet = bets(bet, money, 1000, 5000) # same here as with above.
        if exit_bet == True:
            break
        money -= bet # after you have bet the money you have will be subtracted from the bet.
        money_lost = bet
        exit_bets = False
        (
            small_win,
            medium_win,
            big_win,
            small_big_win,
            medium_big_win,
            big_big_win,
            lose,
            win
            ) = slots(slot)
        money_lost = 0
        money_won = 0
        
        if small_win == True:
            if slot == 2:
                money_won += bet * 1
            if slot == 1:
                money_lost += bet * 0.5
            clear_and_see()
            print("you have won half of your bet back")
            os.system('pause')
            
        if small_big_win == True:
            money_won += bet * 1
            clear_and_see()
            print("you have won your bet back")
            os.system('pause')
            
        if medium_win == True:
            money_won += bet * 1.5
            clear_and_see()
            print("you have won your bet times 1.5")
            os.system('pause')
            
        if medium_big_win == True:
            money_won += bet * 2
            clear_and_see()
            print("you have won your bet times 2")
            os.system('pause')
            
        if big_win == True:
            money_won += bet * 2.5
            clear_and_see()
            print("you have won your bet times 2.5")
            os.system('pause')
            
        if big_big_win == True:
            money_won += bet * 3
            clear_and_see()
            print("you have won your bet times 3")
            os.system('pause')
            
        if win == True:
            wins += 1
            games_played += 1
            
        if lose == True:
            games_played += 1
            loses += 1
            if small_win == False:
                money_lost += bet
            if small_win == True:
                money = money + money_lost
            clear_and_see()
            print("you have lost (some of) your money :(")
            print("you have lost:", money_lost)
            os.system('pause')
        
        if slot == 2 and lose == False:
            clear_and_see()
            print("Because you have spun the Dutch school system,")
            print("You have won the money you won, times 1.5")
            money_won *= 1.5
            money = money + money_won
            print("You have won:", money_won)
            os.system('pause')
            money_won -= bet
        
        if slot == 1 and lose == False:
            clear_and_see()
            print("You have won:", money_won)
            money = money + money_won
            os.system('pause')
            money_won -= bet
            
        money_lost_total += money_lost
        money_won_total += money_won

time_played_end = time.time()
time_played_total = time_played_end - time_played_begin

if os.path.isfile(path_time_played) == True: # dont ask me how it works,
    with open(path_time_played, "r") as file: # it just does.
        read_time = file.readlines()
    time_played_file = int(read_time[0])
    time_played_total = time_played_total + time_played_file
    with open(path_time_played, "w") as file:
        file.write(f"{time_played_total:.0f}")
else:
    with open(path_time_played, "w") as file:
        file.write(f"{time_played_total:.0f}")
        
if GameOver == True:
    with open(path_time_played, "r") as file:
        read_time = file.readlines()
    time_played_file = int(read_time[0])
    if os.path.isfile(path_gamestats):
        with open(path_gamestats, "a") as file:
            file.write(
                f"times won : {wins:.0f}\ntimes lost: {loses:.0f}\ntimes played: {games_played:.0f}\nmoney won : {money_won_total:.0f}\nmoney lost: {money_lost_total:.0f}\ntotal play time: {time_played_file:.0f} seconds\n\n"
                )
    else:
        with open(path_gamestats, "w") as file:
            file.write(
                f"|| welcome to your game stats ||\n\ntimes won : {wins:.0f}\ntimes lost: {loses:.0f}\ntimes played: {games_played:.0f}\nmoney won : {money_won_total:.0f}\nmoney lost: {money_lost_total:.0f}\ntotal play time: {time_played_total:.0f} seconds\n\n"
                )
    with open(path, "w") as file:
        file.write(f"{500:.0f}\n{0:.0f}\n{0:.0f}\n{0:.0f}\n{0}\n{0}\n0")
    with open(path_time_played, "w") as file:
        file.write("0")
    print("You lost :(")
    print("your game stats are in Game stats.txt")
    os.system('pause')
