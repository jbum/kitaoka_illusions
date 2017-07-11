# Selected reproductions of full page illustrations from the book "Trick Eyes" (2002) by Akiyoshi Kitaoka

# "Snakes, the Eto of 2001" rotation illusion appears on page 18
# Reference Image: http://www.psy.ritsumei.ac.jp/~akitaoka/hebi2001.gif

output_name = "negajo_2011"
bg_color = color(178)
c_colors = (color(0),color(255))
tongue_color = color(254,19,18)
eye_color = color(255)

orig_width = 417
orig_height = 484


def setup():
    size(1024,1188) # orig is 417 x 484
    noLoop()

def snake_tail(px,py,ang,fg_color):
    global cw
    pushMatrix()
    translate(px,py)
    rotate(ang)
    fill(fg_color)
    strokeWeight(1)
    stroke(fg_color)
    arc(0,0,cw*2,cw,-PI/2,PI/2)
    popMatrix()
    
def snake_head(px,py,ang,fg_color,eye_color,sc=1.0):
    global cw,sw
    pushMatrix()
    translate(px,py)
    rotate(ang)
    scale(sc,1.0)
    
    # head
    fill(fg_color)
    strokeWeight(1)
    stroke(fg_color)
    rect(0,-cw,cw*2,cw*2)
    ellipse(cw*2,0,cw,cw)
    noStroke()
    fill(bg_color)
    arc(cw*3,0,cw,cw,0,PI)
    fill(eye_color)
    ellipse(cw*2,-cw/2,cw*.15,cw*.15)
    
    # tongue
    stroke(tongue_color)
    noFill()
    strokeWeight(sw)
    strokeCap(ROUND)
    beginShape()
    curveVertex(cw*2+sw,sw)
    curveVertex(cw*2+sw,sw)
    curveVertex(cw*3,cw*0.5)
    curveVertex(cw*4,cw*1-sw)
    curveVertex(cw*4,cw*1-sw)
    endShape()
    beginShape()
    curveVertex(cw*2+sw,sw*2)
    curveVertex(cw*2+sw,sw)
    curveVertex(cw*3,cw*0.4)
    curveVertex(cw*4,sw)
    curveVertex(cw*4,sw)
    endShape()
    noStroke()
    
    
    
    popMatrix()

def draw():
    global cw,sw
    ellipseMode(RADIUS)
    
    sw = width*1.5/orig_width
    cw = width*10.0/orig_width
    lm = width*23.0/orig_width
    tm = height*55.0/orig_height
    
    gw,gh = (32,38)
    
    background(bg_color)
    pushMatrix()
    translate(lm,tm)
    
    # interior
    x_ofst = 0
    x_ofst_dir = 1

    # top/bot heads/tails
    for x in xrange(0,gw,2):
        px1 = x*cw+cw
        py1 = 0*cw+cw*2
        px2 = x*cw+cw
        py2 = (gh-2)*cw
        ctr = (x/2)%2
        noStroke()
        fill(c_colors[(x/2) % 2])
        if ctr == 0:
            snake_head(px1,py1,-PI/2,c_colors[0],c_colors[1])
            snake_tail(px2,py2,PI/2,c_colors[0])
        else:
            snake_tail(px1,py1,-PI/2,c_colors[1])
            snake_head(px2,py2,PI/2,c_colors[1],c_colors[0])

    # left/right heads/tails
    x_ofst = 1
    x_ofst_dir = 1
    for y in xrange(2,gh-2):
        px1 = (x_ofst)*cw+cw
        py1 = y*cw
        px2 = (x_ofst+gw-2)*cw
        py2 = y*cw
        if y % 2 == 1:
            if (5+y) % 6 != 0:
                if x_ofst_dir > 0:
                    snake_head(px1,py1,-PI,c_colors[0],c_colors[1])
                    snake_head(px2,py2,0,c_colors[1],c_colors[0])
                else:
                    print "!"
                    snake_head(px1+cw,py1,0,c_colors[0],c_colors[1],sc=-1)
                    snake_head(px2,py2,-PI,c_colors[1],c_colors[0],sc=-1)
            else:
                fill(0)
                stroke(0)
                strokeWeight(1)
                rect(px1-cw,py1-cw,cw,cw*2)
                fill(255)
                stroke(255)
                rect(px2+cw,py2-cw,cw,cw*2)
        x_ofst += x_ofst_dir
        if x_ofst == 6:
            x_ofst = 5
            x_ofst_dir = -1
        elif x_ofst == -1:
            x_ofst = 0
            x_ofst_dir = 1

    x_ofst = 1
    x_ofst_dir = 1
    for y in xrange(2,gh-1):
        if y < gh-2:
            for x in xrange(1,gw-1):
                px = (x_ofst+x)*cw
                py = y*cw
                fill(c_colors[(x/2) % 2])
                stroke(c_colors[(x/2) % 2])
                strokeWeight(1)
                rect(px,py,cw,cw)
        if (5+y) % 6 != 0:
            stroke(bg_color)
            strokeWeight(sw)
            line(0,y*cw,width,y*cw)
        x_ofst += x_ofst_dir
        if x_ofst == 6:
            x_ofst = 5
            x_ofst_dir = -1
        elif x_ofst == -1:
            x_ofst = 0
            x_ofst_dir = 1


    popMatrix()
    saveFrame("../output/" + output_name + ".png")
        
    