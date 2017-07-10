# Selected reproductions of full page illustrations from the book "Trick Eyes" (2002) by Akiyoshi Kitaoka

# "A Snake" spiral illusion appears on page 9
# reference image: http://www.psy.ritsumei.ac.jp/~akitaoka/hebis.jpg

output_name = "snake_1"
irad_1_ratio = 37/312.0
orad_1_ratio = 47.5/312.0
detail = 4
stripes = 18*2*detail
red_color = color(151,4,102)
white_color = color(255)
bg_color = color(200)

def setup():
    size(1024,1024)
    noLoop()
    
def draw():
    background(bg_color)
    nbr_rings = 0
    irad = width*irad_1_ratio*0.5
    orad = width*orad_1_ratio*0.5
    pushMatrix()
    translate(width/2,height/2)
    noStroke()
    while nbr_rings < 5:
        nbr_rings += 1
        # draw stuff
        strokeWeight(1)
        for s in xrange(stripes):
            fill(red_color if s/detail % 2 > 0 else white_color)
            stroke(red_color if s/detail % 2 > 0 else white_color)
            # noStroke()
            ang1 = s*TWO_PI/stripes
            ang2 = (s+1)*TWO_PI/stripes
            beginShape()
            vertex(cos(ang1)*irad,sin(ang1)*irad)
            vertex(cos(ang1)*orad,sin(ang1)*orad)
            vertex(cos(ang2)*orad,sin(ang2)*orad)
            vertex(cos(ang2)*irad,sin(ang2)*irad)
            endShape(CLOSE)
        noFill()
        sweight = width*2.5/624.0
        strokeWeight(sweight)
        strokeCap(PROJECT)
        for s in xrange(stripes):
            stroke(red_color if s/detail % 2 > 0 else white_color)
            aoffset = detail*PI/stripes
            ang1 = s*TWO_PI/stripes
            ang2 = (s+1)*TWO_PI/stripes
            irad2 = irad+sweight*.4
            orad2 = orad-sweight*.4
            line(cos(ang1+aoffset)*irad2,sin(ang1+aoffset)*irad2,cos(ang2+aoffset)*irad2,sin(ang2+aoffset)*irad2)
            line(cos(ang1-aoffset)*orad2,sin(ang1-aoffset)*orad2,cos(ang2-aoffset)*orad2,sin(ang2-aoffset)*orad2)
        
        irad = orad+(orad-irad)
        orad = irad*orad_1_ratio/irad_1_ratio
    popMatrix()
    saveFrame("../output/" + output_name + ".png")

