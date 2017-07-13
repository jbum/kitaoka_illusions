# Selected reproductions of optical illusions by Akiyoshi Kitaoka

# "Rollers" rotation illusion appears on website
# reference image: http://www.ritsumei.ac.jp/~akitaoka/rollers.jpg

# this one isn't quite accurate, might be better to model as 3D cylinders...

output_name = "rollers"
orig_width,orig_height = (903.0,638.0)
bg_color = color(208,210,18)
r_color = color(28,98,254)
bars = 3
nbr_rollers_h,nbr_rollers_v = (8,8)

def setup():
    size(903,638)
    noLoop()

def draw():    
    ellipseMode(RADIUS)
    background(bg_color)
    
    bar_width = width*267/orig_width
    bar_height = height*550/orig_height
    margin_h = (width-bar_width*3)/2.0
    margin_v = (height-bar_height)/2.0
    r_ratio_h,r_ratio_v = (0.9,0.75)
    rx_adjust_scale = 0.985
    r_width = rx_adjust_scale*(r_ratio_h*bar_width/nbr_rollers_h)
    r_height = r_ratio_v*bar_height/nbr_rollers_v
    noStroke()
    for b in xrange(bars):
        pushMatrix()
        translate(margin_h+bar_width*b,margin_v)
        for y in xrange(nbr_rollers_v):
            py = y*r_height/r_ratio_v+r_height/2.0
            px = 0
            for x in xrange(nbr_rollers_h):
                sc = sin(map(x,-1,nbr_rollers_h,0,PI))
                rw = sc*r_width
                px += rw/r_ratio_h + rw/2.0
                noStroke()
                fill(r_color)
                ellipse(px,py,sc*0.9*r_width/2.0,0.9*r_height/2.0)
                noFill()
                strokeCap(SQUARE)
                strokeWeight(width*3.5/orig_width)
                stroke(255*((b%2)==0))
                arc(px,py,sc*r_width/2.0,r_height/2.0,-PI/2,PI/2)
                stroke(255*((b%2)==1))
                arc(px,py,sc*r_width/2.0,r_height/2.0,PI/2,3*PI/2)
        popMatrix()


    saveFrame("../output/" + output_name + ".png")
