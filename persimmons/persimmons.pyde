# persimmons
# Selected reproductions of full page illustrations from the book "Trick Eyes" (2002) by Akiyoshi Kitaoka and other publications

# "Persimmons" motion/geometrical illusion appears on page 48
# reference image: http://www.ritsumei.ac.jp/~akitaoka/kaki.gif

output_name = "persimmons"
orig_width = 305

bg_color = color(255)
checkers = 9

def setup():
    size(1024,1024)
    noLoop()

def quadstar(dsize):
    beginShape()
    vertex(0,-dsize)
    quadraticVertex(0,0,dsize,0)
    quadraticVertex(0,0,0,dsize)
    quadraticVertex(0,0,-dsize,0)
    quadraticVertex(0,0,0,-dsize)
    endShape()


def draw():
    background(bg_color)
    margin = width*9/float(orig_width)
    pushMatrix()
    translate(margin,margin)
    cw = int((width-margin*2)/float(checkers))
 
    # scale 1
    pimg1 = createGraphics(cw,cw)
    pimg1.beginDraw()
    pimg1.loadPixels()
    H_PI = PI/2.0
    for y in xrange(cw):
        for x in xrange(cw):
            pimg1.pixels[y*cw+x] = color(53,153,52)
    pimg1.updatePixels()
    pimg1.endDraw()
    
    # scale 2
    pimg2 = createGraphics(cw,cw)
    pimg2.beginDraw()
    pimg2.loadPixels()
    for y in xrange(cw):
        ry = y/float(cw)
        c1 = color(200,127,16)
        c2 = color(255,160,32)
        for x in xrange(cw):
            rx = x/float(cw)
            pimg2.pixels[y*cw+x] = lerpColor(c1,c2,2*max(abs(0.5-ry),abs(0.5-rx)))
    pimg2.updatePixels()
    pimg2.endDraw()
    
    for y in xrange(checkers):
        for x in xrange(checkers):
            px = x*cw
            py = y*cw
            image(pimg1 if (x+y) % 2 == 0 else pimg2, px, py)
          
    noStroke()
    for y in xrange(0,checkers+1):
        for x in xrange(0,checkers+1):
            px = x*cw
            py = y*cw
            pushMatrix()
            if x == 0 or y == 0 or x == checkers or y == checkers:
                fill(255)
            else:
                cx = x + (x > 4) + (y > 4)
                fill(255 if (cx+y) % 2 == 0 else 0)
            translate(px,py)
            quadstar(cw/3.0)
            popMatrix()
                   
                                                        
    
    
    popMatrix()
    saveFrame("../output/" + output_name + ".png")