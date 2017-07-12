# Selected reproductions of full page illustrations from the book "Trick Eyes" (2002) by Akiyoshi Kitaoka

# "Omikuji" op effect, motion illusion appears on page 34
# reference image: http://www.ritsumei.ac.jp/~akitaoka/shijo.gif

output_name = "omikuji"

c_colors = [color(254,19,18),color(0),color(254,154,20),color(255)]
bg_color = color(255)
checkers = 11
orig_width = 339

def setup():
    size(1024,1024) # intentionally a multiple of gw+margin_checkers*2 for sharp pixel boundaries
    noLoop()

def draw():
    margin = width*5.0/orig_width
    
    cw = (width-margin*2)/checkers

    background(bg_color)
    pushMatrix()
    translate(margin,margin)
    
    # draw checkers
    for y in xrange(checkers):
        for x in xrange(checkers):
            c_idx = ((x+y)%2)*2
            fill(c_colors[c_idx])
            noStroke()
            rect(x*cw,y*cw,cw,cw)

    translate(cw,cw)
    for y in xrange(checkers-1):
        for x in xrange(checkers-1):
            d = dist(4.5,4.5,x,y)
            if d < 5:
                c_idx = (x+y)%2 # !!
                if (x < 5) != (y < 5):
                    c_idx = 1-c_idx 
                c_idx *= 2
                fill(c_colors[c_idx])
                rect(x*cw-cw*11/30.0,y*cw-cw*11/30.0,cw*22/30.0,cw*22/30.0)
                fill(c_colors[c_idx+1])
                rect(x*cw-cw*9/30.0,y*cw-cw*9/30.0,cw*18/30.0,cw*18/30.0)
                                    
    pushMatrix()

   
    popMatrix()

    
    saveFrame("../output/" + output_name + ".png")
    
    