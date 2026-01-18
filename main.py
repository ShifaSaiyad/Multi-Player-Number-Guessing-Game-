import random

def game1():

    player_1_score = 0
    player_2_score = 0
    player = 1

    for i in [1,2]:
        n = random.randint(1,100)
        print(f"player {player}' turn")
        attemps=0
        #player = ++1
        a = -1

        while(n != a):
            a = int(input("Gauess the Number bitween 1 to 100 : "))
            attemps += 1
            if n>a:
                print("higher Number please ")
            elif n<a:
                print("lower Number please ")
          
        print(f"player {player} Win!! find {n} number in {attemps} attemps")
        if player == 1:
            player_1_score = attemps
        else:
            player_2_score = attemps
        player +=1

    #winner Logic 
    if player_1_score < player_2_score:
        print(f"______player 1 is winner with {player_1_score} attemps_____")
    elif player_1_score > player_2_score:
        print(f"_____player 2 is winner with {player_2_score} attemps_____")
    else:
        print("_____it's TIE!!, Try again_____")
        
game1()



