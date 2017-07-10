# Selected reproductions of full page illustrations from the book "Trick Eyes" (2002) by Akiyoshi Kitaoka and other publications

# "Rotating Snakes" rotating spiral illusion (does not appear in the 2002 book)
# reference image: http://www.ritsumei.ac.jp/~akitaoka/rotsnake.gif

color1 = color(209,211,18)
color2 = color(29,99,254)
# color1 = color(0,255,255)
# color2 = color(255,0,0)
# color1 = color(255,0,255)
# color2 = color(0,255,0)
# color1 = color(200,200,200)
# color2 = color(100,100,100)


rad = .99;
freq = 42;
shrink = 0.8
lm = 20
tm = 20
output_name = "rotating_snakes"

def setup():
    size(1024,772)
    ellipseMode(RADIUS)
    noLoop()

def draw_circle_pattern(cx,cy,rad,sign):
    print cx,cy,sign
    sNbr = 0
    shrink = 0.8
    noStroke()
    while rad > 5:
        irad = rad*shrink
        stripes = 42
        pushMatrix()
        translate(cx,cy)
        rotate(PI/stripes)
        aColor,bColor = (255,0)
        cColor = color2 if sign > 0 else color1
        dColor = color1 if sign > 0 else color2
        if sNbr % 2 > 0:
            rotate(2*PI/stripes)
        # draw checkers
        for s in range(stripes):
            a1 = s*TWO_PI/stripes
            a2 = (s+1)*TWO_PI/stripes
            fill(aColor if s % 2 > 0 else bColor)
            quad(cos(a1)*irad, sin(a1)*irad,
                 cos(a2)*irad, sin(a2)*irad,
                 cos(a2)*rad, sin(a2)*rad,
                 cos(a1)*rad, sin(a1)*rad)
        oWidth = (rad-irad)/4.0
        oHeight = (rad-irad)/2.0
        for s in range(stripes):
            pushMatrix()
            rotate(s*TWO_PI/stripes)
            fill(cColor if s % 2 > 0 else dColor)
            ellipse((irad+rad)/2.0,0,
                    oHeight,oWidth)
            popMatrix()

        popMatrix()
        rad = irad
        sNbr += 1
        # draw ovals

def draw():
    global lm,tm
    background(255)
    rad = (width-lm*2)/8
    
    for y in range(3):
        for x in range(4):
            cx = lm + rad + rad*2*x
            cy = tm + rad + rad*2*y
            draw_circle_pattern(cx,cy,rad,1 if (y ^ x) % 2 > 0 else -1)

    for y in range(2):
        for x in range(3):
            cx = lm+rad*2 + rad*2*x
            cy = tm+rad*2 + rad*2*y
            draw_circle_pattern(cx,cy,rad,1 if (y ^ x) % 2 > 0 else -1)

    saveFrame("../output/" + output_name + ".png")
