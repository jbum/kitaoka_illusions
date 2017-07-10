# Selected reproductions of full page illustrations from the book "Trick Eyes" (2002) by Akiyoshi Kitaoka and other publications

# "Nuts" motion illusion / geometrical illusion appears on page 11
# reference image found under the name "cherries": http://www.ritsumei.ac.jp/~akitaoka/sakuranb.gif

output_name = "nuts"

checkers = 25
cmargin = 5

check_colors = [color(202,204,17),
                color(203,154,15)]
dot_colors = [color(253,255,24),
              color(204,255,204),
              color(179,9,9),
              color(253,205,21)]

white = color(255)
black = color(0)

def setup():
   size(1024,1024)
   ellipseMode(RADIUS)
   noLoop()

debug = False

def idiamond(dsize):
    beginShape()
    vertex(0,-dsize)
    quadraticVertex(0,0,dsize,0)
    quadraticVertex(0,0,0,dsize)
    quadraticVertex(0,0,-dsize,0)
    quadraticVertex(0,0,0,-dsize)
    endShape()

def draw():
    csize = width/float(checkers)

    noStroke()
    for y in xrange(checkers):
        for x in xrange(checkers):
            ctr = (x + y) % 2
            fill(check_colors[ctr])
            px = x*csize
            py = y*csize
            rect(px,py,csize,csize)
    if debug:
        stroke(255)
        noFill()
        rect(cmargin*csize,cmargin*csize,19*csize,19*csize)
    # draw dividers
    noStroke()
    dsize = csize*.13
    hsize = dsize*.3
    for y in xrange(1,checkers):
        for x in xrange(1,checkers):
            inverted = y > cmargin and y < checkers-cmargin and x > cmargin and x < checkers-cmargin 
            centered = y > cmargin+1 and y < checkers-(cmargin+1) and x > cmargin+1 and x < checkers-(cmargin+1)
            if not inverted or centered:
                ctr = (x + y + (1 if centered else 0)) % 2
                fill(dot_colors[ctr*2])
                px = x*csize
                py = y*csize
                pushMatrix()
                translate(px,py)
                ellipse(0,0,dsize,dsize)
                fill(dot_colors[ctr*2+1])
                ellipse(0,0,hsize,hsize)
                popMatrix()
    
    saveFrame("../output/" + output_name + ".png")