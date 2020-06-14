class Orb():
    
    board_start_x = 200
    board_end_x = width - 50
    board_start_y = 50
    board_end_y = height - 50
    orb_size = 20
    
    def __init__(self):
        self.x = random(board_start_x, board_end_x)
        self.y = random(board_start_y, board_end_y)
        self.size = orb_size
