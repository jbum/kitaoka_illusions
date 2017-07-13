# Selected reproductions of optical illusions by Akiyoshi Kitaoka

# "rotating_rays" rotation illusion appears on website
# reference image: http://www.ritsumei.ac.jp/~akitaoka/rotrays.gif

output_name = "rotating_rays"

g_colors = [color(30,200,255),color(19,239,216)]
r_color = color(200,12,12)
bg_color = color(255)
orig_width = 689.0
orig_crad = 280
nbr_seeds = 12
rings = 3
bands = 2
nbr_rays = 6*4

def setup():
    size(1024,1024)
    noLoop()

def draw():
    ellipseMode(RADIUS)
    background(bg_color)
    rad = 0.5*width*652/orig_width
    subrad_ratios = [280/orig_width,127/orig_width]
    s_ang = TWO_PI/nbr_rays

    pushMatrix()
    translate(width/2,height/2)
    
    # radial gradient background
    noFill()
    strokeWeight(2)
    for i in xrange(1,int(rad)+1):
        stroke(lerpColor(g_colors[0],g_colors[1],map(i,1,rad,0,1)))
        ellipse(0,0,i,i)
    
    for b in xrange(bands):
        crad = width*subrad_ratios[b]
        for r in xrange(rings):
            radw = TWO_PI*crad/nbr_rays
            for i in xrange(nbr_rays):
                pushMatrix()
                rotate(s_ang*(i + 0.5*(r%2)))
                translate(crad,0)
                dr = radw*.9*0.5
                fill(r_color)
                noStroke()
                quad(-dr,0,0,-dr,dr,0,0,dr)
                strokeWeight(width*3.5/orig_width) # note: strokeWeight does not diminish with ray size..
                stroke(255*b)
                # upper
                line(-dr,0,0,-dr)
                line(0,-dr,dr,0)
                stroke(255*(1-b))
                line(dr,0,0,dr)
                line(0,dr,-dr,0)
                fill(0)
                noStroke()
                eye_ofsty = dr*0.4*(-1 if b else 1)
                eye_dist = crad*5/orig_crad
                eye_vr = crad*5/orig_crad
                eye_hr = eye_vr/2.0
                ellipse(-eye_dist,eye_ofsty,eye_hr,eye_vr)
                ellipse(+eye_dist,eye_ofsty,eye_hr,eye_vr)
                # lower
                popMatrix()
            crad = crad-radw*0.75

    popMatrix()

    saveFrame("../output/" + output_name + ".png")
    
    
    