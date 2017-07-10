# Selected reproductions of full page illustrations from the book "Trick Eyes" (2002) by Akiyoshi Kitaoka and other publications

# "Ferry Boats" motion illusion / geometrical illusion appears on page 12
# reference image found under the name "watashi": http://www.psy.ritsumei.ac.jp/~akitaoka/watashib.jpg



output_name = "ferryboats"
stripes = 31
stripe_colors = [color(106,136,254),color(187,220,255)]
boat_colors = [color(128),color(192)]
dot_colors = [color(0),color(150),color(255),color(150)]

def setup():
    size(912,517)
    ellipseMode(RADIUS)
    noLoop()

def draw_cherry(ctr,x,y):
    global cherry_rad
    fill(dot_colors[(ctr%2)*2])
    ellipse(x,y,cherry_rad,cherry_rad)
    fill(dot_colors[(ctr%2)*2+1])
    ellipse(x,y,cherry_rad*.3,cherry_rad*.3)

def draw():
    global cherry_rad
    sheight = height/float(stripes)
    bwidth = sheight * 2
    background(0)
    noStroke()
    for i in xrange(stripes):
        fill(stripe_colors[i % 2])
        py = sheight*i
        rect(0,py,width,sheight)
    
    cherry_rad = sheight*.25
        
    for b in xrange(2):
        for y in xrange(1,stripes-1):
            px1 = map(y,1,stripes-2,sheight,sheight*8) + b*bwidth*2
            px2 = map(y+1,1,stripes-2,sheight,sheight*8) + b*bwidth*2
            py1 = y*sheight
            py2 = (y+1)*sheight
            fill(boat_colors[(y-1)%2])
            quad(px1,py1, px1+bwidth,py1, px2+bwidth,py2,px2,py2)
            quad(width-px1,height-py1, width-(px1+bwidth),height-py1, width-(px2+bwidth),height-py2,width-px2,height-py2)
            if y > 1:
                draw_cherry(y,px1,py1)
                draw_cherry(y+1,px1+bwidth,py1)
                draw_cherry(y,width-px1,height-py1)
                draw_cherry(y+1,width-px1-bwidth,height-py1)
                        
    oy = (9+13)*sheight
    ox1 = map(9+13,1,stripes-2,sheight,sheight*8)+bwidth*4
    ox2 = map(9+13+13,1,stripes-2,sheight,sheight*8)+bwidth*4
    for b in xrange(6):
          for y in xrange(13):
              fill(boat_colors[y%2])
              px1 = map(y,0,12,ox1,ox2)+b*bwidth*2
              px2 = map(y+1,0,12,ox1,ox2)+b*bwidth*2
              py1 = (9+13-y)*sheight
              py2 = py1 - sheight
              quad(px1,py1,px1+bwidth,py1,px2+bwidth,py2,px2,py2)
              if y > 0:
                  draw_cherry(y+1,px1,py1)
                  draw_cherry(y,px1+bwidth,py1)
        
    saveFrame("../output/" + output_name + ".png")

        
        
