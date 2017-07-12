# Selected reproductions of full page illustrations from the book "Trick Eyes" (2002) by Akiyoshi Kitaoka

# "Red Mist" perceptual transparency appearson page 36
# no online reference imagefound

output_name = "red_mist"

c_colors = [color(255,255,0),color(0,0,255)]
mist_color = color(255,0,0)
bg_color = color(255)
checkers = 8

def setup():
    size(1024,1024) # intentionally a multiple of gw+margin_checkers*2 for sharp pixel boundaries
    noLoop()

def draw():
    
    cw = width/float(checkers)

    background(bg_color)
    pushMatrix()
    
    # draw checkers
    for y in xrange(checkers):
        for x in xrange(checkers):
            fill(c_colors[(x+y) % 2])
            noStroke()
            rect(x*cw,y*cw,cw,cw)

    # draw red mist
    for i in xrange(width):
       ang = (i % (cw*2))/float(cw*2)
       alfa = 1-sin(ang*PI)
       stroke(255,0,0,255*alfa)
       line(i,0,i+width,height)
       line(0,i,height,i+height)
       line(width-i,0,width-i-width,height)
       line(width,i,0,i+height)
                                    
    popMatrix()

    
    saveFrame("../output/" + output_name + ".png")
    
    