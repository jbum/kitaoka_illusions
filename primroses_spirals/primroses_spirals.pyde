# Selected reproductions of full page illustrations from the book "Trick Eyes" (2002) by Akiyoshi Kitaoka

# "Primrose's Spirals" spiral illusion, rotating illusion appears on page 31
# reference image:  http://www.psy.ritsumei.ac.jp/~akitaoka/uzusaku.gif

stripes = 9*4

output_name = "primroses_spirals"
s_colors = [color(62,190,130),color(160,221,15)]
c_colors = [color(255), color(204,4,153) ]

bg_color = color(255)
radius_ratio = 0.466
quadstar_ratio = 0.4
quadstar_dot_ratio = 0.15
quadstar_ang_ratio = 0.9

ring_side_ratio = 0.86

def setup():
    size(1024,1024)
    noLoop()

def clover(px,py,dwidth):
    for d in xrange(4):
        pushMatrix()
        translate(px,py)
        rotate(d*TWO_PI/4)
        beginShape()
        vertex(0,0)
        vertex(dwidth/2.0,-dwidth*1/3.5)
        vertex(dwidth,0)
        vertex(dwidth/2.0,dwidth*1/3.5)
        endShape(CLOSE)
        popMatrix()

def draw():
    background(bg_color)
    noStroke()
    
    pushMatrix()
    translate(width/2,height/2)
    
    rad = width*radius_ratio
    
    n = 0
    s_ang = TWO_PI/stripes
    while rad > 1:
        circ = TWO_PI*rad
        side = circ/float(stripes)
        rad2 = rad-side * ring_side_ratio

        for i in xrange(stripes):
           pushMatrix()
           rotate(-i*s_ang)
           fill(s_colors[(i+n)%2])
           stroke(s_colors[(i+n)%2])
           quad(cos(0)*rad2, sin(0)*rad2,
                cos(-s_ang)*rad2,sin(-s_ang)*rad2,
                cos(-s_ang)*rad,sin(-s_ang)*rad,
                cos(0)*rad, sin(0)*rad)
           popMatrix()
        noStroke()
        for i in xrange(stripes):
           pushMatrix()
           rotate(-i*s_ang)
           fill(c_colors[(i+n)%2])
           px,py = (cos(0)*rad,sin(0)*rad)
           clover(px,py,side/3.5)
           popMatrix()

        rad = rad2
        n += 1
    
    popMatrix()
    saveFrame("../output/" + output_name + ".png")