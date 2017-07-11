# Selected reproductions of full page illustrations from the book "Trick Eyes" (2002) by Akiyoshi Kitaoka

# "Neural Network" spral illusion, spiral illusion, appears on page 29
# reference image: http://www.psy.ritsumei.ac.jp/~akitaoka/neuralcircuitspirals.jpg

stripes = 40

output_name = "neural_network"
s_colors = [color(163,165,12), color(208,210,18)]
d_colors = [color(152,5,5), color(255), color(59,44,254), color(255)]
dit_color = color(178)

bg_color = color(255)
radius_ratio = 0.471
quadstar_ratio = 0.4
quadstar_dot_ratio = 0.15
quadstar_ang_ratio = 0.9

ring_side_ratio = 0.95

def setup():
    size(1024,1024)
    noLoop()

def quadstarr(dsize,rad):
    ang = (PI/stripes)*quadstar_ang_ratio
    x,y = (cos(0)*rad,sin(0)*rad)
    pushMatrix()
    beginShape()
    vertex(cos(-ang)*rad,sin(-ang)*rad)
    quadraticVertex(x,y,x+dsize,y)
    quadraticVertex(x,y,cos(ang)*rad,sin(ang)*rad) # sin(ang)*rad
    quadraticVertex(x,y,x-dsize,y)
    quadraticVertex(x,y,cos(-ang)*rad,sin(-ang)*rad)
    endShape()
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
           fill(d_colors[(i+n*3)%4])
           px,py = (cos(0)*rad,sin(0)*rad)
           quadstarr(side*quadstar_ratio,rad)
           fill(dit_color)
           ellipse(px,py,side * quadstar_dot_ratio,side * quadstar_dot_ratio)
           popMatrix()

        rad = rad2
        n += 1
    
    popMatrix()
    saveFrame("../output/" + output_name + ".png")