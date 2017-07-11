# Selected reproductions of full page illustrations from the book "Trick Eyes" (2002) by Akiyoshi Kitaoka

# "Fever" rotation illusion on page 33 (also appears on cover)
# reference image: http://www.psy.ritsumei.ac.jp/~akitaoka/fever.jpg

stripes = 36*2

output_name = "fever"
dk_stripe_color= color(251,18,53)
lt_stripe_color = color(226,199,19)
s_colors = [dk_stripe_color, lt_stripe_color]
white_dot_color = color(255,255,255)
blue_dot_color = color(30,0,250)
d_colors = [white_dot_color, blue_dot_color]
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
    for i in xrange(stripes):
        a1 = i*TWO_PI/stripes
        a2 = (i+1)*TWO_PI/stripes
        fill(s_colors[i % 2])
        arc(0,0,rad,rad,a1,a2)
        fill(s_colors[(i+1) % 2])
        arc(0,0,rad2,rad2,a1,a2)
        fill(s_colors[i % 2])
        arc(0,0,rad1,rad1,a1,a2)
    for i in xrange(stripes):
        a1 = i*TWO_PI/stripes
        a2 = (i+1)*TWO_PI/stripes
        r1 = TWO_PI*rad1/(stripes*4)
        r2 = TWO_PI*rad2/(stripes*4)
        r1i = r1/3.5
        r2i = r2/3.5
        fill(d_colors[i % 2])
        ellipse(cos(a1)*rad1,sin(a1)*rad1,r1,r1)
        ellipse(cos(a1)*rad2,sin(a1)*rad2,r2,r2)
        fill(d_colors[(i+1) % 2])
        ellipse(cos(a1)*rad1,sin(a1)*rad1,r1i,r1i)
        ellipse(cos(a1)*rad2,sin(a1)*rad2,r2i,r2i)
    popMatrix()
    saveFrame("../output/" + output_name + ".png")