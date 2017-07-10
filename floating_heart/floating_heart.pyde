# Selected reproductions of full page illustrations from the book "Trick Eyes" (2002) by Akiyoshi Kitaoka and other publications

# "The Floating Heart" color illusion / motion illusion appears on page 14
# reference image here: http://www.ritsumei.ac.jp/~akitaoka/heart-u.gif

output_name = "floating_heart"

pat = '''
.*.*.*.*.*.*.*.*.*.*.*.
*.*.*.*.*.*.*.*.*.*.*.*
.*.*.*.*.*.*.*.*.*.*.*.
*.*.*.....*.*.....*.*.*
.*.*..+.+..*..+.+..*.*.
*.*..+.+.+...+.+.+..*.*
.*..+.+.+.+.+.+.+.+..*.
*..+.+.+.+.+.+.+.+.+..*
.*..+.+.+.+.+.+.+.+..*.
*..+.+.+.+.+.+.+.+.+..*
.*..+.+.+.+.+.+.+.+..*.
*.*..+.+.+.+.+.+.+..*.*
.*.*..+.+.+.+.+.+..*.*.
*.*.*..+.+.+.+.+..*.*.*
.*.*.*..+.+.+.+..*.*.*.
*.*.*.*..+.+.+..*.*.*.*
.*.*.*.*..+.+..*.*.*.*.
*.*.*.*.*..+..*.*.*.*.*
.*.*.*.*.*...*.*.*.*.*.
*.*.*.*.*.*.*.*.*.*.*.*
.*.*.*.*.*.*.*.*.*.*.*.
'''

bg_color = color(255,20,20)
check_color = color(20,255,20)
heart_color = color(0)

# pattern is 23 x 21
def setup():
    size(1012,924)
    noLoop()

def draw():
    background(bg_color)
    noStroke()
    lines = pat.lstrip().rstrip().split('\n')
    checksize = width/float(len(lines[0]))
    for y,line in enumerate(lines):
        for x,ch in enumerate(line):
            if ch == '+':
                fill(heart_color)
            elif ch == '*':
                fill(check_color)
            else:
                continue
            rect(x*checksize,y*checksize,checksize,checksize)
    saveFrame("../output/" + output_name + ".png")
