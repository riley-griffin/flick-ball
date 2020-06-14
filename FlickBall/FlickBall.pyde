# ideas:
# black hole version/animation

import Player
import Orb

def setup():
    size(1500, 500)
    fill(255, 255, 255)
    noStroke()
    rect(0, 0, 200, height)
    
    stroke(15)
    fill(0, 100, 200)
    rect(200, 0, width-200, height)

    orbs = []
    player = Player()

    
def draw():
    while(not player.resetting):
        fill(255, 0, 0)
        circle(100, 100, 100)
        
        for i in range(40):
            fill(random(100, 255), random(100, 255), random(100, 255))
            orb = Orb()
            orbs.append(orb)
        player.resetting = true
