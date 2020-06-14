        
class Player():

    def set_vars(width, height):
        player_start_x = 50
        player_start_y = height/2
        player_size = 100
    
    def __init__(self):
        self.x = player_start_x
        self.y = player_start_y
        self.size = player_size
        self.resetting = false
