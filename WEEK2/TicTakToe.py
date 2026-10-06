    # Tic-Tac-Toe using Game Tree

board = [' ' for _ in range(9)]


def display():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()


def winner(player):
    winning = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in winning:
        if board[a] == player and \
           board[b] == player and \
           board[c] == player:
            return True

    return False


def full():
    return ' ' not in board


def minimax(maximizing):

    # Computer wins
    if winner('O'):
        return 1

    # Human wins
    if winner('X'):
        return -1

    # Draw
    if full():
        return 0

    if maximizing:

        best = -1000

        for i in range(9):

            if board[i] == ' ':

                board[i] = 'O'

                score = minimax(False)

                board[i] = ' '

                best = max(best, score)

        return best

    else:

        best = 1000

        for i in range(9):

            if board[i] == ' ':

                board[i] = 'X'

                score = minimax(True)

                board[i] = ' '

                best = min(best, score)

        return best


def computer_move():

    best_score = -1000
    best_position = -1

    for i in range(9):

        if board[i] == ' ':

            board[i] = 'O'

            score = minimax(False)

            board[i] = ' '

            if score > best_score:
                best_score = score
                best_position = i

    board[best_position] = 'O'


# Main Program

print("TIC-TAC-TOE")
print("Human = X")
print("Computer = O")

while True:

    display()

    # Human move
    position = int(input("Enter position (1-9): ")) - 1

    if position < 0 or position > 8 or board[position] != ' ':
        print("Invalid position!")
        continue

    board[position] = 'X'

    if winner('X'):
        display()
        print("Human Wins!")
        break

    if full():
        display()
        print("Draw!")
        break

    # Computer move
    computer_move()

    if winner('O'):
        display()
        print("Computer Wins!")
        break

    if full():
        display()
        print("Draw!")
        break