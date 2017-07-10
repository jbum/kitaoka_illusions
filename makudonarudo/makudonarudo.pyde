# Selected reproductions of full page illustrations from the book "Trick Eyes" (2002) by Akiyoshi Kitaoka and other publications

# "Majudonarudo" (McDonald's) motion illusion / geometrical illusion appears on page 13
# reference image here: http://www.psy.ritsumei.ac.jp/~akitaoka/mcdonaldb.jpg

output_name = "makudonarudo"
stripes = 31
stripe_colors = [color(255,20,20),color(255,150,150)]
boat_colors = [color(150,150,10),color(255,255,25)]
dot_colors = [color(0),color(150),color(255),color(150)]

def setup():
    size(969,551)
    ellipseMode(RADIUS)
    noLoop()

def draw_cherry(ctr,x,y):
    global dot_rad
    fill(dot_colors[(ctr%2)*2])
    ellipse(x,y,dot_rad,dot_rad)
    fill(dot_colors[(ctr%2)*2+1])
    ellipse(x,y,dot_rad*.3,dot_rad*.3)

def draw():
    global dot_rad
    sheight = height/float(stripes)
    bwidth = width*36/969.0
    background(0)
    noStroke()
    for i in xrange(stripes):
        fill(stripe_colors[i % 2])
        py = sheight*i
        rect(0,py,width,sheight)
    
    dot_rad = sheight*.25
    top_x = width*31/969.0
    bot_x = width*155/969.0
    
    seams = (width*258/969.0,width*712/969.0)
    for seam in seams:
        for y in xrange(1,stripes-1):
            x1 = map(y,1,stripes-2,top_x,bot_x)
            x2 = map(y+1,1,stripes-2,top_x,bot_x)
            y1 = y*sheight
            y2 = (y+1)*sheight
            for sgn in (-1,1):
                fill(boat_colors[(y-1)%2])
                px1 = seam+(x1)*sgn
                px2 = seam+(x1+bwidth)*sgn
                px3 = seam+(x2+bwidth)*sgn
                px4 = seam+(x2)*sgn
                py1 = y1
                py2 = y2
                quad(px1,y1, px2,y1, px3,y2, px4,y2)
                if y > 1:
                    draw_cherry(y,px1,py1)
                    draw_cherry(y+1,px2,py1)
                        
       
    saveFrame("../output/" + output_name + ".png")

        
        

