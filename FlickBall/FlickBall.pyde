# ideas:
# black hole version/animation

from player import Player
from orb import Orb

player = None
orbs = None

def setup():
    size(1500, 500)
    background(50,150,255)
    fill(255, 255, 255)
    noStroke()
    rect(0, 0, 150, height)

    global orbs, player
    orbs = []
    Orb.set_vars(width, height)
    Player.set_vars(width, height)
    player = Player()
    print("setup")
    for num in range(40):
        orb = Orb()
        orbs.append(orb)

    
def draw():
    global player, orbs
    player.update()
    print(player.size)
        
    for o in orbs:
        o.update()
    #player.playing = True
