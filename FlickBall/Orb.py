class Orb():

    def __init__(self, width, height):
        board_start_x = width - width * .8
        board_end_x = width - 50
        board_start_y = 50
        board_end_y = height - 50
        orb_size = 20
        self.x = random(board_start_x, board_end_x)
        self.y = random(board_start_y, board_end_y)
        self.size = orb_size
        self.color = [0, random(0, 255), random(0, 255)]
        self.visible = True
        
    def update(self, player_x, player_y):
        # eventually checking if the player has touched you or not and disappear logic will go here
        if (self.x - self.size / 2) < (player_x + self.size / 2) and (self.x + self.size / 2) > (player_x - self.size / 2):
            if (self.y + self.size / 2) > (player_y - self.size / 2) and (self.y - self.size / 2) < (player_y + self.size / 2):
                self.visible = False
    
    def show(self):
        if self.visible:
            stroke(10)
            fill(self.color[0], self.color[1], self.color[2])
            circle(self.x, self.y, self.size)
