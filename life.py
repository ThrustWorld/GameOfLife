from ezgraphics import GraphicsWindow

# global variables
MAX_WIDTH = 400
MAX_HEIGHT = 500
CELL_SIZE = 25
BUTTON_SIZE = 100
CELL_STATUS = [0,1] # 0 -> dead 1 -> live
CELLS_FOR_ROW = (MAX_HEIGHT - 100) // CELL_SIZE
CELLS_FOR_COL = MAX_WIDTH // CELL_SIZE
# Set up window and canvas
window = GraphicsWindow(MAX_WIDTH, MAX_HEIGHT)
window.setTitle("The game of Life")
canvas = window.canvas()

# Button events
def step():
    update_cells(cells,True)
    return

def clear(cells):
    for row in range(CELLS_FOR_ROW):
        for col in range(CELLS_FOR_COL):
            cells[row][col] = CELL_STATUS[0]
    update_cells(cells,True)

def glider(cells):
    glider = [[0,0,1],
              [1,0,1],
              [0,1,1]]

    center_row = (CELLS_FOR_ROW // 2) - 1 #  - 1 = first square on the row based on glider's pattern
    center_col = (CELLS_FOR_COL // 2) - 2 #  - 2 = first square on the col based on glider's pattern
    for row in range(3):
        for col in range(3):
            cells[center_row + row][center_col + col] = glider[row][col]
    update_cells(cells,True)
    

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
    for i in range(CELLS_FOR_ROW):
        row = [0] * CELLS_FOR_COL
        cells_list.append(row)


def check_neighbours(cells,row,col):
    neighbours = 0
    neighbour_offsets = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)] # neighbours' pattern

    for offset in neighbour_offsets:
        # taking cells around the current cell
        new_row = row + offset[0]  
        new_col = col + offset[1]
        # if the near cell is alive, it's a neighbour
        if new_row < CELLS_FOR_ROW and new_col < CELLS_FOR_COL:
            if cells[new_row][new_col] == CELL_STATUS[1]:
                neighbours += 1
    return neighbours

def toggle_cell(cells,row,col):
    if cells[row][col] == CELL_STATUS[0]:
        cells[row][col] = CELL_STATUS[1]
    else:
        cells[row][col] = CELL_STATUS[0]

squares = []
def update_grid(cells,must_clean):
    # If I have ids, it means I have elements inside the canvas that need to be eliminated before creating them again
    if(len(squares) > 0 and must_clean is True):
        for id in squares:
            canvas.removeItem(id) # Cleaning canvas to prevent performance issues by removing the 
        squares.clear()
    # Population of the canvas with cells: white if dead(0) or black if alive(1)
    for x in range(CELLS_FOR_ROW):
        for y in range(CELLS_FOR_COL):
            if cells[x][y] == CELL_STATUS[0]:
                canvas.setFill(255,255,255)
            else:
                canvas.setFill(0,0,0) 
            id = canvas.drawRect(y * CELL_SIZE, x * CELL_SIZE, CELL_SIZE, CELL_SIZE) # Used to clean the canvas during recalculations
            squares.append(id) # List that contains the id for each element of the canvas that we have drawn

    print(len(squares))    

old_cells = []
def draw_cell(cells):
    for x in range(CELLS_FOR_ROW):
        for y in range(CELLS_FOR_COL):
            if cells[x][y] != old_cells[x][y]:
                if cells[x][y] == CELL_STATUS[0]:
                    canvas.setFill(255,255,255)
                else:
                    canvas.setFill(0,0,0) 
                id = canvas.drawRect(y * CELL_SIZE, x * CELL_SIZE, CELL_SIZE, CELL_SIZE) # Used to clean the canvas during recalculations
                squares.append(id) # List that contains the id for each element of the canvas that we have drawn
            old_cells[x][y] = cells[x][y]
    print(len(squares)) 

def draw_grid():
    canvas.setOutline(255,0,0) # red
    for i in range(CELLS_FOR_ROW):
        canvas.drawLine(0,i * CELL_SIZE,MAX_WIDTH,i * CELL_SIZE)
    for j in range(CELLS_FOR_COL):
        canvas.drawLine(j * CELL_SIZE,0,j * CELL_SIZE,MAX_HEIGHT-100)   

def update_cells(cells, must_clean):
    temp_cells = [] 
    init_cells(temp_cells)
    # Update cells status
    for row in range(CELLS_FOR_ROW):
        for col in range(CELLS_FOR_COL):
            neighbours = check_neighbours(cells, row, col)
            cell_value = cells[row][col]
            if cell_value == CELL_STATUS[1]: # live
                if neighbours > 3 or neighbours < 2:  # Overpopulation/Underpopulation -> 0 -> dead cell
                    temp_cells[row][col] = CELL_STATUS[0]
                else :
                    temp_cells[row][col] = CELL_STATUS[1]
            elif cell_value == CELL_STATUS[0]: # dead
                if neighbours == 3: # Reproduction -> 1 -> live cell
                    temp_cells[row][col] = CELL_STATUS[1]
                else:
                    temp_cells[row][col] = CELL_STATUS[0]
    # Update cells value before redrawing them
    for row in range(CELLS_FOR_ROW):
        for col in range(CELLS_FOR_COL):
            cells[row][col] = temp_cells[row][col]
    update_grid(cells,must_clean)

cells = []
def start():
    # Buttons
    init_buttons()
    # List of dead cells
    init_cells(cells)
    init_cells(old_cells)
    # 2d grid with dead cells
    draw_grid()

def update():
    done = False
    while not done:
        if(window.onMouseDown):
            mouse_xy = window.getMouse() # mouse coordinates for x and y when mouse button is pressed
            # Change cell status if we pressed inside the 2d grid
            if(mouse_xy[1] < MAX_HEIGHT-100):
                row = mouse_xy[1] // CELL_SIZE
                col = mouse_xy[0] // CELL_SIZE
                toggle_cell(cells,row,col)
                draw_cell(cells)
            # Raise the button event equal to mouse pos
            if mouse_xy[0] > MAX_WIDTH-100 and mouse_xy[1] > MAX_HEIGHT-100: # Quit event
                done = quit()
            elif mouse_xy[0] > MAX_WIDTH-200 and mouse_xy[1] > MAX_HEIGHT-100: # Glider event
                glider(cells)
                #print("Glider event!")
            elif mouse_xy[0] > MAX_WIDTH-300 and mouse_xy[1] > MAX_HEIGHT-100: # Clear event
                clear(cells)
                #print("Clear event!")
            elif mouse_xy[0] > 0 and mouse_xy[1] > MAX_HEIGHT-100: # Step event
                step()
                #print("Step event!")


start()
update()