def setup():
    # Set up the size of the display window.
    size(640, 480)

def draw():
    # Any commands you need to run once a frame, for example drawing a circle.
    if mousePressed:
        fill(0)
    else:
        fill(255)
    ellipse(mouseX, mouseY, 60, 60)
