# Roller Torus

# based on variation by Beau Deeley http://www.horntorus.com/illustration/extern/BeauDeeley_01.jpg
# based on pattern at http://www.psy.ritsumei.ac.jp/~akitaoka/rollersstrong3plastic.jpg

output_name = "roller_torus"
rad = .99;
freq = 30;
shrink = 0.8
lm = 20
tm = 20
stripes = 32

bg_color = color(27,40,225)
circ_color = color(244,114,2)
light_color = color(255,255,255)
dark_color = color(0,0,0)

ribs = 240
detail = 120*2
texture_width = 1024
texture_height = int(texture_width*32.0/42.0)

def setup():
  global tMap 
  size(1200,800, P3D)

  tMap = createGraphics(texture_width,texture_height, P2D)
  draw_circle_pattern(tMap, texture_width/2, texture_height/2, texture_width*.49)
  fov = PI*0.5
  cameraZ = (height/2.0) / tan(fov/2.0)
  perspective(fov, float(width)/float(height), 
              cameraZ/10.0, cameraZ*10.0)
  textureMode(NORMAL)
  textureWrap(REPEAT)
  smooth(8)
  noLoop()

def draw_circle_pattern(tMap, cx,cy,rad):
    sNbr = 0
    shrink = 0.8
    tMap.beginDraw()
    tMap.smooth(8)
    tMap.ellipseMode(RADIUS)
    tMap.noStroke()
    tMap.background(bg_color)
    stripes = 24
    crad = texture_width*0.5*0.66
    bord_scale = 0.8
    tMap.pushMatrix()
    tMap.translate(texture_width/2, texture_height/2)
    tMap.rotate(PI/2)
    tMap.fill(dark_color)
    tMap.arc(0,0,crad,crad,0,PI)
    tMap.fill(light_color)
    tMap.arc(0,0,crad,crad,PI,TWO_PI)
    tMap.fill(circ_color)
    tMap.ellipse(0,0,crad*bord_scale,crad*bord_scale)
    tMap.popMatrix()
    tMap.filter(BLUR)
    tMap.endDraw()

# tube_rad is width of circle cross-section of donut
# mid-point between outer/inner radius
def torus(inner_radius, outer_radius, ribs,detail, textureMap,invert=False):
    global t
    tube_rad = (outer_radius-inner_radius)/2.0
    cx = (inner_radius+outer_radius)/2.0
    cy = 0
    texture_inc = stripes / float(ribs)
    for r in xrange(ribs):
        pushMatrix()
        # rotateX(PI*.3)
        rotateY(r*TWO_PI/ribs)
        beginShape(QUAD_STRIP)
        texture(textureMap)
        for d in xrange(detail+1):
            x = cx + cos(d*TWO_PI/detail)*tube_rad
            y = cy + sin(d*TWO_PI/detail)*tube_rad # * tube_aspect
            # tx = r/float(ribs)
            tx = r*stripes/float(ribs)
            ty = d*stripes*1.3125/float(detail)
            # circumfrence of circle at this x coordinate
            x_circ = TWO_PI*x
            rib_rad = (x_circ/ribs)*0.5
            vertex(x,y,-rib_rad,tx,ty)
            vertex(x,y,rib_rad,tx-texture_inc,ty)
        endShape()
        popMatrix()
            

def draw():
    global t, tMap
    background(255)
    noStroke()
    pushMatrix()
    t = 0 # millis()*0.0002
    camera(0,-height*0.5,-width*.5, # eye
         0,height,0,      # target
         0,1,0)

    v = 80 # ; // map(mouseY,height,0,0,255);
    cx = width/2
    ambientLight(v,v,v) 
    v1 = 128 + sin(-PI/4)*128
    v2 = 128 + cos(-PI/4)*128
    pointLight(v1,v1,v1,cx*0.1,0,cx)  # backlight
    pointLight(v2,v2,v2,cx*0.1,0,-cx) # frontlight
    
            
    # translate(width/2,height/2,-500)
    # rotateX(-TWO_PI*.05)
    # rotateZ(TWO_PI/60)
    # rotateX(PI/2)
    
    # apply lighting here...
    
    # for r in range(200,800,200):
    #     torus(r-200,r+20,ribs,detail,tMap,r%2==0)
    
    torus(66, width, ribs, detail, tMap)
    
    popMatrix()
    # image(tMap,0,0)
    saveFrame("../output/" + output_name + ".png")
