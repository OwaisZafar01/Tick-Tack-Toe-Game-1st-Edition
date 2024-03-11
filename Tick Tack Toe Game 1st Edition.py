#Tick Tack Toe Game

#IMAGINE 1 IS PLAYER 1 AND 2 IS PLAYER 2 IF 1 WIN MEANS PLAYER 1 WIN SIMILARLY 2 WIN MEANS PLAYER 2 WINS


game=[[1,2,1],[2,1,1],[1,1,2]]

if game[0][0]==game[0][1]==game[0][2]:
    print("PLAYER",game[0][0],"won")

elif game[1][0]==game[1][1]==game[1][2]:
    print("PLAYER",game[1][0],"won")

elif game[2][0]==game[2][1]==game[2][2]:
    print("PLAYER",game[2][0],"won")

elif game[0][0]==game[1][0]==game[2][0]:
    print("PLAYER",game[0][0],"won")

elif game[0][1]==game[1][1]==game[2][1]:
    print("PLAYER",game[0][1],"won")

elif game[0][2]==game[1][2]==game[2][2]:
    print("PLAYER",game[0][2],"won")

elif game[0][0]==game[1][1]==game[2][2]:
    print("PLAYER",game[0][0],"won")

elif game[2][0]==game[1][1]==game[0][0]:
    print("PLAYER",game[2][0],"won")

else:
    print("GAME DRAW")






