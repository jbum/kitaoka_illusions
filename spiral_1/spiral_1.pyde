# Selected reproductions of full page illustrations from the book "Trick Eyes" (2002) by Akiyoshi Kitaoka

# "Red Spiral" spiral color illusion appears on page 26
# reference image: http://www.psy.ritsumei.ac.jp/~akitaoka/redspiral.gif

# "Green Spiral" spiral color illusion appears on page 27 - exact same thing with red->green
# reference image: http://www.psy.ritsumei.ac.jp/~akitaoka/grnspiral.gif

output_name = "red_spiral"
s_colors = [color(0,0,255),color(255,0,0),color(255,255,0)]

# output_name = "green_spiral"
# s_colors = [color(0,0,255),color(0,255,0),color(255,255,0)]

stripes = 30
band_ratio = 17/64.0
r1_ratio = 240/400.0
r2_ratio = 320/400.0
r_inc_ratio = .0005
a_inc_ratio = 1/80.0

stripes = [[0,2],[1,2],[0,2],[0,1]]


ctr_max = 11

def setup():
    size(1024,1024)
    noLoop()

myscale = 2  # oddly, higher scales look worse...

to_stripes = 4
fro_stripes = 120
to_scale = 25.2
fro_scale = 100

def draw():
    imap = createGraphics(width*myscale,height*myscale)
    imap.beginDraw()
    imap.loadPixels()
    n = 0
    sc1 = to_scale
    sc2 = fro_scale
    for y in xrange(imap.height):
        yf = map(y,0,imap.height,-1,1)
        for x in xrange(imap.width):
            xf = map(x,0,imap.width,-1,1)
            d = dist(0,0,xf,yf)
            a1 = (atan2(xf,yf)+PI)*to_stripes
            a2 = (atan2(yf,xf)+PI)*fro_stripes
            ctr4 = int((a1+log(d*sc1*TWO_PI+.01)*sc1)/TWO_PI) % 4
            ctr2 = int((a2+log(d*sc2*TWO_PI+.01)*sc2)/TWO_PI) % 2
            ctr = stripes[ctr4][ctr2]
            # imap.pixels[n] = s_colors[int((a1+log(d*sc1*TWO_PI+.01)*sc1)/TWO_PI) % 4]   works
            imap.pixels[n] = s_colors[ctr]
            n += 1
    imap.updatePixels()
    imap.endDraw()
    image(imap,0,0,width,height)
    saveFrame("../output/" + output_name + ".png")
            
