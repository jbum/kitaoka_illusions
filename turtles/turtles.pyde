# Selected reproductions of full page illustrations from the book "Trick Eyes" (2002) by Akiyoshi Kitaoka and other publications

# "Turtles" geometrical illusion appears on page 52
# reference image: http://www.psy.ritsumei.ac.jp/~akitaoka/kame.jpg

output_name = "turtles"

checkers = 11
orig_width = 366
bg_color = color(255)
fg_color = color(0)

def setup():
   size(1024,1024)
   noLoop()

def draw_turtle(f1,f2,f3,f4):
    global cw,crad
    beginShape()

    # top-left    
    vertex(0,crad*2)
    vertex(-crad if f1 else crad,crad)
    vertex(0,0)
    vertex(crad,crad if f1 else -crad)
    vertex(crad*2,0)
    
    # top-right
    vertex(cw-crad*2,0)
    vertex(cw-crad,-crad if f2 else crad)
    vertex(cw,0)
    vertex(cw-crad if f2 else cw+crad,crad)
    vertex(cw,crad*2)
    
    # bot-right
    vertex(cw, cw-crad*2)
    vertex(cw+crad if f3 else cw-crad,cw-crad)
    vertex(cw,cw)
    vertex(cw-crad,cw-crad if f3 else cw+crad)
    vertex(cw-crad*2,cw)
    
    # bot-left
    vertex(crad*2,cw)
    vertex(crad,cw+crad if f4 else cw-crad)
    vertex(0,cw)
    vertex(crad if f4 else -crad,cw-crad)
    vertex(0,cw-crad*2)

    endShape(CLOSE)

def draw():
    global cw,crad
    margin = width*7.0/orig_width
    background(bg_color)
    fill(fg_color)
    noStroke()
    
    pushMatrix()
    translate(margin,margin)
    
    cw = (width-margin*2)/checkers
    crad = width*4.0/orig_width

    
    for y in xrange(checkers):
        for x in xrange(checkers):
            if (x+y)%2 > 0:
                continue
            pushMatrix()
            translate(x*cw,y*cw)
            draw_turtle((x<6)==(y<6),
                        (x<5)==(y<6),
                        (x<5)==(y<5),
                        (x<6)==(y<5))
            popMatrix()
    
    popMatrix()
    saveFrame("../output/" + output_name + ".png")