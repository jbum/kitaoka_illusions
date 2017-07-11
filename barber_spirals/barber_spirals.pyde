# Selected reproductions of full page illustrations from the book "Trick Eyes" (2002) by Akiyoshi Kitaoka

# "Barber Spirals" spiral illusion appears on page 30
# no online reference image found

stripes = 40

output_name = "barber_spirals"
s_colors = [color(20,120,200), color(255),color(200,70,100),color(255)]
bg_color = color(255)

radius_ratio = 0.471
ring_side_ratio = 1.1

stripes = 36*2

def setup():
    size(1024,1024)
    noLoop()

def draw():
    ellipseMode(RADIUS)
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
        rad2 = rad-side*ring_side_ratio
        noStroke()
        for i in xrange(stripes):
           pushMatrix()
           rotate(n*s_ang/2-i*s_ang)
           ctr = i%4
           fill(s_colors[ctr])
           stroke(s_colors[ctr])
           quad(cos(0)*rad2, sin(0)*rad2,
                cos(-s_ang)*rad2,sin(-s_ang)*rad2,
                cos(-s_ang)*rad,sin(-s_ang)*rad,
                cos(0)*rad, sin(0)*rad)
           popMatrix()
        noFill()
        strokeWeight(.07*TWO_PI*rad/stripes)
        stroke(192)
        ellipse(0,0,rad,rad)
        rad = rad2
        n += 1
    popMatrix()
    saveFrame("../output/" + output_name + ".png")