# Selected reproductions of full page illustrations from the book "Trick Eyes" (2002) by Akiyoshi Kitaoka

# "An Approaching Asteroid" motionr illusion, color illusion appears on page 6
# no online reference image found: similar to http://www.psy.ritsumei.ac.jp/~akitaoka/showaku12s.jpg


output_name = "aproaching_asteroid"
bg_color = color(255)
outer_colors = [color(0),color(255)]
inner_colors = [color(0),color(29,0,253)]
ring_color = color(0)

orad_ratio = 110/151.0
irad_ratio = 93/151.0

density = 128 

def setup():
    size(1024,1024)
    noLoop()

def draw():
    cw = width/float(density)
    noStroke()
    for y in xrange(density):
        for x in xrange(density):
            d = dist(density/2.0,density/2.0,x,y)
            if d < irad_ratio*density*0.5:
                fill(inner_colors[int(random(2))])
            elif d > orad_ratio*density*0.5:
                fill(outer_colors[int(random(2))])
            else:
                fill(ring_color)
            rect(x*cw,y*cw,cw,cw)
    saveFrame("../output/" + output_name + ".png")