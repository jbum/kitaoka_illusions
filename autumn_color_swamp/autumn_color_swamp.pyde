# Selected reproductions of full page illustrations from the book "Trick Eyes" (2002) by Akiyoshi Kitaoka and other publications

# "Autumn Color Swamp" motion illusion appears on page 10
# reference image: http://www.psy.ritsumei.ac.jp/~akitaoka/ACswamp.jpg

output_name = "autumn_color_swamp"

checkers = 37
cmargin = 9

ccolors = [color(255,20,20),
           color(255,128,20),
           color(255,205,20),
           color(255,128,20)]
white = color(255)
black = color(0)

def setup():
   size(1024,1024)
   noLoop()

debug = False

def quadstar(dsize):
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
            inverted = y >= cmargin and y < checkers-cmargin and x >= cmargin and x < checkers-cmargin 
            ctr = (x + y*3) % 4 if not inverted else (x + y) % 4
            fill(ccolors[ctr])
            px = x*csize
            py = y*csize
            rect(px,py,csize,csize)
    if debug:
        stroke(255)
        noFill()
        rect(cmargin*csize,cmargin*csize,19*csize,19*csize)
    # draw dividers
    noStroke()
    dsize = csize*.45
    for y in xrange(1,checkers-1):
        for x in xrange(1,checkers-1):
            inverted = y >= cmargin and y <= checkers-cmargin and x >= cmargin and x <= checkers-cmargin 
            ctr = (x + y*3) % 4 if not inverted else (3+(x + y)) % 4
            if ctr == 0 or ctr == 2:
                fill(white if ctr < 2 else black)
                px = x*csize
                py = y*csize
                pushMatrix()
                translate(px,py)
                quadstar(dsize)
                popMatrix()
    
    saveFrame("../output/" + output_name + ".png")