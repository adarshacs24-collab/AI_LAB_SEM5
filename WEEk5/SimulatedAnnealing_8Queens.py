# Implementation of Simulated Annealing for 8-Queens Problem

import random
import math

# Define the environment class
class Environment:
    def __init__(self):
        # Randomly place 8 queens, one in each column
        self.board = [random.randint(0, 7) for _ in range(8)]


# Define the Simulated Annealing agent class
class SimulatedAnnealingAgent:
    def __init__(self, environment):
        self.board = environment.board

        # Initial temperature
        T = 1000

        # Continue until temperature becomes zero
        while T > 0:
            # Generate a random neighbour
            nextBoard = self.board.copy()

            col = random.randint(0, 7)
            row = random.randint(0, 7)
            nextBoard[col] = row

            # Calculate change in cost
            deltaE = self.cost(self.board) - self.cost(nextBoard)

            # Accept better state
            if deltaE > 0:
                self.board = nextBoard

            # Accept worse state with probability e^(deltaE/T)
            else:
                p = math.exp(deltaE / T)

                if random.random() < p:
                    self.board = nextBoard

            # Decrease temperature
            T -= 1

            # Stop if solution is found
            if self.cost(self.board) == 0:
                break

        # Display final board
        self.printBoard()

        if self.cost(self.board) == 0:
            print("Solution Found!")
        else:
            print("Solution not found.")

        print("Cost:", self.cost(self.board))

    # Cost function: count attacking pairs of queens
    def cost(self, board):
        conflicts = 0

        for i in range(8):
            for j in range(i + 1, 8):
                if board[i] == board[j] or \
                   abs(board[i] - board[j]) == abs(i - j):
                    conflicts += 1

        return conflicts

    # Display the chessboard
    def printBoard(self):
        for row in range(8):
            for col in range(8):
                if self.board[col] == row:
                    print("Q", end=" ")
                else:
                    print(".", end=" ")
            print()


# Main program
theEnvironment = Environment()
theAgent = SimulatedAnnealingAgent(theEnvironment)
