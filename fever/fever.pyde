# Selected reproductions of full page illustrations from the book "Trick Eyes" (2002) by Akiyoshi Kitaoka

# "Fever" rotation illusion on page 33 (also appears on cover)
# reference image: http://www.psy.ritsumei.ac.jp/~akitaoka/fever.jpg

stripes = 36*2

output_name = "fever"
dk_stripe_color= color(251,18,53)
lt_stripe_color = color(226,199,19)
white_dot_color = color(255,255,255)
gray_dot_color = color(30,0,250)
background_color = color(255,255,255)

def setup():
    size(1024,1024)
    noLoop()

def draw():
    rad = width*.48
    rad1 = rad*.642
    rad2 = rad*.800
    ellipseMode(RADIUS)
    background(background_color)
    fill(dk_stripe_color)
    noStroke()
    pushMatrix()
    translate(width/2,height/2)
    blendMode(DARKEST) # helps reduce artifacts in center
    for i in xrange(stripes):
        a1 = i*TWO_PI/stripes
        a2 = (i+1)*TWO_PI/stripes
        fill(dk_stripe_color if i % 2 > 0 else lt_stripe_color)
        beginShape()
        vertex(0,0)
        vertex(cos(a1)*rad1,sin(a1)*rad1)
        vertex(cos(a2)*rad1,sin(a2)*rad1)
        endShape(CLOSE)
        fill(dk_stripe_color if i % 2 == 0 else lt_stripe_color)
        beginShape()
        vertex(cos(a1)*rad1,sin(a1)*rad1)
        vertex(cos(a2)*rad1,sin(a2)*rad1)
        vertex(cos(a2)*rad2,sin(a2)*rad2)
        vertex(cos(a1)*rad2,sin(a1)*rad2)
        endShape(CLOSE)
        fill(dk_stripe_color if i % 2 > 0 else lt_stripe_color)
        beginShape()
        vertex(0,0)
        vertex(cos(a1)*rad2,sin(a1)*rad2)
        vertex(cos(a2)*rad2,sin(a2)*rad2)
        vertex(cos(a2)*rad,sin(a2)*rad)
        vertex(cos(a1)*rad,sin(a1)*rad)
        endShape(CLOSE)
    blendMode(BLEND)
    for i in xrange(stripes):
        a1 = i*TWO_PI/stripes
        a2 = (i+1)*TWO_PI/stripes
        r1 = TWO_PI*rad1/(stripes*4)
        r2 = TWO_PI*rad2/(stripes*4)
        r1i = r1/3.5
        r2i = r2/3.5
        fill(white_dot_color if i % 2 == 0 else gray_dot_color)
        ellipse(cos(a1)*rad1,sin(a1)*rad1,r1,r1)
        ellipse(cos(a1)*rad2,sin(a1)*rad2,r2,r2)
        fill(white_dot_color if i % 2 > 0 else gray_dot_color)
        ellipse(cos(a1)*rad1,sin(a1)*rad1,r1i,r1i)
        ellipse(cos(a1)*rad2,sin(a1)*rad2,r2i,r2i)
    popMatrix()
    saveFrame("../output/" + output_name + ".png")