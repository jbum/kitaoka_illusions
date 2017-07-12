import glob, re

cw,ch = (178,178)
gw,gh = (5,7)

def setup():
    size(890,1246) # cw*gw, ch*gh
    noLoop()
    textFont(loadFont("HelveticaNeue-Light-18.vlw"),18)
    textAlign(CENTER,CENTER)
             
def draw():
    global gw,gh,cw,ch
    background(255)
    for n,fname in enumerate(glob.glob(sketchPath()+'/../output/*.png')):
        pimg = loadImage(fname)
        x = n%gw
        y = n/gw
        sc = float(cw)/pimg.width
        pushMatrix()
        translate(x*cw+cw/2.0,y*ch+ch/2.0)
        scale(sc)
        image(pimg,-pimg.width/2,-pimg.height/2)
        popMatrix()
            
    for n,fname in enumerate(glob.glob(sketchPath()+'/../output/*.png')):
        x = n%gw
        y = n/gw
        m = re.search(".*/([\w\-]+)\.png",fname)
        if m:
            txt = m.group(1)
            fill(255,200)
            noStroke()
            rect(x*cw,y*ch+ch-24,cw,24)
            fill(20)
            text(txt, x*cw+cw/2,y*ch+ch-14)
    
    saveFrame("../output/montage.jpg")