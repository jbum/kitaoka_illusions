# Selected reproductions of full page illustrations from the book "Trick Eyes" (2002) by Akiyoshi Kitaoka

# "Kids of Seals" spiral color illusion appears on page 28
# no online reference image found


output_name = "kids_of_seals"
s_colors = [color(0,0,192),color(255,255,0),color(192,0,0),color(255)]
d_colors = [color(255),color(0),color(255),color(0)]
bg_color = color(255)

nbr_seals = 80

rad_ratio = 12.5/14.2

def setup():
    size(1024,1024)
    ellipseMode(RADIUS)
    # noLoop()

def draw():
    rad = width*.45
    n = 0

    rad_ratio = .9  # map(mouseX,0,width,.8,.99)
    # rad_ratio = map(mouseX,0,width,.8,.99)
    # print rad_ratio
    
    escale = 0.25 # map(mouseX,0,width,1/12.0,1/2.0)
    dscale = 1/12.0
    # print escale
   
    background(bg_color)
    
    pushMatrix()
    translate(width/2,height/2)
    noStroke()
    
    s_ang = TWO_PI/nbr_seals
    
    while rad > 1:
        rad2 = rad*rad_ratio
        
        for i in xrange(nbr_seals):
           pushMatrix()
           rotate(-i*s_ang)
           fill(s_colors[(i+n)%4])
           quad(cos(0)*rad2, sin(0)*rad2,
                cos(-s_ang)*rad2,sin(-s_ang)*rad2,
                cos(-s_ang)*rad,sin(-s_ang)*rad,
                cos(0)*rad, sin(0)*rad)
           popMatrix()
        
        for i in xrange(nbr_seals):
           pushMatrix()
           rotate(-i*s_ang)
           fill(s_colors[(i+n)%4])
           ellipse(cos(0)*rad, sin(0)*rad,(rad/rad_ratio-rad2)/4,(TWO_PI*rad/nbr_seals)*escale)
           fill(d_colors[(i+n)%4])
           ellipse(cos(0)*rad, sin(0)*rad,(rad-rad2)*dscale,(rad-rad2)*dscale)
           popMatrix()
        rad = rad2
        n += 1
    popMatrix()
    saveFrame("../output/" + output_name + ".png")
 