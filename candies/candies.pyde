# Selected reproductions of full page illustrations from the book "Trick Eyes" (2002) by Akiyoshi Kitaoka

# "Candy" rotation illusion on page 1
# reference: http://www.psy.ritsumei.ac.jp/~akitaoka/candy2.gif
# rev 2 reference: http://www.psy.ritsumei.ac.jp/~akitaoka/candyrevision2.gif

output_name1 = "candies"       # original: flat background
output_name2 = "candies_rev2"  # rev 2:    gradient background

background_color = color(200,12,11)
candy_color = color(255,19,18)
white = color(255,255,255)

rad1_ratio = .585
rad2_ratio = .773
nbr_candies = 9*4
strokeweight_ratio = .3
diagonal_ratio = 1.5
crosshair_ratio = .05
crosshair_thick_ratio = .2

def setup():
    size(1024,1024)
    noLoop()


def draw_candies(mode):
    
    rwidth,rheight = (width,height)
    rad1 = rwidth*.5*rad1_ratio
    rad2 = rwidth*.5*rad2_ratio
    dot1_rad = (TWO_PI*rad1/nbr_candies)*.33
    dot2_rad = (TWO_PI*rad2/nbr_candies)*.33
    ellipseMode(RADIUS)
    
    background(white)
    fill(background_color)
    noStroke()

    if mode == 0:
        rect(0,0,rwidth, rheight)
    else:
        # radial gradient from  90,0,0  228,15,15
        # blendMode(DARKEST)
        grad = dist(width/2,height/2,0,0)
        for r in xrange(1,grad):
            strokeWeight(2)
            noFill()
            stroke(lerpColor(color( 228,15,15),color(90,0,0),r/float(grad)))
            ellipse(width/2,height/2,r,r)
    
    pushMatrix()
    translate(width/2,height/2)
    
    # draw lines
    stroke(white)
    strokeCap(PROJECT)
    for i in xrange(nbr_candies):
        a = i*TWO_PI/nbr_candies
        a2 = i*TWO_PI/nbr_candies - PI*.25
        x = cos(a)*rad1
        y = sin(a)*rad1
        strokeWeight(dot1_rad*strokeweight_ratio)
        line(x+cos(a2)*dot1_rad*diagonal_ratio, y+sin(a2)*dot1_rad*diagonal_ratio, 
             x+cos(a2+PI)*dot1_rad*diagonal_ratio, y+sin(a2+PI)*dot1_rad*diagonal_ratio) 
        a2 = i*TWO_PI/nbr_candies + PI*.25
        x = cos(a)*rad2
        y = sin(a)*rad2
        strokeWeight(dot2_rad*strokeweight_ratio)
        line(x+cos(a2)*dot2_rad*diagonal_ratio, y+sin(a2)*dot2_rad*diagonal_ratio, 
             x+cos(a2+PI)*dot2_rad*diagonal_ratio, y+sin(a2+PI)*dot2_rad*diagonal_ratio) 
    
    # draw candies
    noStroke()
    fill(candy_color)
    for i in xrange(nbr_candies):
        a = i*TWO_PI/nbr_candies
        x = cos(a)*rad1
        y = sin(a)*rad1
        ellipse(x,y,dot1_rad,dot1_rad)
        x = cos(a)*rad2
        y = sin(a)*rad2
        ellipse(x,y,dot2_rad,dot2_rad)

    crosshair_rad = rwidth*crosshair_ratio*0.5
    crosshair_thick = crosshair_rad * crosshair_thick_ratio
    strokeWeight(crosshair_thick)
    strokeCap(SQUARE)
    stroke(0)
    noFill()
    line(-crosshair_rad,0,crosshair_rad,0)
    line(0,-crosshair_rad,0,crosshair_rad)

    popMatrix()
    
def draw():
    
    draw_candies(0)
    saveFrame("../output/" + output_name1 + ".png")
    
    draw_candies(1)
    saveFrame("../output/" + output_name2 + ".png")
    
    