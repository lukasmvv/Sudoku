class Block():
    """Sudoku single block"""

    def __init__(self, pos, value):

        self.position = pos
        self.value = value
        self.possible_values = []

    def get_value(self):
        """Getting value"""
        return self.value

    def get_pos(self):
        """Getting position"""
        return self.position

    def get_x_pos(self):
        """Getting x position"""
        return self.position[0]

    def get_y_pos(self):
        """Getting y position"""
        return self.position[1]
