# Selected reproductions of full page illustrations from the book "Trick Eyes" (2002) by Akiyoshi Kitaoka

# "Packed Cherries" motion illusion appears on cover page
# reference image: http://www.ritsumei.ac.jp/~akitaoka/sakuran2.gif

output_name = "packed_cherries"

dark_maroon = color(199,12,11)
light_maroon = color(254,19,18)
white = color(255,255,255)
gw,gh = (15,15)
gw2,gh2 = (6,6)
drad_ratio = .4375
strokeweight_ratio = .125
imargin_ratio = .015

def setup():
    size(1024,1024)
    noLoop()


def draw():
    margin = 0
    background(white)
    fill(dark_maroon)
    noStroke()
    pushMatrix()
    translate(margin,margin)
    rwidth, rheight = (width-margin*2,height-margin*2)
    rect(0,0,rwidth, rheight)
    imargin = rwidth*imargin_ratio
    pushMatrix()
    translate(imargin,imargin)
    fill(0)
    irwidth, irheight = (rwidth-imargin*2,rheight-imargin*2)
    # rect(0,0,irwidth, irheight)
    ellipseMode(RADIUS)
    tw,th = (irwidth/float(gw),irheight/float(gh))
    drad = tw*drad_ratio
    strokeWeight(tw*strokeweight_ratio)
    strokeCap(PROJECT)
    stroke(white)
    noFill()
    
    # outer lines
    for y in xrange(gh):
        for x in xrange(gw):
            if x > 3 and x < 11 and y > 3 and y < 11:
                continue
            line(x*tw,y*th,(x+1)*tw,(y+1)*th)
        
        
    # back lines
    for y in xrange(4,4+6):
        for x in xrange(4,4+6):
            line(irwidth-(x+.5)*tw,(y+.5)*th,irwidth-(x+1.5)*tw,(y+1.5)*th)
    
    noStroke()
    for y in xrange(gh):
        for x in xrange(gw):
            if x > 3 and x < 11 and y > 3 and y < 11:
                continue
            fill(light_maroon)
            px = x*tw+tw/2
            py = y*th+th/2
            ellipse(px,py,drad,drad)

    for y in xrange(gh2):
        for x in xrange(gw2):
            fill(light_maroon)
            px = 4.5*tw + x*tw+tw/2
            py = 4.5*th + y*th+th/2
            ellipse(px,py,drad,drad)
            
    popMatrix()
    pushMatrix()
    saveFrame("../output/" + output_name + ".png")
    
    