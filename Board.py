from Block import Block


class Board():
    """Class for a Sudoku board, which contains 9 rows, 9 columns and 9 big blocks"""

    def __init__(self, start_list=None):

        self.row_range = list(range(1, 10))
        self.col_range = list(range(1, 10))
        self.num_range = list(range(1, 10))
        self.bb_x = [1, 4, 7]
        self.bb_y = [1, 4, 7]
        self.blocks = self.add_blocks(start_list)

    def add_blocks(self, start_list):
        """Adding blocks from start list"""

        blocks = []

        # Adding blocks
        for y in self.row_range:
            row = []
            for x in self.col_range:
                new_block = Block((x, y), start_list[y - 1][x - 1])
                row.append(new_block)
            blocks.append(row)

        return blocks

    def print_board(self):
        """Printing 3 seperate boards to screen"""

        pos_str = ''
        val_str = ''
        pos_vals = ''

        for row in self.blocks:
            for block in row:
                pos_str = pos_str + str(block.get_pos())
                if block.get_value() is None:
                    val_str = val_str + '_' + '   '
                    pos_vals = pos_vals + str(block.possible_values) + '    '
                else:
                    val_str = val_str + str(block.get_value()) + '   '
                    pos_vals = pos_vals + str(block.get_value()) + '    '
            pos_str = pos_str + '\n'
            val_str = val_str + '\n'
            pos_vals = pos_vals + '\n'

        print(pos_str)
        print(val_str)
        print(pos_vals)

    def get_row_as_list(self, row_num):
        """Returns a row of values in a list"""

        ls = []
        for block in self.blocks[row_num - 1]:
            if block.value is not None:
                ls.append(block.value)
        return ls

    def get_row_as_pv_list(self, row_num):
        """Returns a list of possible values for entire row in a list"""

        ls = []
        for block in self.blocks[row_num - 1]:
            if block.value is None:
                ls.extend(block.possible_values)
        return ls

    def get_col_as_list(self, col_num):
        """Returns a column of values in a list"""

        ls = []
        for row in self.blocks:
            block = row[col_num - 1]
            if block.value is not None:
                ls.append(block.value)
        return ls

    def get_col_as_pv_list(self, col_num):
        """Returns a list of possible values for entire column in a list"""

        ls = []
        for row in self.blocks:
            block = row[col_num - 1]
            if block.value is None:
                ls.extend(block.possible_values)
        return ls

    def get_big_block_as_list(self, block_x, block_y):
        """Returns a 3x3 block of values in a list"""

        # Setting starting values for big block based on given values
        start_x, start_y = 0, 0
        for x in self.bb_x:
            if block_x >= x:
                start_x = x
        for y in self.bb_y:
            if block_y >= y:
                start_y = y

        # Adding blocks values in big block to list
        ls = []
        for y in range(start_y, start_y + 3):
            for x in range(start_x, start_x + 3):
                block = self.blocks[y - 1][x - 1]
                if not (block.value is None):
                    ls.append(block.value)
        return ls

    def get_big_block_as_pv_list(self, block_x, block_y):
        """Returns a 3x3 block of values in a list"""

        # Setting starting values for big block based on given values
        start_x, start_y = 0, 0
        for x in self.bb_x:
            if block_x >= x:
                start_x = x
        for y in self.bb_y:
            if block_y >= y:
                start_y = y

        # Adding blocks possible values in big block to list
        ls = []
        for y in range(start_y, start_y + 3):
            for x in range(start_x, start_x + 3):
                block = self.blocks[y - 1][x - 1]
                if block.value is None:
                    ls.extend(block.possible_values)
        return ls

    def is_done(self):
        """Checks if board is filled in"""

        for row in self.blocks:
            for block in row:
                if block.value is None:
                    return False
        return True

    def is_valid(self):
        """Checks values of blocks to see if finished board is valid"""

        # Checking rows
        for x in self.row_range:
            row = self.get_row_as_list(x)
            for i in self.num_range:
                if row.count(i) == 1:
                    pass
                else:
                    print('Row False:' + str(row))
                    return False

        # Checking cols
        for x in self.col_range:
            col = self.get_col_as_list(x)
            for i in self.num_range:
                if col.count(i) == 1:
                    pass
                else:
                    print('Col False:' + str(col))
                    return False

        # Checking blocks
        for x in self.bb_x:
            for y in self.bb_y:
                big_block = self.get_big_block_as_list(x, y)
                for i in self.num_range:
                    if big_block.count(i) == 1:
                        pass
                    else:
                        print('Block False: ' + str(big_block))
                        return False

        return True

    def populate_possible_values(self):
        """Loops throughs all blocks and adds possible values where necessary"""

        for row in self.blocks:
            for block in row:
                if block.value is None:
                    # Resetting possible values
                    block.possible_values = []

                    # Getting grid position
                    pos = block.get_pos()
                    x, y = pos[0], pos[1]

                    # Getting row, col and big block for single block
                    row_list = self.get_row_as_list(y)
                    col_list = self.get_col_as_list(x)
                    block_list = self.get_big_block_as_list(x, y)

                    # Checking if i is in row, col or big block
                    for i in self.num_range:
                        # Check row, column and block
                        if not (i in row_list) and not (i in col_list) and not (i in block_list):
                            if not (i in block.possible_values):
                                block.possible_values.append(i)

    def check_all(self):
        """Loops through all empty blocks and checks for possible values that are not possible elsewhere in the row, col, big_block"""

        for row in self.blocks:
            for block in row:
                if block.value is None:
                    # Getting grid position
                    pos = block.get_pos()
                    x, y = pos[0], pos[1]

                    # Getting all possible values in row, col and big block
                    row_list = self.get_row_as_pv_list(y)
                    col_list = self.get_col_as_pv_list(x)
                    block_list = self.get_big_block_as_pv_list(x, y)

                    # Checking for singular possible blocks
                    if len(block.possible_values) == 1:
                        block.value = block.possible_values[0]
                        self.populate_possible_values()
                        continue

                    # Looping through possible values for block
                    for val in block.possible_values:
                        if row_list.count(val) == 1:  # Only possible place for val in row
                            block.value = val
                            self.populate_possible_values()
                            continue
                        if col_list.count(val) == 1:  # Only possible place for val in col
                            block.value = val
                            self.populate_possible_values()
                            continue
                        if block_list.count(val) == 1:  # Only possible place for val in big block
                            block.value = val
                            self.populate_possible_values()
                            continue
