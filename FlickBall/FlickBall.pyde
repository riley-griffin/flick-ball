# ideas:
# make the camera move with the dude as you go along
# black hole version/animation
# make the sky darken and have space as you get farther up

from player import Player
from orb import Orb

player = None
orbs = None
sling = False
p_mouse = (0,0)
n_mouse = (0,0)
orbs_per_level = 50

def setup():
    size(1500, 500)
    background(50,150,255)
    fill(255, 255, 255)
    noStroke()
    rect(0, 0, width - width * .85, height)

    global orbs, player, orbs_per_level
    player = Player(width, height)
    spawn_new_orbs(orbs_per_level)


def draw():
    # for board
    background(50,150,255)
    fill(255, 255, 255)
    noStroke()
    rect(0, 0, width - width * .85, height)
    global player, orbs, orbs_per_level
    show()
    if player.playing:
        update()
    if player.resetting:
        orbs = []
        player.resetting = False
        spawn_new_orbs(orbs_per_level)
        
def update():
    global player, orbs
    player.update()
    for o in orbs:
        o.update(player.x, player.y)
        
def show():
    global player, orbs
    player.show()
    for o in orbs:
        o.show()
        
def spawn_new_orbs(num_orbs):
    global orbs
    orbs = []
    for num in range(num_orbs):
        orb = Orb(width, height)
        orbs.append(orb)

def mousePressed():
    global p_mouse
    p_mouse = (mouseX, mouseY)

def mouseReleased():
    global player, p_mouse, n_mouse
    n_mouse = (mouseX, mouseY)
    player.vel_x = (p_mouse[0] - n_mouse[0]) / 10
    player.vel_y = (p_mouse[1] - n_mouse[1]) / 10
    player.playing = True
