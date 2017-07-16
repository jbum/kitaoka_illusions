# Selected reproductions of full page illustrations from the book "Trick Eyes" (2002) by Akiyoshi Kitaoka and other publications

# "Autumn Color" geometrical illusion appears on page 44
# no online reference image found, note "chestnut grove" uses the same algorithm

output_name = "autumn_color"

checkers = 21

ccolors = [
           color(255),color(255,255,20),color(255,205,20),color(255,128,20),color(255,20,20),color(0),
           ]

o_color = color(255,20,20)
bg_color = color(255)

orig_width = 512

def setup():
    size(1024,1024)
    noLoop()

def base_ctr(i):
    im = i % 10
    return (im % 5) if im < 5 else 5-(im % 5)

def draw():
    margin = 8*width/float(orig_width)
    tw = (width-margin*2)/float(checkers)
    background(bg_color)
    
    strokeWeight(width*1/float(orig_width))
    pushMatrix()
    translate(margin,margin)
    for y in xrange(checkers):
        y_ctr = base_ctr(y)
        for x in xrange(checkers):
            x_ctr = base_ctr(x)
            py = y*tw
            px = x*tw
            stroke(o_color)
            ctr = abs(y_ctr - x_ctr)
            fill(ccolors[ctr])
            rect(px,py,tw,tw)
    popMatrix()
    saveFrame("../output/" + output_name + ".png")