from ezgraphics import GraphicsWindow

# global variables
MAX_WIDTH = 400
MAX_HEIGHT = 400
CELL_SIZE = 25
BUTTON_SIZE = 100

# Set up window and canvas
window = GraphicsWindow(MAX_WIDTH, MAX_HEIGHT)
canvas = window.canvas()

# Button events
def step():
    #TODO
    return
def clear():
    canvas.setFill(255,255,255)
    draw_grid(MAX_WIDTH,MAX_HEIGHT-100)
    init_cells(cells)
def glider():
    #TODO
    return
def quit():
    return True


def init_buttons():
    # 1.Step
    canvas.drawRect(0,MAX_HEIGHT-100,BUTTON_SIZE,BUTTON_SIZE)
    canvas.drawText(35,335,"STEP")
    # 2.Clear
    canvas.drawRect(MAX_WIDTH-300,MAX_HEIGHT-100,BUTTON_SIZE,BUTTON_SIZE)
    canvas.drawText(130,335,"CLEAR")
    # 3.Glider
    canvas.drawRect(MAX_WIDTH-200,MAX_HEIGHT-100,BUTTON_SIZE,BUTTON_SIZE)
    canvas.drawText(230,335,"GLIDER")
    # 4.Quit
    canvas.drawRect(MAX_WIDTH-100,MAX_HEIGHT-100,BUTTON_SIZE,BUTTON_SIZE)
    canvas.drawText(335,335,"QUIT")


def init_cells(cells_list):
    cells_for_row = (MAX_HEIGHT-100) // CELL_SIZE
    cells_for_col = MAX_WIDTH // CELL_SIZE

    for i in range(cells_for_col):
        for j in range(cells_for_row):
            cells_list.append(0) # 0 = DEAD


def draw_grid(width,height):
    cells_for_row = height // CELL_SIZE
    cells_for_col = width // CELL_SIZE

    canvas.setOutline(255,0,0) # red
    for i in range(cells_for_row):
        for j in range(cells_for_col):   
             canvas.drawRect(j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE)


cells = []
def start():
    window.setTitle("The game of Life")
    # Buttons
    init_buttons()
    
    # List of cells
    init_cells(cells)
    
    # 2d grid
    draw_grid(MAX_WIDTH,MAX_HEIGHT-100)

def update():
    done = False
    while not done:
        mouse_xy = window.getMouse() # mouse coordinates for x and y when left mouse button is pressed

        # Button events
        if mouse_xy[0] > MAX_WIDTH-100 and mouse_xy[1] > MAX_HEIGHT-100: # Quit event
            done = quit()
        elif mouse_xy[0] > MAX_WIDTH-200 and mouse_xy[1] > MAX_HEIGHT-100: # Glider event
            #glider()
            print("Glider event!")
        elif mouse_xy[0] > MAX_WIDTH-300 and mouse_xy[1] > MAX_HEIGHT-100: # Clear event
            clear()
            print("Clear event!")
        elif mouse_xy[0] > 0 and mouse_xy[1] > MAX_HEIGHT-100: # Step event
            #step()
            print("Step event!")

start()
update()