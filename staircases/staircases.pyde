# Selected reproductions of full page illustrations from the book "Trick Eyes" (2002) by Akiyoshi Kitaoka and other publications

# "Staircases" motion/stereopsis/lightness illusion, appears on page 49
# no reference image used
#
# same as background of joro-gumo


output_name = "staircases"

subsquares = 48

scolors = [color(0),color(255)]

def setup():
    size(1024,1024)
    noLoop()

def draw():
    tw = width/float(subsquares)
    background(0)
    strokeWeight(1)
    for y in range(subsquares):
        for x in range(subsquares):
            if x < 12 or y < 12 or x >= subsquares-12 or y >= subsquares-12:
                ctr = ((1+x+y*5) % 6)/3
            else:  
                ctr = ((2+x+y) % 6)/3
            fill(scolors[ctr])
            stroke(scolors[ctr])
            rect(x*tw,y*tw,tw,tw)

    saveFrame("../output/" + output_name + ".png")
    