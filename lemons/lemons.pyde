# Selected reproductions of optical illusions by Akiyoshi Kitaoka

# "Lemons" rotation illusion appears on website
# reference image: http://www.psy.ritsumei.ac.jp/~akitaoka/rotlemons.jpg

output_name = "lemons"

c_colors = [color(0),color(255)]
l_color = color(213,244,20)
s_color = color(104,118,254)
bg_color = color(255)
orig_width = 980
orig_height = 733
nbr_seeds = 12

def setup():
    size(980,733)
    noLoop()

def draw():
    ellipseMode(RADIUS)
    background(bg_color)
    hmargin = 13.0*width/float(orig_width)
    vmargin = 9.0*width/float(orig_width)
    cw = (width-hmargin*2)/4
    s_offset = cw*87/238.0
    r1 = 0.5*cw*42/238.0
    r2 = 0.5*cw*27/238.0

    pushMatrix()
    translate(hmargin,vmargin)
    for y in xrange(3):
        for x in xrange(4):
            pushMatrix()
            translate(x*cw+cw/2.0,y*cw+cw/2.0)
            noStroke()
            fill(l_color)
            ellipse(0,0,cw/2.0,cw/2.0)
            for i in xrange(nbr_seeds):
                pushMatrix()
                rotate(map(i,0,nbr_seeds,0,TWO_PI))
                translate(s_offset,0)
                fill(s_color)
                noStroke()
                ellipse(0,0,r1,r2)
                noFill()
                strokeWeight(4*width/float(orig_width))
                strokeCap(SQUARE)
                ctr = (x+y)%2
                stroke(255*ctr)
                arc(0,0,r1,r2,0,PI)
                stroke(255*(1-ctr))
                arc(0,0,r1,r2,PI,TWO_PI)
                
                popMatrix()
            popMatrix()
    popMatrix()

    saveFrame("../output/" + output_name + ".png")
    
    
    