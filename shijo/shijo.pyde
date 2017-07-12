# Selected reproductions of full page illustrations from the book "Trick Eyes" (2002) by Akiyoshi Kitaoka

# "Shijo-dori Boogie-woogie" op effect, motion illusion appears on page 34
# reference image: http://www.ritsumei.ac.jp/~akitaoka/shijo.gif

output_name = "shijo"

margin_checkers = 2
gw = 16*3 # checkers across

c_colors = [color(0),color(29,0,254),color(255)]
bg_color = color(255)

patlen = 12

def setup():
    size(1040,1040) # intentionally a multiple of gw+margin_checkers*2 for sharp pixel boundaries
    noLoop()
    ellipseMode(RADIUS)

def get_pat(x):
    return ((x+1)/3) & 0x01

def get_color_index(x,y):
    x = x % (patlen*2)
    y = y % (patlen*2)
    if (x >= patlen) == (y < patlen):
        # invert
        x = 11-(x % 12)
        return (get_pat((x+y*(patlen-1)) % patlen))+1
    else:
        return get_pat((x+y*(patlen-1)) % patlen)*2


def dashed_line(x1,y1,x2,y2):
    line(x1,y1,x2,y2)  # needs work
    
def dashed_rect(x,y,w,h):
    dashed_line(x,y,x+w,y)
    dashed_line(x+w,y,x+w,y+h)
    dashed_line(x+w,y+h,x,y+h)
    dashed_line(x,y+h,x,y)

def draw():
    
    cw = width/float(gw+margin_checkers*2)
    
    background(bg_color)
    pushMatrix()
    translate(margin_checkers*cw,margin_checkers*cw)
    
    # draw checkers
    for y in xrange(gw):
        for x in xrange(gw):
            c_idx = get_color_index(x,y)
            fill(c_colors[c_idx])
            noStroke()
            rect(x*cw,y*cw,cw,cw)

    # draw red lines
    clip(0,0,gw*cw,gw*cw)
    cwd = dist(0,0,cw,cw)
    noFill()
    stroke(255,0,0)
    for y in xrange(3):
        yo = patlen*cw*y*2
        xo = 12*cw
        # stroke(0,255,0)
        for x in xrange(3): 
            for r in xrange(1,5):
                pushMatrix()
                translate(xo+x*24*cw,yo)
                rotate(PI/4)
                rad = 1.5*r*cwd
                dashed_rect(-rad,-rad,rad*2,rad*2)
                popMatrix()
            

        xo = 0
        yo = patlen*cw*(y*2+1)
        # stroke(255,0,0)
        for x in xrange(3): 
            for r in xrange(1,5):
                pushMatrix()
                translate(xo+x*24*cw,yo)
                rotate(PI/4)
                rad = 1.5*r*cwd
                dashed_rect(-rad,-rad,rad*2,rad*2)
                popMatrix()
    
    noClip()
    popMatrix()

    
    saveFrame("../output/" + output_name + ".png")
    
    