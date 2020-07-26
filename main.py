import random as rd
class OxGame:
    def __init__(self, ):

        self.r = int()
        self.c = int()
        self.space = " " * 45
        self.grid_x = self.space + ("-" * 15)
        self.grid_y = "| "
        
        self.rc_name = ["  | 1 | 2 | 3 |",
                        ['1', '2', '3']]

        self.element = [['-'] * 3, 
                        ['-'] * 3, 
                        ['-'] * 3] 
        self.history = [[0] * 3, 
                        [0] * 3, 
                        [0] * 3] 

        self.message = ["\n: You have been taking This Positon !!\n  PLEASE TRY AGAIN...\n",
                         "\n: Your Enemy has been taking This Positon !!\n  PLEASE TRY AGAIN...\n",
                         "\n: PLAYER 1 VICTORY!!!\n",
                         "\n: PLAYER 2 VICTORY!!!\n",
                         f"{'=' * 10} !!!DRAW!!! {'=' * 10}"]

        self.marks = ['O', 'X']
        self.next_turn = rd.randint(1,2)

   

    def start(self,):
        print(f'{self.space}{"=" * 15}')
        print(f"{self.space} THE OX GAME!!")
        print(f'{self.space}{"=" * 15}\n')

        self.draw_board()

    def draw_board(self, ):
        
        print(f'{self.space}{self.rc_name[0]}\n')
        for i in range(len(self.element)): #draw each line
            print(f'{self.space}{self.rc_name[1][i]} ',end= self.grid_y)
            for j in range(len(self.element)):
                print(self.element[i][j],end= f' {self.grid_y}') #add init. shape
            
            print(f'\n{self.grid_x}') #draw x_axis grid

        checked = self.isVictory()
        if(checked == 1 or checked == 2):
            quit()

        if(self.next_turn == 1):
            self.playerOne()
        else:
            self.playerTwo()
        

    def playerOne(self, ):
        print("=" * 9)
        print("Player 1:")
        print("=" * 9)
        #Get inputs of ROW and COLOMN to locate the box player want to play  
        self.r = int(input("Row: "))
        self.c = int(input("Column: "))
        
        self.isDuplicate()
        self.element[self.r-1][self.c-1] = self.marks[0]

        if(self.isVictory() == 1):
            self.draw_board()

        self.next_turn = 2
        self.draw_board()
    
    def playerTwo(self, ):
        print("=" * 9)
        print("Player 2:")
        print("=" * 9)
        self.r = int(input("Row: "))
        self.c = int(input("Column: "))
        
        self.isDuplicate()
        self.element[self.r-1][self.c-1] = self.marks[1]
        self.next_turn = 1
        self.draw_board()
        
    def isDuplicate(self, ):
        if(self.next_turn == 1):
            if(self.element[self.r-1][self.c-1] == 'O'):
                print(self.message[0])
                self.playerOne()
            elif(self.element[self.r-1][self.c-1] == 'X'):
                print(self.message[1])
                self.playerOne()
            else:
                return 0
        else:
            if(self.element[self.r-1][self.c-1] == 'X'):
                print(self.message[0])
                self.playerTwo()                
            elif(self.element[self.r-1][self.c-1] == 'O'):
                print(self.message[1])
                self.playerTwo()
            else:
                return 0
                
    def isVictory(self, ):
        #winnig cases
        game_over = 0
        e = self.element
        #check if either player 1 or player 2
        if(self.next_turn == 1):
            sym = self.marks[0]
            mes = self.message[2]
        else:
            sym = self.marks[1]
            mes = self.message[3]

            #- - -
            #O O O
            #- - -
        if(e[1][0] == sym and e[1][1] == sym and e[1][2] == sym):
            game_over = 1

            #- - -
            #- - -
            #O O O
        elif(e[2][0] == sym and e[2][1] == sym and e[2][2] == sym):
            game_over = 1

        elif(e[0][0] == sym ): 
            #O O O
            #- - -
            #- - -
            if(e[0][1] == sym and e[0][2] == sym):
                game_over = 1

            #O - -
            #O - -
            #O - -
            elif(e[1][0] == sym and e[2][0] == sym):
                game_over = 1

            #O - -
            #- O -
            #- - O
            elif(e[1][1] == sym and e[2][2] == sym):
                game_over = 1

        elif(e[0][1] == sym):       
            #- O -
            #- O -
            #- O -
            if(e[1][1] == sym and e[2][1] == sym):
                game_over = 1

        elif(e[0][2] == sym):
            #- - O
            #- - O
            #- - O
            if(e[1][2] == sym and e[2][2] == sym):  
                game_over = 1

            #- - O
            #- O -
            #O - -
            elif(e[1][1] == sym and e[2][0] == sym):
                game_over = 1   

        #Draw case
        if('-' in e[0] or '-' in e[1] or '-' in e[2]):
            pass
        else:    
            print(self.message[4])  
            return 2
               
        #Does match some case                       
        if(game_over == 1):
            print(mes)
            return 1
        #Doesn't match any case
        elif(game_over == 0):
            return 0

game = OxGame()
game.start()




