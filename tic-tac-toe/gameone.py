from playerone import HumanPlayer , RandomComputerPlayer
class TicTacToe1:
    def __init__(self):
        self.board = [" "," "," "," "," "," "," "," "," "]
        self.winner = None
    def print_board(self):
        print("insede print_board")
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print("| "+" | ".join(row)+" |")
    def available_moves(self):
        moves =[]
        for (i,spot) in enumerate(self.board):
            if spot ==" ":
                moves.append(i)
        return moves

    def makemove(self,letter,index):
        if(self.board[index]==" "):
            self.board[index]=letter
            self.print_board()
            return  True
        return False

    def finish(self,index,letter):
        
        i=index//3
        row = self.board[i*3: (i+1)*3] 

        if all([spot == letter for spot in row]):
            return True

        c=index % 3
        column = [self.board[c+i*3]for i in range(3) ]
        if all([spot == letter for spot in column]):
            return True

        if index%2 ==0:
            diagonal1 = [self.board[i] for i in [0,4,8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2,4,6]]
            if all([spot == letter for spot in diagonal2]):
                return True
            
        return False

def playgamein(gameone,x_player,o_player,printgame=True):

    player = "X"
    while gameone.winner == None :
        if player == "X":
            index = x_player.get_move(gameone)
            print(f"Player made the move {index}")
            
        if player == "O":
            index = o_player.get_move(gameone)
            print(f"Computer made the move {index}")
        
        if gameone.makemove(player,index):
            if gameone.finish(index,player):
                gameone.winner=player
                print(player + "wins")
            if player == "X":
                player = "O"
            else:
                player="X"
        li = gameone.available_moves()
        if len(li)<1:
            print("It's a tie")
            break
        




if __name__ == "__main__":
    player1 = HumanPlayer("X")
    player2 = RandomComputerPlayer("O")

    t=TicTacToe1()
    t.print_board()
    playgamein(t,player1,player2,printgame=True)

