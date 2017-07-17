# Selected reproductions of full page illustrations from the book "Trick Eyes" (2002) by Akiyoshi Kitaoka and other publications

# "Tires" rotating illusion appears on page 50
# reference image: http://www.psy.ritsumei.ac.jp/~akitaoka/tire.gif
#

# 
output_name = "tires"

orig_width = 572
r_ratios = (211.0/orig_width,264.0/orig_width)
a1_angles = (-PI/4,-3*PI/4)
a2_angles = (3*PI/4,PI/4)
nbr_treads = 9*4
tread_ratio1 = 2/7.0
tread_ratio2 = 1/4.75
bg_color = color(255)
fg_color = color(0)

def setup():
    size(1024, 1024)
    noLoop()

def draw():
    strokeWeight(width*2.5/float(orig_width))
    strokeCap(SQUARE)
    strokeJoin(ROUND)
    background(bg_color)
    stroke(fg_color)
    
    pushMatrix()
    translate(width/2, height/2)
    
    crad = width*13.5/orig_width
    line(-crad,0,crad,0)
    line(0,-crad,0,crad)
    
    
    
    for ri in xrange(2):   
        rad = r_ratios[ri]*width
        circ = TWO_PI*rad/nbr_treads
        a1 = a1_angles[ri]
        a2 = a2_angles[ri]
        for t in xrange(nbr_treads):
            pushMatrix()
            rotate(t*TWO_PI/nbr_treads)
            pushMatrix()
            translate(rad,0)
            beginShape()
            vertex(0+cos(a1)*circ*tread_ratio2,-circ*tread_ratio1+sin(a1)*circ*tread_ratio2)
            vertex(0,-circ*tread_ratio1)
            vertex(0, circ*tread_ratio1)
            vertex(0+cos(a2)*circ*tread_ratio2, circ*tread_ratio1+sin(a2)*circ*tread_ratio2)
            endShape()
            popMatrix()
            popMatrix()

    popMatrix()
    saveFrame("../output/" + output_name + ".png")
