# Selected reproductions of full page illustrations from the book "Trick Eyes" (2002) by Akiyoshi Kitaoka and other publications

# "Primrose's Hill" motion illusion, geometrical illusion appears on page 21
# reference image: http://www.ritsumei.ac.jp/~akitaoka/babaroa.gif

# tweaked a bit from 'primroses_field' and 'bavarian_cream'

output_name = "primroses_hill"

checkers_h = 13
checkers_v = 13
cmargin = 9

ccolors = [color(159,215,55),
           color(79,187,129)]
scolors = [color(205,5,152),
           color(255)]

pattern = (0,1,1,0,1,0,0,1)
bulge = (0,2,4,5,5,6,6,6,6,5,5,4,2,0)

def setup():
   size(1024,1024)
   noLoop()

debug = False

def clover(px,py,dwidth):
    for d in xrange(4):
        pushMatrix()
        translate(px,py)
        rotate(d*TWO_PI/4)
        beginShape()
        vertex(0,0)
        vertex(dwidth/2.0,-dwidth*1/3.0)
        vertex(dwidth,0)
        vertex(dwidth/2.0,dwidth*1/3.0)
        endShape(CLOSE)
        popMatrix()

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
                dwidth = csize_h/4.50
                clover(px,py,dwidth)
    
    saveFrame("../output/" + output_name + ".png")