
from player import HumanPlayer,RandomComputerPLayer


class TicTacToe:
    def __init__(self):
        self.board = [ " " , " " , " " , " " , " " , " " , " " , " " , " "]
        self.current_winner = None

    def print_board(self):
        for row in [self.board [i*3:(i+1)*3] for i in range(3)]:
            print('| '+' | '.join(row) +' |')
#=============================================================================
    @staticmethod 
    def print_board_nums():
         number_board = [[str(i) for i in range(j*3,(j+1)*3)] for j in range(3)]
         for row in number_board:
            print('| '+' | '.join(row)+' |')
#=============================================================================
    def available_moves(self):
        moves = []
        for(i,spot) in enumerate(self.board):
            if spot == " ":
                moves.append(i)
        return moves

#==============EMPTY SQUARES=============================================================================

    def empty_squares(self):
        return " " in self.board
#=============================================================================   
    def num_empty_square(self):
        return self.board.count(" ")
#=============================================================================
    def make_move(self, square,letter):
        print("entered make_move")
        if self.board[square] == " ":
            print("entered condition")
            self.board[square] = letter
            for x in range(len(self.board)):
                print(self.board[x])
            if self.winner(square,letter):
                self.current_winner = letter
            return True
        return False
#=============================================================================        
    def winner (self,square,letter):
        row_ind = square // 3
        row = self.board[row_ind*3: (row_ind +1)*3]
        if all([spot == letter for spot in row]):
            return True

        #check column
        col_ind = square % 3
        column = [self.board [col_ind+i*3]for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        #checl diagonals
        #but only if the square is an even number (0,2,4,6,8)
        #these are the only moves possib;le to win a diagonal
        if square %2==0:
            diagonal1=[self.board[i]for i in [0,4,8]]
            if all([spot == letter for spot in diagonal1]):
                return True
      
            diagonal2=[self.board[i]for i in [2,4,6]]
            if all([spot == letter for spot in diagonal2]):
                return True
        #if all checks fail 
        return False
    
            


#=============================================================================
#=============================================================================
def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()

    letter = 'X'

    while game.empty_squares():
        if letter =='O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square,letter):
            if print_game:
                print(letter + f"make a move to square {square}")
                game.print_board()
                print(" ")
            
            if game.current_winner:
                if print_game:
                    print(letter + "wins")
                return letter
            print("going to change players")
            if letter == "X":
                letter = "O"
            else:
                letter = "X"
    if print_game:
        print("It's a tie ")
#=============================================================================
if __name__=='__main__':
    x_player = HumanPlayer('X')
    o_player = RandomComputerPLayer('O')
    t=TicTacToe()
    t.print_board()
    play(t, x_player, o_player,print_game=True)