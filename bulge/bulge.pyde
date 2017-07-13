# Selected reproductions of optical illusions by Akiyoshi Kitaoka

# "Bulge02c" geometrical illusion appears on website
# reference image: http://www.ritsumei.ac.jp/~akitaoka/Bulge02c.jpg

output_name = "bulge02c"

c_colors = [color(0),color(255)]
bg_color = color(255)
checkers = 15
orig_width = 574

flags = [
  0, 0, 0, 0, 0, 0, 0,  0,  0, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 9, 10,  6, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 9, 9, 9, 10,  6, 6, 6, 0, 0, 0, 0,
  0, 0, 0, 9, 9, 9, 9, 10,  6, 6, 6, 6, 0, 0, 0,
  0, 0, 9, 9, 9, 9, 9, 10,  6, 6, 6, 6, 6, 0, 0,
  0, 0, 9, 9, 9, 9, 9, 10,  6, 6, 6, 6, 6, 0, 0,
  0, 9, 9, 9, 9, 9, 9, 10,  6, 6, 6, 6, 6, 6, 0,
  0, 3, 3, 3, 3, 3, 3,  0, 12,12,12,12,12,12, 0,
  0, 6, 6, 6, 6, 6, 6,  5,  9, 9, 9, 9, 9, 9, 0,
  0, 0, 6, 6, 6, 6, 6,  5,  9, 9, 9, 9, 9, 0, 0,
  0, 0, 6, 6, 6, 6, 6,  5,  9, 9, 9, 9, 9, 0, 0,
  0, 0, 0, 6, 6, 6, 6,  5,  9, 9, 9, 9, 0, 0, 0,
  0, 0, 0, 0, 6, 6, 6,  5,  9, 9, 9, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 6,  5,  9, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 0,  0,  0, 0, 0, 0, 0, 0, 0]

xd = [1,1,-1,-1]
yd = [-1,1,-1,1]

def setup():
    size(574,574) # intentionally a multiple of gw+margin_checkers*2 for sharp pixel boundaries
    noLoop()

def draw():
    ellipseMode(RADIUS)
    margin = width*16.0/orig_width
    
    cw = (width-margin*2)/checkers

    background(bg_color)
    pushMatrix()
    translate(margin,margin)
    
    cwo = cw*10/35.0
    cww = cw*10/35.0
    
    # draw checkers
    for y in xrange(checkers):
        for x in xrange(checkers):
            c_idx = (x+y) % 2
            fill(c_colors[c_idx])
            noStroke()
            pushMatrix()
            translate(x*cw+cw/2,y*cw+cw/2)
            rect(-cw/2,-cw/2,cw,cw)
            fill(c_colors[1-c_idx])
            for q in xrange(4):
                if (flags[y*checkers+x] & (1 << q)) > 0:
                    rect(xd[q]*cwo-cww/2,yd[q]*cwo-cww/2,cww,cww)
            popMatrix()
    popMatrix()

    saveFrame("../output/" + output_name + ".png")
    
    