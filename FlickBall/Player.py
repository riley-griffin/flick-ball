class Player():
    
    def __init__(self, width, height):
        self.x = width - width * .9
        self.y = height / 2
        self.size = 50
        self.playing = False
        self.gravity = .1
        self.vel_y = 0
        self.vel_x = 0
        self.resetting = False
        self.score = 0
        
    def update(self):
        self.x += self.vel_x
        self.vel_y += self.gravity
        self.y += self.vel_y
        if (self.y + self.size / 2) >= height:
            self.reset()
            
    def reset(self):
        self.resetting=True
        self.x = width - width * .9
        self.y = height / 2
        self.playing = False
        self.vel_y = 0
        self.vel_x = 0
        
    def show(self):
        stroke(10)
        fill(255,50,50)
        circle(self.x, self.y, self.size)
