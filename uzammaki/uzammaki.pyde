# Selected reproductions of optical illusions by Akiyoshi Kitaoka

# "uzummaki ampan" spiral illusion appears on website
# reference image: http://www.ritsumei.ac.jp/~akitaoka/uzuampan2011b.jpg

orig_width = 300.0
orig_rad = 145.0
output_name = "uzummaki_ampan"
bg_color = color(255)
cen_color = color(128)
ring_color = color(176)
spokes = 36
rings = 17

lim = sum([sin(map(i+1,0,rings,0,PI))**2 for i in xrange(rings)]) # 9.5143

def setup():
    size(800,800)
    print "limit",lim
    noLoop()
    
def draw():
    ellipseMode(RADIUS)
    
    background(bg_color)
    pushMatrix()
    translate(width/2,height/2)
    
    rad = width*orig_rad/orig_width
    crad = rad
    s_ang = TWO_PI/spokes
    strokeWeight(width*1.0/orig_width)
    for i in xrange(rings):
        noStroke()
        if i == rings-1:
            fill(cen_color)
            ellipse(0,0,crad,crad)
        else:
            for s in xrange(spokes):
                a1 = s_ang*i/2.0+map(s,0,spokes,0,TWO_PI)
                a2 = s_ang*i/2.0+map(s+1,0,spokes,0,TWO_PI)
                fill(255*(s & 1))
                arc(0,0,crad,crad,a1,a2)
        stroke(ring_color)
        noFill()
        ellipse(0,0,crad,crad)
        crad -= rad*sin(map(i+1,0,rings,0,PI))**2/lim
        
    popMatrix()
    saveFrame("../output/" + output_name + ".png")
        
        
        
        
    
    
    