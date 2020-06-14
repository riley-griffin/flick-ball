# ideas:
# black hole version/animation

from player import Player
from orb import Orb

player = None
orbs = None

def setup():
    size(1500, 500)
    fill(255, 255, 255)
    noStroke()
    rect(0, 0, 200, height)
    
    stroke(15)
    fill(0, 100, 200)
    rect(200, 0, width-200, height)

    global orbs
    global player
    orbs = []
    Orb.set_vars(width, height)
    Player.set_vars(width, height)
    player = Player()

    
def draw():
    global player
    global orbs
    while player.playing:
        player.update()
        
        for num in range(40):
            orb = Orb()
            orbs.append(orb)
            
        for o in orbs:
            o.update()
        #player.playing = True
