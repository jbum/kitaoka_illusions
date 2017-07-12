# Selected reproductions of full page illustrations from the book "Trick Eyes" (2002) by Akiyoshi Kitaoka

# "Eggs pf a Moth" geometrical illusion appears on page 40
# reference image: http://www.ritsumei.ac.jp/~akitaoka/gatamago.gif

output_name = "gatmago"

c_colors = [color(158,128,128),color(212,192,192)]
d_colors = [color(0),color(255)]
bg_color = color(255)
checkers = 11
orig_width = 361

def setup():
    size(800,800) # intentionally a multiple of gw+margin_checkers*2 for sharp pixel boundaries
    noLoop()

def draw():
    ellipseMode(RADIUS)
    margin = width*4.0/orig_width
    
    cw = (width-margin*2)/checkers

    background(bg_color)
    pushMatrix()
    translate(margin,margin)
    
    # draw checkers
    for y in xrange(checkers):
        for x in xrange(checkers):
            c_idx = (x+y) % 2
            fill(c_colors[c_idx])
            noStroke()
            rect(x*cw,y*cw,cw,cw)

    translate(cw*2,cw*2)
    cw2 = cw/2.0
    for y in xrange(checkers*2-7):
        for x in xrange(checkers*2-7):
            if ((x+y)%2) > 0:
                continue
            ix = x%8
            invert = (x < 8) != (y < 8)
            if invert:
                c_idx = 1-((ix/2+7*y/2)%2)
            else:
                c_idx = (ix/2+y/2)%2
            fill(d_colors[c_idx])
            ellipse(x*cw2,y*cw2,cw/4.0,cw/4.0)
            fill(d_colors[1-c_idx])
            ellipse(x*cw2,y*cw2,cw/20.0,cw/20.0)
                                
    pushMatrix()

   
    popMatrix()

    
    saveFrame("../output/" + output_name + ".png")
    
    