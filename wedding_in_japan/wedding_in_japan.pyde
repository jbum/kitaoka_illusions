# Selected reproductions of full page illustrations from the book "Trick Eyes" (2002) by Akiyoshi Kitaoka and other publications

# "Wedding in Japan" motion illusion / geometrical illusion appears on page 15
# no reference image found

output_name = "wedding_in_japan"

nbr_bg_checks = 7

bg_color = color(255)
bg_check_color = color(102,121,67)
fg_check_colors = [color(255),color(0),color(255,20,20,),color(255)]
pattern = (0,1,0,1,1,0,1,0)

def setup():
    size(1024,1024)
    noLoop()

def draw():
    gw = (nbr_bg_checks*2-1)
    background(bg_color)
    
    tw = width/float(gw)
    noStroke()
    for y in xrange(gw):
        for x in xrange(gw):
            if (x+y)%2 == 0:
                fill(bg_check_color)
                rect(x*tw,y*tw,tw,tw)
    mw = tw*2/3
    mr = mw/2.0
    strokeWeight(width*1/640.0)
    for y in xrange(1,gw):
        for x in xrange(1,gw):
            pat = pattern[(y*7+x)%len(pattern)]
            if y == 1:
                print (y*7+x)%len(pattern)
            fill(fg_check_colors[2*pat])
            stroke(fg_check_colors[1+2*pat])
            rect(x*tw-mr,y*tw-mr,mw,mw)
    saveFrame("../output/" + output_name + ".png")
