class Orb():
    
    board_start_x = 0
    board_end_x = 0
    board_start_y = 0
    board_end_y = 0
    orb_size = 0
    
    @staticmethod
    def set_vars(width, height):
        board_start_x = 200
        board_end_x = width - 50
        board_start_y = 50
        board_end_y = height - 50
        orb_size = 20

    def __init__(self):
        self.x = random(Orb.board_start_x, Orb.board_end_x)
        self.y = random(Orb.board_start_y, Orb.board_end_y)
        self.size = Orb.orb_size
        
    def update(self):
        fill(random(100, 255), random(100, 255), random(100, 255))
        circle(self.x, self.y, self.size)
