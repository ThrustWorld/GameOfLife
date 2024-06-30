from ezgraphics import GraphicsWindow

# global variables
MAX_WIDTH = 400
MAX_HEIGHT = 500
CELL_SIZE = 25
BUTTON_SIZE = 100
CELL_STATUS = [0,1]
# Set up window and canvas
window = GraphicsWindow(MAX_WIDTH, MAX_HEIGHT)
canvas = window.canvas()

# Button events
def step():
    #TODO
    return
def clear():
    draw_grid(MAX_WIDTH,MAX_HEIGHT-100)
def glider():
    #TODO
    return
def quit():
    return True

def init_buttons():
    # 1.Step
    canvas.drawRect(0,MAX_HEIGHT-100,BUTTON_SIZE,BUTTON_SIZE)
    canvas.drawText(35,445,"STEP")
    # 2.Clear
    canvas.drawRect(MAX_WIDTH-300,MAX_HEIGHT-100,BUTTON_SIZE,BUTTON_SIZE)
    canvas.drawText(130,445,"CLEAR")
    # 3.Glider
    canvas.drawRect(MAX_WIDTH-200,MAX_HEIGHT-100,BUTTON_SIZE,BUTTON_SIZE)
    canvas.drawText(230,445,"GLIDER")
    # 4.Quit
    canvas.drawRect(MAX_WIDTH-100,MAX_HEIGHT-100,BUTTON_SIZE,BUTTON_SIZE)
    canvas.drawText(335,445,"QUIT")


def init_cells(cells_list):
    cells_for_row = (MAX_HEIGHT-100) // CELL_SIZE
    cells_for_col = MAX_WIDTH // CELL_SIZE

    # table
    for i in range(cells_for_row):
        row = [0] * cells_for_col
        cells_list.append(row)

def change_cell_status(mouse):
    x = mouse[0]
    y = mouse[1]
    
    pos_x = x // CELL_SIZE
    pos_y = y // CELL_SIZE

    cells_for_row = (MAX_HEIGHT-100) // CELL_SIZE
    cells_for_col = MAX_WIDTH // CELL_SIZE
    for i in range(cells_for_row):
        for j in range(cells_for_col):
            if cells[i][j] == CELL_STATUS[0]:
                canvas.setColor(0,0,0)
                canvas.drawRect(pos_x*CELL_SIZE, pos_y* CELL_SIZE, CELL_SIZE, CELL_SIZE)

def draw_grid(cells,width,height):
    init_cells(cells)
    
    cells_for_row = height // CELL_SIZE
    cells_for_col = width // CELL_SIZE

    canvas.setOutline(255,0,0) # red
    for x in range(cells_for_row):
        for y in range(cells_for_col):
            if cells[x][y] == 0:
                canvas.setFill(255,255,255)
            else:
                canvas.setFill(0,0,0)
            canvas.drawRect(y * CELL_SIZE, x * CELL_SIZE, CELL_SIZE, CELL_SIZE)


cells = []
def start():
    window.setTitle("The game of Life")
    # Buttons
    init_buttons()
    
    # List of cells
    init_cells(cells)
    cells[0][0] = 1
    cells[2][1] = 1

    # 2d grid
    draw_grid(cells,MAX_WIDTH,MAX_HEIGHT-100)

def update():
    done = False
    while not done:
        mouse_xy = window.getMouse() # mouse coordinates for x and y when left mouse button is pressed

        # Change cell status
        if(window.onMouseDown and mouse_xy[1] < MAX_HEIGHT-100):
            change_cell_status(mouse_xy)

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