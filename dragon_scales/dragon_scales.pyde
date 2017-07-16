# Selected reproductions of full page illustrations from the book "Trick Eyes" (2002) by Akiyoshi Kitaoka and other publications

# "Scales of a Dragon" depth/shading illusion appears on page 47
# reference image: http://www.ritsumei.ac.jp/~akitaoka/ryuuroko.gif

output_name = "dragon_scales"
orig_width = 393
bg_color = color(255)
checkers = 8

def setup():
    size(1024,1024)
    noLoop()

def draw():
    background(bg_color)
    margin = width*4/float(orig_width)
    pushMatrix()
    translate(margin,margin)
    cw = int((width-margin*2)/float(checkers))
 
    # scale 1
    pimg1 = createGraphics(cw,cw)
    pimg1.beginDraw()
    pimg1.loadPixels()
    H_PI = PI/2.0
    for y in xrange(cw):
        ry = y/float(cw)
        c1 = color(0)
        c2 = color(255,255,0)
        for x in xrange(cw):
            rx = x/float(cw)
            a = H_PI+rx*H_PI-ry*H_PI
            pimg1.pixels[y*cw+x] = lerpColor(c1,c2,sin(a))
    pimg1.updatePixels()
    pimg1.endDraw()
    
    # scale 2
    pimg2 = createGraphics(cw,cw)
    pimg2.beginDraw()
    pimg2.loadPixels()
    for y in xrange(cw):
        ry = y/float(cw)
        c1 = color(0)
        c2 = color(255)
        for x in xrange(cw):
            rx = x/float(cw)
            a = rx*H_PI+ry*H_PI
            pimg2.pixels[y*cw+x] = lerpColor(c1,c2,sin(a))
    pimg2.updatePixels()
    pimg2.endDraw()
    
    for y in xrange(checkers):
        for x in xrange(checkers):
            px = x*cw
            py = y*cw
            image(pimg1 if (x < checkers/2) == (y < checkers/2) else pimg2, px, py)
          
    strokeWeight(width*1/float(orig_width))
    strokeCap(SQUARE)
    stroke(color(0))
    noFill()
                   
    for i in xrange(checkers+1):
        line(0,i*cw,cw*checkers,i*cw)
        line(i*cw,0,i*cw,cw*checkers)
    
    
    popMatrix()
    saveFrame("../output/" + output_name + ".png")