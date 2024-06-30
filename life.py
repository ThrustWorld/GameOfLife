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


def draw_grid(width,height):
    cell_size = 25
    cells_for_row = width // cell_size
    cells_for_col = height // cell_size
    
    cells_list = []

    # list of cells
    for i in range(cells_for_col):
        for j in range(cells_for_row):
            cells_list.append(0)


    # grid
    canvas.setOutline(255,0,0)
    for i in range(cells_for_row):
        for j in range(cells_for_col):   
             canvas.drawRect(i * cell_size,j * cell_size, cell_size, cell_size)


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

draw_grid(400,300)

done = False
while not done:
    mouse_xy = window.getMouse() # mouse coordinates for x and y when left mouse button is pressed

    # Button events
    
    if mouse_xy[0] > 300 and mouse_xy[1] > 300: # Quit event
        done = quit()
    elif mouse_xy[0] > 200 and mouse_xy[1] > 300: # Glider event
        #glider()
        print("Glider event!")
    elif mouse_xy[0] > 100 and mouse_xy[1] > 300: # Clear event
        #clear()
        print("Clear event!")
    elif mouse_xy[0] > 0 and mouse_xy[1] > 300: # Step event
        #step()
        print("Step event!")