# Exrecise 3:
# Tic Tac Toe Exrecise:
def TicTacToe(Mat):
    Pos = 0 # 0 represent Tie , 1 win for player 1 , 2 win for player 2
    if Mat[0][0] == Mat[1][0] == Mat[2][0] and Mat[0][0] != 0:
        Pos = Mat[0][0]
    elif Mat[0][1] == Mat[1][1] == Mat[2][1] and Mat[0][1] != 0:
        Pos = Mat[0][1]
    elif Mat[0][2] == Mat[1][2] == Mat[2][2] and Mat[0][2] != 0:
        Pos = Mat[0][2]
    elif Mat[0][0] == Mat[0][1] == Mat[0][2] and Mat[0][0] != 0:
        Pos = Mat[0][0]
    elif Mat[1][0] == Mat[1][1] == Mat[1][2] and Mat[1][0] != 0:
        Pos = Mat[1][0]
    elif Mat[2][0] == Mat[2][1] == Mat[2][2] and Mat[2][0] != 0:
        Pos = Mat[2][0]
    elif Mat[0][0] == Mat[1][1] == Mat[2][2] and Mat[0][0] != 0:
        Pos = Mat[0][0]
    elif Mat[0][2] == Mat[1][1] == Mat[2][0] and Mat[0][2] != 0:
        Pos = Mat[0][2]

    if Pos == 0:
        print("Tie")
    else:
        print("Player " + str(Pos) + " has won")
    return

def main():
	# Exrecise 3 init (player 1 win situtation):
    Mat = [[1,0,2],
           [1,0,2],
           [1,2,0]]
    TicTacToe(Mat)

if __name__ == '__main__':
    main()

