# Selected reproductions of full page illustrations from the book "Trick Eyes" (2002) by Akiyoshi Kitaoka

# "Neural Circuits" rotation illusion, geometrical illusion appears on page 24
# reference image: http://www.psy.ritsumei.ac.jp/~akitaoka/neuralc2.gif
# 'plastic version': http://www.psy.ritsumei.ac.jp/~akitaoka/rotneuralcplastic.jpg

stripes = 36*2

output_name = "neural_circuits"
s_colors = [color(218,221,19), color(142,153,9), ]
d_colors = [color(255), color(152,7,5), color(255), color(59,42,254)]
background_color = color(255)

def setup():
    size(1024,1024)
    noLoop()

def quadstar(dsize,x,y,a):
    pushMatrix()
    translate(x,y)
    rotate(a)
    beginShape()
    vertex(0,-dsize)
    quadraticVertex(0,0,dsize,0)
    quadraticVertex(0,0,0,dsize)
    quadraticVertex(0,0,-dsize,0)
    quadraticVertex(0,0,0,-dsize)
    endShape()
    popMatrix()


def draw():
    rad = width*.48
    rad1 = rad*.642
    rad2 = rad*.800
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
        triangle(0,0,
                 cos(a1)*rad,sin(a1)*rad,
                 cos(a2)*rad,sin(a2)*rad)
        # fill(color(255) if i%2 > 0 else color(0))
        blendMode(BLEND)
        fill(s_colors[(i+1) % 2])
        quad(cos(a1)*rad1,sin(a1)*rad1,
             cos(a2)*rad1,sin(a2)*rad1,
             cos(a2)*rad2,sin(a2)*rad2,
             cos(a1)*rad2,sin(a1)*rad2)
    drat = 0.5/float(stripes)
    for i in xrange(stripes):
        a1 = i*TWO_PI/stripes
        fill(d_colors[i % 4])
        quadstar(TWO_PI*rad1*drat,cos(a1)*rad1,sin(a1)*rad1,a1)
        fill(d_colors[(i*3) % 4])
        quadstar(TWO_PI*rad2*drat,cos(a1)*rad2,sin(a1)*rad2,a1)
    popMatrix()
    saveFrame("../output/" + output_name + ".png")