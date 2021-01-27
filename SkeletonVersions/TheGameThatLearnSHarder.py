import random
from os import system, name
from time import sleep


class Board:
        def __init__(self):
            self.board = [['X','X','X'], ['-', '-', '-'], ['O', 'O', 'O']]

        def PrintBoard(self):
            for i in range(3):
                str = ''
                for j in range(3):
                    str += self.board[i][j]
                print(str)
            print("\n")

        def MakeMove(self,moving, destination):
            team1 = self.board[moving[0]][moving[1]]

            if team1 == 'X':
                if moving[0] >= destination[0]:
                    #print("Invalid move, Try again.")
                    return -1

            if team1 == 'O':
                if moving[0] <= destination[0]:
                    #print("Invalid move, Try again.")
                    return -1

            if moving[0] < 0 or moving[1] < 0 or destination[0] < 0 or destination[1] < 0:
                return -1
            if moving[0] > 2 or moving[1] > 2 or destination[0] > 2 or destination[1] > 2:
                return -1
            if abs(destination[0] - moving[0]) > 1 or abs(destination[1] - moving[1]) > 1:
                return -1

            team2 = self.board[destination[0]][destination[1]]
            if team1 == '-' or team1 == team2:
                #print("Invalid move, Try again.")
                return -1
            elif team2 == '-':
                if moving[1] != destination[1]:
                    #print("Invalid move, Try again.")
                    return -1
                self.board[moving[0]][moving[1]] = '-'
                self.board[destination[0]][destination[1]] = team1
                return 1
            elif moving[1] == destination[1]:
                #print("Invalid move, Try again.")
                return -1
            else:
                self.board[moving[0]][moving[1]] = '-'
                self.board[destination[0]][destination[1]] = team1
                return 1

        def SimulateMove(self, moving, destination, check = False):
            temp = [[],[],[]]
            for i in range(3):
                for j in range(3):
                    temp[i].append(self.board[i][j])
            a = self.MakeMove(moving, destination)
            temp2 = [[],[],[]]
            for i in range(3):
                for j in range(3):
                    temp2[i].append(self.board[i][j])
            self.board = temp
            if check:
                return a
            return temp2

        def CheckValidMoves(self,piece, i, j):
            if piece == 'X':
                if self.board[i+1][j] == '-':
                    return True

                if j < 2:
                    if self.board[i+1][j+1] == 'O':
                        return True

                elif j > 0:
                    if self.board[i+1][j-1] == 'O':
                        return True
            elif piece == 'O':
                if self.board[i-1][j] == '-':
                    return True

                if j < 2:
                    if self.board[i-1][j+1] == 'X':
                        return True

                elif j > 0:
                    if self.board[i-1][j-1] == 'X':
                        return True
            else:
                print("Piece Error")
                return -1

            return False

        def GenerateValidMoves(self, piece):
            validBoards = []
            validMoves = []
            if piece == 'X':
                d = 1
                enemy = 'O'
            elif piece == 'O':
                d = -1
                enemy = 'X'
            else:
                print("Piece Error")
                return -1

            for i in range(3):
                for j in range(3):
                    if (i+d) < 3 and (i+d) > -1:
                        if piece == self.board[i][j]:
                            if self.board[i+d][j] == '-':
                                validBoards.append(self.SimulateMove((i,j), (i+d,j)))
                                validMoves.append(((i,j),(i+d,j)))

                            if j < 2:
                                if self.board[i+d][j+1] == enemy:
                                    validBoards.append(self.SimulateMove((i,j), (i+d,j+1)))
                                    validMoves.append(((i,j),(i+d,j+1)))
                            if j > 0:
                                if self.board[i+d][j-1] == enemy:
                                    validBoards.append(self.SimulateMove((i,j), (i+d,j-1)))
                                    validMoves.append(((i,j),(i+d,j-1)))
            return (validBoards, validMoves)

        #prevMove = 0 = cup, prevMove = 1 = player
        #return 1 = player win, return 0 = Cpu win, return -1 = noone win, return -1 = error
        def CheckVictory(self, prevMove):
            xLeft = False
            oLeft = False
            xValid = False
            oValid = False
            for i in range(3):
                for j in range(3):
                    if i == 0:
                        if self.board[i][j] == 'O':
                            #print("Congrats, You Won!")
                            return 1

                    if i == 2:
                        if self.board[i][j] == 'X':
                            #print("Oh No, The Cpu Won. Better Luck Next Time.")
                            return 0

                    if self.board[i][j] == 'X':
                        if not xValid:
                            res = self.CheckValidMoves(self.board[i][j], i, j)
                            if res == -1:
                                print("DIE")
                                return -2
                            elif res == True:
                                xValid = True
                        if not xLeft:
                            xLeft = True

                    if self.board[i][j] == 'O':
                        if not oValid:
                            res = self.CheckValidMoves(self.board[i][j], i, j)
                            if res == -1:
                                print("DIE")
                                return -2
                            elif res == True:
                                oValid = True
                        if not oLeft:
                            oLeft = True

            if not xLeft:
                #print("Congrats, You Won!")
                return 1
            if not oLeft:
                #print("Oh No, The Cpu Won. Better Luck Next Time.")
                return 0
            if prevMove == 0 or prevMove == 'X':
                if not oValid:
                    #print("Oh No, The Cpu Won. Better Luck Next Time.")
                    return 0
            if prevMove == 1 or prevMove == 'O':
                if not xValid:
                    #print("Congrats, You Won!")
                    return 1
            return -1

        def SetBoard(self, board):
            for i in range(3):
                for j in range(3):
                    self.board[i][j] = board[i][j]

        def CompareBoard(self, board):
            for i in range(3):
                for j in range(3):
                    if board[i][j] != self.board[i][j]:
                        return False
            return True

        def Reset(self):
            self.board = [['X','X','X'], ['-', '-', '-'], ['O', 'O', 'O']]

class CPU:

    def __init__(self):
            self.gameStates = [[],[],[]]
            self.validMoves = [[],[],[]]
            self.GenerateChoices()

    def GenerateChoices(self):
        g = Board()
        queue = []
        turn = [-1,-1,-1,-1,-1,-1,-1,-1]
        lis = g.GenerateValidMoves('O')
        for x in range(len(lis[0])):
            self.gameStates[0].append(lis[0][x])
            queue.append(lis[0][x])
        turn[0] += len(lis[0])
        j = 0
        i = 0
        validM = []
        while i < len(queue):
            validM = []
            if j > 5:
                break
            if (j+1)%2 == 1:
                g.SetBoard(queue[i])
                lis = g.GenerateValidMoves('X')
                for x in range(len(lis[0])):
                    g.SetBoard(lis[0][x])
                    if g.CheckVictory('X') < 0:
                        queue.append(lis[0][x])
                        turn[j+1] += 1
                    validM.append(lis[1][x])
                self.validMoves[j//2].append(validM)
            if (j+1)%2 == 0:
                g.SetBoard(queue[i])
                lis = g.GenerateValidMoves('O')
                for x in range(len(lis[0])):
                    g.SetBoard(lis[0][x])
                    if g.CheckVictory('O') < 0:
                        queue.append(lis[0][x])
                        turn[j+1] += 1
                        self.gameStates[(j+1)//2].append(lis[0][x])
            turn[j] -= 1
            if turn[j] < 0:
                j += 1
            i+=1

    def CheckBoardState(self, board, turn):
        if turn >= 3:
            print("Failed Check Board, out of bounds. Turn must be < 3")
        g = Board()
        g.SetBoard(board)
        for j in range(len(self.gameStates[turn])):
            if g.CompareBoard(self.gameStates[turn][j]):
                return j
        print("Failed")
        return -1

    def GetMove(self, board, turn, num = True):
        ran = random.randint(0, len(self.validMoves[turn][board])-1)
        mov = self.validMoves[turn][board][ran]
        movv = mov[0][0]*3 + mov[0][1] + 1
        movTo = mov[1][0]*3 + mov[1][1] + 1
        return (movv, movTo, ran, board)

    def RemoveMove(self, move):
        turn = move[0]
        index = move[2]
        board = move[1]
        self.validMoves[turn][board] = self.validMoves[turn][board][:index] + self.validMoves[turn][board][index+1:]

class Game:
    def __init__(self):
        self.cpu = CPU()
        self.board = Board()
        self.lastMover = 'X'
        self.turns = 0
        self.lastMoveIndex = -1
        self.CpuScore = 0
        self.PlayerScore = 0
        self.Input = 0

    def MakePlayerMove(self):
        print("Which piece would you like to move?")
        self.Input = input() # move from
        if self.Input == 'q':
            exit()
        frm = self.Input
        print("Where would you like to move the piece to?")
        self.Input = input() # move to
        if self.Input == 'q':
            exit()
        to = self.Input
        if len(frm) == 1 and len(to) == 1:
            if ord(frm) > ord('9') or ord(frm) < ord('1') or ord(to) > ord('9') or ord(to) < ord('1'):
                print("Invalid move, Try again.")
                return self.MakePlayerMove()
        else:
            print("Invalid move, Try again.")
            return self.MakePlayerMove()
        move = (int(frm), int(to))

        frm = move[0] - 1
        to = move[1] - 1
        idxT = [0,0]
        idxF = [0,0]

        idxF[0] = frm // 3
        idxF[1] = frm % 3

        idxT[0] = to // 3
        idxT[1] = to % 3

        if self.board.board[idxF[0]][idxF[1]] != self.lastMover and self.board.SimulateMove(tuple(idxF), tuple(idxT), True) != -1:
            self.board.MakeMove(tuple(idxF), tuple(idxT))
            self.turns += 1
            self.lastMover = self.board.board[idxF[0]][idxF[1]]
        else:
            print("Invalid move, Try again.")
            return self.MakePlayerMove()

    def MakeMove(self, move):
        frm = move[0] - 1
        to = move[1] - 1
        idxT = [0,0]
        idxF = [0,0]

        idxF[0] = frm // 3
        idxF[1] = frm % 3

        idxT[0] = to // 3
        idxT[1] = to % 3

        if self.board.board[idxF[0]][idxF[1]] != self.lastMover:
            if self.board.MakeMove(tuple(idxF), tuple(idxT)) != -1:
                self.turns += 1
                self.lastMover = self.board.board[idxF[0]][idxF[1]]
        else:
            print("Invalid move, Try again.")

    def PlayerTurn(self):
        if self.turns%2 == 0:
            return True
        return False

    def CpuTurn(self):
        if self.turns % 2 == 1:
            return True
        return False

    def RemoveLosingMove(self):
        self.cpu.RemoveMove(self.lastMoveIndex)

    def CpuWon(self):
        victory = self.board.CheckVictory('X')
        if victory == 0:
            return True
        return False

    def PlayerWon(self):
        victory = self.board.CheckVictory('O')
        if victory == 1:
            return True
        return False

    def PrintBoard(self):
        print("\n")
        mov = [[1,2,3],[4,5,6],[7,8,9]]
        for i in range(3):
            stri = ''
            for j in range(3):
                stri += self.board.board[i][j]
            print(stri + "          " +  str(mov[i]))

    def Clear(self):
        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')

    def MakeCpuMove(self):
        boardLayout = self.cpu.CheckBoardState(self.board.board, self.turns//2)
        move = self.cpu.GetMove(boardLayout, self.turns//2)
        self.lastMoveIndex = ( self.turns//2, move[3], move[2],)
        self.MakeMove((move[0], move[1]))
        return move

    def PlayerCelebrate(self):
        print("\n")
        print("Congratulations, you won!")
        print("The Current Score is: ")
        print("Cpu: ", self.CpuWins)
        print("You: ", self.PlayerWins)
        print("Press any key to start over, or q to quit")
        self.Input = input()

    def Exit(self):
        if self.Input == 'q':
            return True
        return False

    def CpuCelebrate(self):
        self.Clear()
        self.PrintBoard()
        print("\n")
        print("Oh no, you lost.")
        print("The Current Score is: ")
        print("Cpu: ", self.CpuWins)
        print("You: ", self.PlayerWins)
        print("Press any key to start over, or q to quit")
        ch = input()

    def Reset(self):
        self.board.Reset()
        self.lastMover = 'X'
        self.turns = 0

    def Play(self):
        print("Welcome to 'The game that learns' hosted by UConn Developer Student Club")
        print("You may press q to quit at any time")
        print("Press any key to continue, or q to quit")

        self.Input = input()

        #Work on the lines below. Everything else, above, is set and ready to go.

        quit()

g = Game()
g.Play()
