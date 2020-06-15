class Orb():
    
    board_start_x = 0
    board_end_x = 0
    board_start_y = 0
    board_end_y = 0
    orb_size = 0
    
    @staticmethod
    def set_vars(width, height):
        global board_start_x, board_end_x, board_start_y, board_end_y, orb_size
        board_start_x = 200
        board_end_x = width - 50
        board_start_y = 50
        board_end_y = height - 50
        orb_size = 20

    def __init__(self):
        self.x = random(board_start_x, board_end_x)
        self.y = random(board_start_y, board_end_y)
        self.size = orb_size
        self.color = [0, random(0, 255), random(0, 255)]
        
    def update(self):
        stroke(15)
        fill(self.color[0], self.color[1], self.color[2])
        circle(self.x, self.y, self.size)
