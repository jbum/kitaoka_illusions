# Selected reproductions of full page illustrations from the book "Trick Eyes" (2002) by Akiyoshi Kitaoka

# "The Barber" rotational illusion appears on page 25
# no online reference image found

output_name = "barber"
bg_color = color(109,162,183)

# this effect is actually stronger if you just use red,white,blue instead of the 4 colors in the original
# s_colors = (color(0,0,255),color(255),color(255,0,0))
s_colors = (color(0,0,255),color(255),color(255,0,0),color(255))
rad_factors = (52/76.0, 66.5/76.0)

def setup():
    size(1024,1024)
    noLoop()

stripes = 120
stripe_len = TWO_PI/(stripes/2)

def draw():
    background(bg_color)
    
    pushMatrix()
    translate(width/2,height/2)
    strokeWeight(width*2/760.0)
    ring_width = width*3/760
    for n,rf in enumerate(rad_factors):
        rad = rf*width/2.0
        for i in xrange(stripes):
            a1 = i*TWO_PI/stripes
            a2 = a1 + stripe_len*(-1 if n == 0 else 1)
            r1 = rad-ring_width/2.0
            r2 = rad+ring_width/2.0
            stroke(s_colors[(i + (len(s_colors)-1)*n) % len(s_colors)])
            line(cos(a1)*r1,sin(a1)*r1,cos(a2)*r2,sin(a2)*r2)
    popMatrix()

    saveFrame("../output/" + output_name + ".png")
            

    