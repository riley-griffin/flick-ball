class Orb():
        
    def __init__(self, width, height, player):
        orb_size = 20
        self.respawn(player)
        self.size = orb_size
        self.color = [0, random(0, 255), random(0, 255)]
        self.visible = True
        
    def update(self, player):
        # eventually checking if the player has touched you or not and disappear logic will go here
        if (self.x - self.size / 2) < (player.x + player.size / 2) and (self.x + self.size / 2) > (player.x - player.size / 2):
            if (self.y + self.size / 2) > (player.y - player.size / 2) and (self.y - self.size / 2) < (player.y + player.size / 2):
                self.visible = False
                player.score += 1
        if (self.x - self.size / 2) < (player.x - player.size / 2 - 100):
            self.respawn(player)
            
    def respawn(self, player):
        lower_x = player.x
        upper_x = player.x + 1500
        lower_y = player.y - 250
        upper_y = player.y + 250
        self.x = random(lower_x, upper_x)
        self.y = random(lower_y, upper_y)
    
    def show(self):
        if self.visible:
            stroke(10)
            fill(self.color[0], self.color[1], self.color[2])
            circle(self.x, self.y, self.size)
