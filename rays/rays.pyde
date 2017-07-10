# Selected reproductions of full page illustrations from the book "Trick Eyes" (2002) by Akiyoshi Kitaoka and other publications

# "Rays" motion illusion appears on page 16
# reference image: http://www.psy.ritsumei.ac.jp/~akitaoka/ei.gif

output_name = "rays"

nbr_bg_checks = 7

bg_colors = [color(11,204,180),color(19,205,220),color(24,174,230),color(24,146,230),color(19,87,200)]
ray_color = color(140,75,75)
black_color = color(0)

orig_meas_width = 508.0
orig_meas_margin = 14.0

def setup():
    size(1024,1024)
    noLoop()

def draw():
    # gradient
    diag = dist(0,0,width,height)
    cx = 0
    cy = 0
    for d in xrange(diag):
        r = d/float(diag)
        r4 = int(r*4)
        r = (r-r4*.25)/0.25
        strokeWeight(2)
        stroke(lerpColor(bg_colors[r4],bg_colors[r4+1],r))
        line(d-width,d+width,d+width,d-width)
    margin = width*orig_meas_margin/orig_meas_width
    checkers = 16
    tw = (width-margin*2)/checkers
    lg_d = tw*0.35
    sm_d = tw*0.25
    e_dist = width*2/orig_meas_width
    e_bot = sm_d*.8
    e_top = sm_d*.98
    pushMatrix()
    translate(margin,margin)
    stroke(black_color)
    strokeWeight(width/orig_meas_width)
    fill(ray_color)
    for y in xrange(checkers):
        for x in xrange(checkers):
            cx = x*tw+tw/2
            cy = y*tw+tw/2
            if x <= 3 or x >= 12 or y <= 3 or y >= 12:
                quad(cx-lg_d,cy-lg_d,
                    cx+sm_d,cy-sm_d,
                    cx+lg_d,cy+lg_d,
                    cx-sm_d,cy+sm_d)
                pushMatrix()
                translate(cx,cy)
                rotate(-PI/4)
                line(e_bot,-e_dist,e_top,-e_dist)
                line(e_bot,+e_dist,e_top,+e_dist)
                popMatrix()
            elif x > 4 and x < 11 and y > 4 and y < 11:
                quad(cx-sm_d,cy-sm_d,
                    cx+lg_d,cy-lg_d,
                    cx+sm_d,cy+sm_d,
                    cx-lg_d,cy+lg_d)
                pushMatrix()
                translate(cx,cy)
                rotate(-(3*PI/4))
                line(e_bot,-e_dist,e_top,-e_dist)
                line(e_bot,+e_dist,e_top,+e_dist)
                popMatrix()
            
    popMatrix()
    saveFrame("../output/" + output_name + ".png")
