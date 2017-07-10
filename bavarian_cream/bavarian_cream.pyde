# Selected reproductions of full page illustrations from the book "Trick Eyes" (2002) by Akiyoshi Kitaoka and other publications

# "Bavarian Cream" motion illusion, geometrical illusion appears on page 21
# reference image: http://www.ritsumei.ac.jp/~akitaoka/babaroa.gif
# and http://www.psy.ritsumei.ac.jp/~akitaoka/babaroa.jpg (remake)

# tweaked a bit from 'autumn_color_waves'

output_name = "bavarian_cream"

checkers_h = 13
checkers_v = 13
cmargin = 9

ccolors = [color(255,220,144),
           color(255,170,20)]
scolors = [color(203,13,14),
           color(253,255,178)]

pattern = (0,1,1,0,1,0,0,1)
bulge = (0,1,4,5,5,5,6,6,5,5,5,4,1,0)

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
    csize_h = width/float(checkers_h)
    csize_v = height/float(checkers_v)

    noStroke()
    for y in xrange(checkers_v):
        for x in xrange(checkers_h):
            ctr = (x+y) % 2
            fill(ccolors[ctr])
            px = x*csize_h
            py = y*csize_v
            rect(px,py,csize_h,csize_v)

    dsize = csize_h*.25
    noStroke()
    for y in xrange(1,checkers_v):
        for x in xrange(1,checkers_h):
            dx = abs(x-6.5)
            dy = abs(y-6.5)
            if dx <= bulge[y] and dy <= bulge[x]:
                polarity =  (x < 6.5) != (y < 6.5) 
                ctr = (x+y+polarity) % 2
                fill(scolors[pattern[ctr]])
                px = x*csize_h
                py = y*csize_v
                pushMatrix()
                translate(px,py)
                quadstar(dsize)
                popMatrix()
                
    # draw dividers
    # noStroke()
    # dsize = csize*.45
    # for y in xrange(1,checkers-1):
    #     for x in xrange(1,checkers-1):
    #         inverted = y >= cmargin and y <= checkers-cmargin and x >= cmargin and x <= checkers-cmargin 
    #         ctr = (x + y*3) % 4 if not inverted else (3+(x + y)) % 4
    #         if ctr == 0 or ctr == 2:
    #             fill(white if ctr < 2 else black)
    #             px = x*csize
    #             py = y*csize
    #             pushMatrix()
    #             translate(px,py)
    #             quadstar(dsize)
    #             popMatrix()
    
    saveFrame("../output/" + output_name + ".png")