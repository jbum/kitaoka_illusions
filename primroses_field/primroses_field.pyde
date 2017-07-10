# Selected reproductions of full page illustrations from the book "Trick Eyes" (2002) by Akiyoshi Kitaoka and other publications

# "Primrose's Field" waving motion illusion appears on page 22
# reference image: http://www.ritsumei.ac.jp/~akitaoka/sakurasfs.jpg

output_name = "primroses_field"

checkers = 17
color1 = color(79,187,129)
color2 = color(159,215,55)
color3 = color(255,255,255)
color4 = color(205,5,152)

def setup():
   size(1024,1024, P2D)
   noLoop()

   smooth(8)
   ellipseMode(RADIUS)

def clover(px,py,dwidth):
    for d in xrange(4):
        pushMatrix()
        translate(px,py)
        rotate(d*TWO_PI/4)
        beginShape()
        vertex(0,0)
        vertex(dwidth/2.0,-dwidth*1/3.0)
        vertex(dwidth,0)
        vertex(dwidth/2.0,dwidth*1/3.0)
        endShape(CLOSE)
        popMatrix()

def draw():
    csize = width/checkers
    
    background(255)
    scramble = [False,True,True,False,True,False,False,True]
    for y in range(checkers):
        for x in range(checkers):
            fill(color1 if (y^x)%2 > 0 else color2)
            noStroke()
            rect(csize*x,csize*y,csize,csize)
    for y in range(checkers-1):
        for x in range(checkers-1):
            ct = (y*7 + x) % 8
            fill(color4 if scramble[ct] else color3)
            noStroke()
            px = csize*(x+1)
            py = csize*(y+1)
            dwidth = csize*1/4.0
            clover(px,py,dwidth)
            # alternates...
            # ellipse(px+4,py,3,3)
            # ellipse(px-4,py,3,3)
            # ellipse(px,py+4,3,3)
            # ellipse(px,py-4,3,3)
            # ellipse(px,py,6,6)
            # quad(px-6,py,px,py+6,px+6,py,px,py-6)

    saveFrame("../output/" + output_name + ".png")