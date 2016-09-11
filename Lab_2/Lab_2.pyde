a = 0
b = 0
c = False

d = 0
e = 20
f = False
def setup():
    size(400,400)
    background(0)
    noStroke()
def draw():
    global a
    global b
    global c
    global d
    global e
    global f
    fill(0,0,255)
    rect(a,b,80,80) 
    if(c == False):   
        a = (a + 1) 
        b = (b + 1) 
        if(a >= 320 and b >= 320):
            c = True
    else:
        a = (a-1) 
        b = (b-1) 
        if(a <= 0 and b <= 0):
            c = False

    fill(255,165,0)
    ellipse(d,e,40,40)
    if (f == False):
        d = d + 10
        if(d == 380):
            f = True
    else:
        d = d - 10
        if(d == 20):
            f = False
       

    

    
