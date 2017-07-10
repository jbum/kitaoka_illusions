# Selected reproductions of full page illustrations from the book "Trick Eyes" (2002) by Akiyoshi Kitaoka and other publications

# "Waves of Autumn Color" motion illusion, geometrical illusion appears on page 20
# reference image: http://www.psy.ritsumei.ac.jp/~akitaoka/koyowave.jpg

output_name = "autumn_color_wave"

checkers_h = 21
checkers_v = 13
cmargin = 9

ccolors = [color(255,220,144),
           color(255,170,20)]
scolors = [color(253,255,178),
           color(203,13,14)]

pattern = (0,1,1,0,1,0,0,1)

def setup():
   size(1092,676)
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
            ctr = (x+y*7) % 8
            fill(scolors[pattern[ctr]])
            px = x*csize_h
            py = y*csize_v
            pushMatrix()
            translate(px,py)
            quadstar(dsize)
            popMatrix()
    
    saveFrame("../output/" + output_name + ".png")