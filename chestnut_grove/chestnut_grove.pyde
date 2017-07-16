# Selected reproductions of full page illustrations from the book "Trick Eyes" (2002) by Akiyoshi Kitaoka and other publications

# "A Chestnut Grove" geometrical illusion appears on page 45
# no online reference image found, note "autumn color" uses the same algorithm


output_name = "chestnut_grove"

checkers = 21
ccolors = [color(255),color(231,231,219),color(218,180,160),color(187,148,62),color(104,15,26),color(0)]
o_color = color(187,211,141)
bg_color = color(255)

orig_width = 512

def setup():
    size(1024,1024)
    noLoop()
    ccolors = []
        

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