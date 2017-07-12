# Selected reproductions of full page illustrations from the book "Trick Eyes" (2002) by Akiyoshi Kitaoka

# "Primrose's Circulation" rotation illusion appears on page 32
# reference image: http://www.ritsumei.ac.jp/~akitaoka/rotsaku.gif

stripes = 9*4

output_name = "primroses_circulation"
s_colors = [color(62,190,130),color(160,221,15)]
c_colors = [color(255), color(204,4,153) ]
background_color = color(255)
rad_ratio = .5*596/616.0
rad1_ratio = 475/596.0
rad2_ratio = 335/596.0

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
    rad = width * rad_ratio
    rad1 = rad * rad1_ratio
    rad2 = rad * rad2_ratio

    ellipseMode(RADIUS)
    background(background_color)
    noStroke()
    pushMatrix()
    translate(width/2,height/2)
    for i in xrange(stripes):
        blendMode(DARKEST) # helps reduce artifacts in center
        a1 = i*TWO_PI/stripes
        a2 = (i+1)*TWO_PI/stripes
        fill(s_colors[i % 2])
        arc(0,0,rad,rad,a1,a2)
        blendMode(BLEND)
        fill(s_colors[(i+1) % 2])
        arc(0,0,rad1,rad1,a1,a2)
        
        fill(s_colors[i % 2])
        arc(0,0,rad2,rad2,a1,a2)

    drat = 0.5/float(stripes)
    for i in xrange(stripes):
        a1 = i*TWO_PI/stripes
        fill(c_colors[i % 2])
        side1 = TWO_PI*rad1/stripes 
        side2 = TWO_PI*rad2/stripes 
        clover(cos(a1)*rad1,sin(a1)*rad1, side1/3.5)
        fill(c_colors[(i*1) % 2])
        clover(cos(a1)*rad2,sin(a1)*rad2, side2/3.5)
    popMatrix()
    saveFrame("../output/" + output_name + ".png")