from Board import Board

board = Board([[None, None, None, None, None, None, None, None, 7],
               [None, 9, None, 8, None, None, None, None, 2],
               [1, None, None, 2, 3, None, 6, None, None],
               [None, 3, None, None, None, 4, 9, None, None],
               [8, 2, None, None, None, None, None, 4, 6],
               [None, None, 4, 6, None, None, None, 5, None],
               [None, None, 3, None, 7, 2, None, None, 9],
               [2, None, None, None, None, 5, None, 3, None],
               [4, None, None, None, None, None, None, None, None]])

count = 0
while not board.is_done():
    board.print_board()
    board.populate_possible_values()
    board.check_all()
    count = count + 1
board.print_board()
print(str(count))
print(board.is_valid())
