        
class Player():

    player_start_x = 0
    player_start_y = 0
    player_size = 0
    
    @staticmethod
    def set_vars(width, height):
        player_start_x = 50
        player_start_y = height/2
        player_size = 100
    
    def __init__(self):
        self.x = Player.player_start_x
        self.y = Player.player_start_y
        self.size = Player.player_size
        self.playing = True
        
    def update(self):
        fill(255,50,50)
        circle(self.x, self.y, self.size)
