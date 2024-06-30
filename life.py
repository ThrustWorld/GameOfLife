from ezgraphics import GraphicsWindow

# global variables
MAX_WIDTH = 400
MAX_HEIGHT = 500
CELL_SIZE = 25
BUTTON_SIZE = 100
CELL_STATUS = [0,1] # 0 -> dead 1 -> live

# Set up window and canvas
window = GraphicsWindow(MAX_WIDTH, MAX_HEIGHT)
window.setTitle("The game of Life")
canvas = window.canvas()

# Button events
def step():
    update_grid(cells)
    return

def clear(cells):
    cells_for_row = (MAX_HEIGHT-100) // CELL_SIZE
    cells_for_col = MAX_WIDTH // CELL_SIZE

    for row in range(cells_for_row):
        for col in range(cells_for_col):
            cells[row][col] = CELL_STATUS[0]
    update_grid(cells)

def glider(cells):
    glider = [[0,0,1],[1,0,1],[0,1,1]]

    rows = (MAX_HEIGHT - 100) // CELL_SIZE
    cols = MAX_WIDTH  // CELL_SIZE

    center_row = (rows // 2) - 1
    center_col = (cols // 2) - 1
    for row in range(3):
        for col in range(3):
            cells[center_row + row][center_col + col] = glider[row][col]
    draw_grid(cells)
    

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

def cell_neighbours(cells,row,col):
    neighbours = 0
    neighbour_offsets = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

    rows = (MAX_HEIGHT - 100) // CELL_SIZE
    cols = MAX_WIDTH // CELL_SIZE

    for offset in neighbour_offsets:
        # taking cells next to the current cell
        new_row = row + offset[0]  
        new_col = col + offset[1] 
        # if the near cell is alive, it's a neighbour
        if 0 <= new_row < rows and 0 <= new_col < cols:
            if cells[new_row][new_col] == CELL_STATUS[1]:
                neighbours += 1
    return neighbours

def toggle_cell(cells,row,col):
    cells[row][col] = not cells[row][col]

def draw_grid(cells):
    cells_for_row = (MAX_HEIGHT - 100) // CELL_SIZE
    cells_for_col = MAX_WIDTH // CELL_SIZE

    canvas.setOutline(255,0,0) # red
    for x in range(cells_for_row):
        for y in range(cells_for_col):
            if cells[x][y] == 0:
                canvas.setFill(255,255,255)
            else:
                canvas.setFill(0,0,0)
            canvas.drawRect(y * CELL_SIZE, x * CELL_SIZE, CELL_SIZE, CELL_SIZE)

def update_grid(cells):
    temp_cells = [] 
    init_cells(temp_cells)
    
    cells_for_row = (MAX_HEIGHT - 100) // CELL_SIZE
    cells_for_col = MAX_WIDTH // CELL_SIZE

    for row in range(cells_for_row):
        for col in range(cells_for_col):
            neighbours = cell_neighbours(cells, row, col)
            cell_value = cells[row][col]

            if cell_value == 1:
                if neighbours > 3 or neighbours < 2:
                    temp_cells[row][col] = 0
                else :
                    temp_cells[row][col] = 1
            elif cell_value == 0:
                if neighbours == 3:
                    temp_cells[row][col] = 1
                else:
                    temp_cells[row][col] = 0

    for row in range(cells_for_row):
        for col in range(cells_for_col):
            cells[row][col] = temp_cells[row][col]
    draw_grid(cells)

cells = []
def start():
    
    # Buttons
    init_buttons()
    
    # List of cells
    init_cells(cells)
    
    # 2d grid
    draw_grid(cells)

def update():
    done = False
    while not done:
        if(window.onMouseDown):

            mouse_xy = window.getMouse() # mouse coordinates for x and y when left mouse button is pressed

            # Change cell status
            if(mouse_xy[1] < MAX_HEIGHT-100):
                row = mouse_xy[1] // CELL_SIZE
                col = mouse_xy[0] // CELL_SIZE
                toggle_cell(cells,row,col)
                draw_grid(cells)

            # Button events
            if mouse_xy[0] > MAX_WIDTH-100 and mouse_xy[1] > MAX_HEIGHT-100: # Quit event
                done = quit()
            elif mouse_xy[0] > MAX_WIDTH-200 and mouse_xy[1] > MAX_HEIGHT-100: # Glider event
                glider(cells)
                print("Glider event!")
            elif mouse_xy[0] > MAX_WIDTH-300 and mouse_xy[1] > MAX_HEIGHT-100: # Clear event
                clear(cells)
                print("Clear event!")
            elif mouse_xy[0] > 0 and mouse_xy[1] > MAX_HEIGHT-100: # Step event
                step()
                print("Step event!")

start()
update()