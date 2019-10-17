import herr0092_library as f

f.randomBgColor()
f.clearConsole()

ball =  [
[0,0,0,1,1,0,0,0],
[0,0,1,1,1,1,0,0],
[0,1,1,1,1,1,1,0],
[0,1,1,1,1,1,1,0],
[0,1,1,1,1,1,1,0],
[0,1,1,1,1,1,1,0],
[0,0,1,1,1,1,0,0],
[0,0,0,1,1,0,0,0]
]

x = 0
y = 0

vx = 2
vy = 2

# f.displayObjectNoAnimation( ball, x, y )

# f.dormir(0.3)

# f.eraseObject( ball, 10, 10 )

# f.dormir(0.3)

# newCoords = f.moveObject( ball, 10, 10 ) # , x=10,y=10,vx=10,vy=10

# newCoords = f.checkCollision(ball, x, y, 1, 1 )
# f.randomBgColor()

while ( True ):
    x = x + vx
    y = y + vy

    f.eraseObject( ball, x, y )

    collideX, collideY = f.checkCollision(ball, x, y, vx, vy )    

    if ( collideX ):
        f.randomBgColor()
        vx = vx * -1
    
    if ( collideY ):
        f.randomBgColor()
        vy = vy * -1

    f.moveObject(ball, x, y, vx, vy )
    f.dormir(0.08)
    




