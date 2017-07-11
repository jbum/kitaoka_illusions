import glob, re

def setup():
    size(1280,1536)
    noLoop()
    textFont(createFont("ArialRoundedMTBold",18))
    textAlign(CENTER,CENTER)
             
def draw():
    background(255)
    cw = width/5.0
    ch = cw
    for n,fname in enumerate(glob.glob(sketchPath()+'/../output/*.png')):
        pimg = loadImage(fname)
        x = n%5
        y = n/5
        sc = cw/pimg.width
        pushMatrix()
        translate(x*cw+cw/2,y*ch+ch/2)
        scale(sc)
        image(pimg,-pimg.width/2,-pimg.height/2)
        popMatrix()
            
    for n,fname in enumerate(glob.glob(sketchPath()+'/../output/*.png')):
        x = n%5
        y = n/5
        m = re.search(".*/([\w\-]+)\.png",fname)
        if m:
            txt = m.group(1)
            fill(255,192)
            noStroke()
            rect(x*cw,y*ch+ch-18,cw,18)
            fill(0)
            text(txt, x*cw+cw/2,y*ch+ch-11)
    
    saveFrame("../output/montage.jpg")