# Selected reproductions of full page illustrations from the book "Trick Eyes" (2002) by Akiyoshi Kitaoka and other publications

# "Petit Tomatoes" motion illusion appears on page 17
# reference image: http://www.ritsumei.ac.jp/~akitaoka/tomato1.gif

output_name = "petit_tomatoes"

check_colors = [color(255,20,20),color(255,148,20)]
star_colors = [color(0,150,20),color(255)]

def setup():
   size(1024,1024)
   noLoop()

def quadstar(dsize):
    beginShape()
    vertex(0,-dsize)
    quadraticVertex(0,0,dsize,0)
    quadraticVertex(0,0,0,dsize)
    quadraticVertex(0,0,-dsize,0)
    quadraticVertex(0,0,0,-dsize)
    endShape()

diag_checkers = 31
wide_checkers = 16

def draw():
    background(255)
    cwidth = dist(0,0,width,height)/diag_checkers
    cdiag = width/16.0 # distance(0,0,cwidth,cwidth) should be about the same
    noStroke()
    dsize = cwidth*.4
    for y in range(wide_checkers):
        for x in range(wide_checkers):
            cx = cdiag/2 + x*cdiag
            cy = cdiag/2 + y*cdiag
            fill(check_colors[0])
            quad(cx-cdiag/2,cy,cx,cy-cdiag/2,cx+cdiag/2,cy,cx,cy+cdiag/2)
            if y < wide_checkers-1 and x < wide_checkers-1:
                cx += cdiag/2
                cy += cdiag/2
                fill(check_colors[1])
                quad(cx-cdiag/2,cy,cx,cy-cdiag/2,cx+cdiag/2,cy,cx,cy+cdiag/2)
    for y in range(wide_checkers):
        for x in range(wide_checkers):
            cx = cdiag/2 + x*cdiag
            cy = cdiag/2 + y*cdiag
            if y < wide_checkers-1:
                pushMatrix()
                translate(cx,cy+cdiag/2)
                rotate(PI/4)
                dx = abs(x-7.5)
                dy = abs(y-7)
                is_flipped = (dx+dy) < 4
                ctr = (0 + is_flipped) % 2
                fill(star_colors[ctr])
                quadstar(dsize)
                popMatrix()
            if y < wide_checkers-1 and x < wide_checkers-1:
                cx += cdiag/2
                cy += cdiag/2
                pushMatrix()
                translate(cx,cy+cdiag/2)
                rotate(PI/4)
                dx = abs(x-7)
                dy = abs(y-6.5)
                is_flipped = (dx+dy) < 4
                ctr = (1 + is_flipped) % 2
                fill(star_colors[ctr])
                quadstar(dsize)
                popMatrix()
    saveFrame("../output/" + output_name + ".png")
               
    
    