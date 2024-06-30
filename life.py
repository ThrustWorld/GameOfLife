from ezgraphics import GraphicsWindow

window = GraphicsWindow()
window.setTitle("The game of Life")

canvas = window.canvas()

def step():
    #TODO
    return
def clear():
    #TODO
    return
def glider():
    #TODO
    return
def quit():
    return True

# Buttons
# 1.Step
canvas.drawRect(0,300,100,100)
canvas.drawText(35,335,"STEP")
# 2.Clear
canvas.drawRect(100,300,100,100)
canvas.drawText(130,335,"CLEAR")
# 3.Glider
canvas.drawRect(200,300,100,100)
canvas.drawText(230,335,"GLIDER")
# 4.Quit
canvas.drawRect(300,300,100,100)
canvas.drawText(335,335,"QUIT")

done = False
while not done:
    mouse_xy = window.getMouse() # mouse coordinates when it's pressed

    # Button events
    
    if mouse_xy[0] > 300 and mouse_xy[1] < 400: # Quit event
        done = quit()
    elif mouse_xy[0] > 200 and mouse_xy[1] < 400: # Glider event
        #glider()
        print("Glider event!")
    elif mouse_xy[0] > 100 and mouse_xy[1] < 400: # Clear event
        #clear()
        print("Clear event!")
    elif mouse_xy[0] > 0 and mouse_xy[1] < 400: # Step event
        #step()
        print("Step event!")