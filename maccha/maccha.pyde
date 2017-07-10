# Selected reproductions of full page illustrations from the book "Trick Eyes" (2002) by Akiyoshi Kitaoka

# "Maccha" motion illusion appears on page 8
# reference image: http://www.psy.ritsumei.ac.jp/~akitaoka/macchacircleplastics.jpg

output_name = "maccha"
background_color = color(149,202,12)
dark_green_color = color(0,100,2)
white_color = color(255)
gray_color = color(192)
dot_rad_ratio = .005

def setup():
    size(1024,1024)
    noLoop()

def draw():
    stripes = 16
    nbr_samples = 20
    amp = 1.2*width/stripes
    margin = height/8.0
    background(background_color)
    for i in xrange(stripes):
        strokeWeight(0.65*(width-margin*2)/float(stripes))
        strokeCap(SQUARE)
        stroke(dark_green_color if i % 2 == 0 else white_color)
        noFill()
        beginShape()
        xc = map(i,0,stripes-1,margin,width-margin)
        # vertex(margin,xc)
        for y in xrange(-2,nbr_samples+2):
            py = map(y,0,nbr_samples-1,margin,height-margin)
            ang = map(y,0,nbr_samples-1,0,TWO_PI*2)
            px = xc - sin(ang)*amp
            curveVertex(px,py)
        # vertex(height-margin,xc)
        endShape()
    nbr_dot_rows = 5
    ellipseMode(RADIUS)
    fill(gray_color)
    noStroke()
    dot_rad = width*dot_rad_ratio
    for i in xrange(stripes):
        px = map(i,0,stripes-1,margin,width-margin)
        yd = (height-margin*2)*0.25
        for i in xrange(5):
            py = margin+yd*i
            ellipse(px,py,dot_rad,dot_rad)
    saveFrame("../output/" + output_name + ".png")

        
    