# Selected reproductions of full page illustrations from the book "Trick Eyes" (2002) by Akiyoshi Kitaoka and other publications

# "Joro-gumo" motion illusion, geometrical illusion appears on page 19
# reference image: http://www.ritsumei.ac.jp/~akitaoka/jorogumo.gif

output_name = "joro-gumo"

subsquares = 48
orig_meas_width = 384

scolors = [color(0),color(255,255,25)]
lcolors = [color(255,20,20),color(128)]


def setup():
    size(1024,1024)
    noLoop()

def draw():
    tw = width/float(subsquares)
    background(0)
    strokeWeight(1)
    for y in range(subsquares):
        for x in range(subsquares):
            if x < 12 or y < 12 or x >= subsquares-12 or y >= subsquares-12:
                ctr = ((1+x+y*5) % 6)/3
            else:  
                ctr = ((2+x+y) % 6)/3
            fill(scolors[ctr])
            stroke(scolors[ctr])
            rect(x*tw,y*tw,tw,tw)
    noFill()
    strokeWeight(width*1/float(orig_meas_width))
    stroke(lcolors[0])
    for x in xrange(1,subsquares,2):
        line(x*tw,0,x*tw,height)
    stroke(lcolors[1])
    for y in xrange(1,subsquares,2):
        line(0,y*tw,width,y*tw)
    

    saveFrame("../output/" + output_name + ".png")
    