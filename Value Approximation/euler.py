def y_euler(x0,y0,b,h):
    n = b-x0/h
    y = y0
    x = x0
    for i in range (1,n+1):
        y = y + h*f(x,y)
        x = x + h
    return y
