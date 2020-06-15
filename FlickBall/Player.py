        
class Player():

    player_start_x = 0
    player_start_y = 0
    player_size = 0
    
    @staticmethod
    def set_vars(width, height):
        global player_start_x, player_start_y, player_size
        player_start_x = 50
        player_start_y = height/2
        player_size = 50
    
    def __init__(self):
        self.x = player_start_x
        self.y = player_start_y
        self.size = player_size
        self.playing = True
        
    def update(self):
        fill(255,50,50)
        circle(self.x, self.y, self.size)
