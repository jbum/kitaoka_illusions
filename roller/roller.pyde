# Roller
# based on variation by Beau Deeley http://www.horntorus.com/illustration/extern/BeauDeeley_01.jpg
# based on pattern at http://www.psy.ritsumei.ac.jp/~akitaoka/rollersstrong3plastic.jpg

output_name = "roller"
rad = .99;
freq = 30;
shrink = 0.8
lm = 20
tm = 20

bg_color = color(27,40,225)
circ_color = color(244,114,2)
light_color = color(255,255,255)
dark_color = color(0,0,0)

output_pic = "opart_28.png"

def setup():
   global opart_shader, ographics
   size(1024,1024)
 
   ellipseMode(RADIUS)
   noLoop()


def draw_circle_pattern(cx,cy,rad):
    sNbr = 0
    shrink = 0.8
    noStroke()
    tm = 0 # millis()*.001
    while rad > 20:
        irad = rad*shrink
        stripes = 42
        pushMatrix()
        translate(cx,cy)
        # rotate(PI/stripes)
        crad = (rad-irad)*.7*.39
        bord_scale = 0.8 # 0.8
        # draw checkers
        for s in range(stripes):
            pushMatrix()
            rotate(s*TWO_PI/stripes)
            pushMatrix()
            translate((irad+rad)/2.0,0)
            rotate(-tm*1.1)
            fill(dark_color)
            arc(0,0,crad,crad,0,PI)
            fill(light_color)
            arc(0,0,crad,crad,PI,TWO_PI)
            fill(circ_color)
            ellipse(0,0,crad*bord_scale,crad*bord_scale)
            popMatrix()
            # draw edges
            
            popMatrix()

        popMatrix()
        rad = irad
        sNbr += 1
        # draw ovals

def draw():
    global lm,tm
    background(bg_color)
    rad = (width-lm*2)/8
    draw_circle_pattern(width/2,height/2,width*.49)
    saveFrame("../output/" + output_name + ".png")
    
