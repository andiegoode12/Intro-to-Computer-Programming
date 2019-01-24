"""
Andie Goode
9/24/15
IF: Rock Paper Scissor Judge(PY)
"""
print("Rock Paper Scissor Judge")
#collecting choice from each player
player_1 = input("Enter player 1's pick: ")
player_2 = input("Enter player 2's pick: ")

#player that chooses rock beats player that chooses scissor
if (player_1=='rock' or player_1=='r' or player_1=='Rock' or player_1=='R') and (player_2=='scissor' or player_2=='s' or player_2=='Scissor' or player_2=='S'):
    print("Player 1 wins")
elif (player_1=='scissor' or player_1=='s' or player_1=='Scissor' or player_1=='S') and (player_2=='rock' or player_2=='r' or player_2=='Rock' or player_2=='R'):
    print("Player 2 wins")
#player that chooses paper beats player that chooses rock
elif (player_1=='paper' or player_1=='p' or player_1=='Paper' or player_1=='P') and (player_2=='rock' or player_2=='r' or player_2=='Rock' or player_2=='R'):
    print("Player 1 wins")
elif (player_1=='rock' or player_1=='r' or player_1=='Rock' or player_1=='R') and (player_2=='paper' or player_2=='p' or player_2=='Paper' or player_2=='P'):
    print("Player 2 wins")
#player that chooses scissor beats player that chooses paper
elif (player_1=='scissor' or player_1=='s' or player_1=='Scissor' or player_1=='S') and (player_2=='paper' or player_2=='p' or player_2=='Paper' or player_2=='P'):
    print("Player 1 wins")
elif (player_1=='paper' or player_1=='p' or player_1=='Paper' or player_1=='P') and (player_2=='scissor' or player_2=='s' or player_2=='Scissor' or player_2=='S'):
    print("Player 2 wins")
#if players choose the same option, the game is a tie
elif (player_1=='rock' or player_1=='r' or player_1=='Rock' or player_1=='R') and (player_2=='rock' or player_2=='r' or player_2=='Rock' or player_2=='R'):
    print("Tie Game!")
elif (player_1=='paper' or player_1=='p' or player_1=='Paper' or player_1=='P') and (player_2=='paper' or player_2=='p' or player_2=='Paper' or player_2=='P'):
    print("Tie Game!")
elif (player_1=='scissor' or player_1=='s' or player_1=='Scissor' or player_1=='S') and (player_2=='scissor' or player_2=='s' or player_2=='Scissor' or player_2=='S'):
    print("Tie Game!")

