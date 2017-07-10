# Selected reproductions of full page illustrations from the book "Trick Eyes" (2002) by Akiyoshi Kitaoka

# "Tiger" rotational illusion appears on page 7
# reference image: http://www.psy.ritsumei.ac.jp/~akitaoka/yellowOuchib.jpg

output_name = "tiger"
yellow_color = color(255,255,24)
black_color = color(0,0,0)
stripes = 30
band_ratio = 17/64.0
r1_ratio = 240/400.0
r2_ratio = 320/400.0
r_inc_ratio = .0005
a_inc_ratio = 1/80.0

ctr_max = 11

def setup():
    size(1024,1024)
    noLoop()

myscale = 2  # oddly, higher scales look worse...
def draw():
    imap = createGraphics(width*myscale,height*myscale)
    imap.beginDraw()
    imap.loadPixels()
    n = 0
    for y in xrange(imap.height):
        yf = map(y,0,imap.height,-1,1)
        for x in xrange(imap.width):
            xf = map(x,0,imap.width,-1,1)
            d = dist(0,0,xf,yf)
            inverse = d > r1_ratio and d < r2_ratio
            if inverse:
                xf = -xf
            a = atan2(yf,xf)+PI
            colors = (yellow_color,black_color) if sin(a*.5*stripes-log(d)*PI*6) > 0 else (black_color,yellow_color)
            # pixels[n] = yellow_color if sin(a*.5*stripes-log(d)*PI*6) > 0 else black_color
            imap.pixels[n] = colors[0] if sin(a*2*stripes+log(d)*PI*22) > 0 else colors[1]
            n += 1
    imap.updatePixels()
    imap.endDraw()
    image(imap,0,0,width,height)
    saveFrame("../output/" + output_name + ".png")
            
def old_draw():
    mrad = dist(0,0,width/2,height/2)
    a_offset = 0
    pushMatrix()
    translate(width/2,height/2)
    ctr = 0
    y_stripe = 0
    r = 1
    strokeCap(SQUARE)
    while r < mrad:
        strokeWeight(TWO_PI*r*r_inc_ratio*2)
        inverse = r > width*r1_ratio and r < width*r2_ratio
        for s in xrange(stripes):
            a1 = a_offset + s*TWO_PI/stripes
            a2 = a_offset + (s+1)*TWO_PI/stripes
            if inverse:
                x1,y1 = (-cos(a1)*r,sin(a1)*r)
                x2,y2 = (-cos(a2)*r,sin(a2)*r)
            else:
                x1,y1 = (cos(a1)*r,sin(a1)*r)
                x2,y2 = (cos(a2)*r,sin(a2)*r)
            stroke(yellow_color if (s ^ y_stripe) % 2 > 0 else black_color)
            line(x1,y1,x2,y2)
        ctr += 1
        if ctr > ctr_max:
            y_stripe += 1
            ctr = 0
        a_offset += a_inc_ratio * TWO_PI/(stripes)
        r += TWO_PI*r*r_inc_ratio
    
    