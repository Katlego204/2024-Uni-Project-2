from compass import *
import stdio
import stdarray
import sys
from bee import *
from flower import *
from map import *
from wasp import *
from other_entities import *

gui_mode = int(sys.argv[1])
if gui_mode not in [1, 0]:
    stdio.writeln("ERROR")
if gui_mode == 0:
    pass    
if gui_mode == 1:
    pass

def read_map():
    global bee
    global board
    global size
    global pollen_calc
    global pollen_string
    global pollen_type
    global pollen
    global iterations
    global speed
    
    user_input = stdio.readLine().split()
    size = int(user_input[0])
    iterations = int(user_input[1])
    pollen_type = user_input[2]
    pollen_action = user_input[3]
    pollen_calc = []
    pollen_string = ""
    bee = None
    
    # Configuration Validation
    if pollen_type not in ["f", "s"]:
        stdio.writeln("ERROR: Invalid configuration line")
        return
    if pollen_action not in ["max", "min", "sum", "sort"]:
        stdio.writeln("ERROR: Invalid configuration line")
        return
    if size not in range(0+1, 100+1):
        stdio.writeln("ERROR: Invalid configuration line")
        return
    if (iterations<0):
        stdio.writeln("ERROR: Invalid configuration line")
        return
    if pollen_type == "f":
        if pollen_action not in ["max", "min", "sum"]:
            stdio.writeln("ERROR: Invalid configuration line")
            return
    if pollen_type == "s":
        if pollen_action not in ["sort"]:
            stdio.writeln("ERROR: Invalid configuration line")
            return
        
    board = Map(size=size)
    
    x = None
    pollen = None
    try:
        line = 1
        while not stdio.isEmpty():
            object_data = stdio.readLine().split()
            line += 1
            
            if len(object_data)!=4:
                stdio.writeln(f"ERROR: Invalid object setup on line {line}")
                return
            if object_data[0] not in ["F", "B", "D", "H", "W"]:
                stdio.writeln("ERROR: Invalid configuration line")
                return
            
            x_coord = int(object_data[1])
            y_coord = int(object_data[2])
            
            if x_coord not in range(0, size) or y_coord not in range(0, size):
                stdio.writeln(f"ERROR: Invalid object setup on line {line}")
                return
            
            # FLOWER VALIDATION
            if object_data[0] == "F":
                n_pollen = int(object_data[3])
                flower = Flower(y_coord, x_coord, pollen_type)
                if pollen_type == "f": # if the pollen_type is a float
                    for i in range(int(n_pollen)):
                        try:
                            x = float(stdio.readLine().split()[0])
                            line += 1
                        except ValueError:
                            stdio.writeln(f"ERROR: Invalid object setup on line {line+1}")
                        pollen_calc.append(x)
                if pollen_type == "s": # if pollen_type is a string
                    for j in range(int(n_pollen)):
                        try:
                            x = stdio.readLine().split()[0]
                            pollen_calc.append(x)
                            line += 1
                        except ValueError:
                            stdio.writeln(f"ERROR: Invalid object setup on line {line+1}")
                if pollen_action == "sum":
                    pollen = sum(pollen_calc)
                if pollen == "max":
                    pollen = max(pollen_calc)
                if pollen_action == "min":
                    pollen = min(pollen_calc)
                if pollen_action == "sort":
                    pollen_calc.sort()
                    for i in pollen_calc:
                        pollen_string += i
                        pollen_string += " "
                board.place_entity(flower, "F")
                
            # BEE HIVE VALIDATION
            elif object_data[0] == "B":
                n_entities = int(object_data[3])
                characteristics = stdio.readLine().split()
                line += 1
                if len(characteristics)!=2:
                    stdio.writeln(f"ERROR: Invalid object setup on line {line}")
                    return
                speed = int(characteristics[0])
                perception = int(characteristics[1])
                bee = Bee(y_coord, x_coord, n_entities, speed, perception)
                board.place_entity(bee, "B")
                
            # WASP HIVE VALIDATION
            elif object_data[0] == "W":
                n_entities = int(object_data[3])
                characteristics = stdio.readLine().split()
                if len(characteristics)!=1:
                    stdio.writeln(f"ERROR: Invalid object setup on line {line}")
                    return
                speed = int(characteristics[0])
                wasp = Wasp(y_coord, x_coord, n_entities, speed)
                board.place_entity(wasp, "W")
            
            # HONEYBEE HIVE VALIDATION
            elif object_data[0] == "H":
                n_entities = int(object_data[3])
                characteristics = stdio.readLine().split()
                if len(characteristics)!=2:
                    stdio.writeln(f"ERROR: Invalid object setup on line {line}")
                    return
                speed = int(characteristics[0])
                hive = Hive(y_coord, x_coord, n_entities, speed)
                board.place_entity(hive, "H")
            
            #DESERTBEE HIVE VALIDATION
            elif object_data[0]=="D":
                n_entities = int(object_data[3])
                characteristics = stdio.readLine().split()
                if len(characteristics)!=2:
                    stdio.writeln(f"ERROR: Invalid object setup on line {line}")
                    return
                speed = int(characteristics[0])
                perception = int(characteristics[1])
                hive = Hive(y_coord, x_coord, n_entities, speed)
                board.place_entity(hive, "D")
        
        if (len(pollen_calc)==0) and (len(pollen_string)==0):
            pollen = "No pollen collected"
            
    except EOFError:
        stdio.writeln("ERROR: Invalid configuration line")
        return
    except ValueError:
        return
    except IndexError:
        return
    
def test_compass(row, col, speed, size, n_moves):
    # Initialize the compass with the given row, column, and speed
    compass_0 = Compass(row, col, speed)

    #create a list of the coordinates such that you'll be able to index into it
    list = []
    list.append((row, col))
    
    # Print the initial position
    #stdio.writeln(f"{row}, {col}")

    # Calculate and print subsequent locations
    for move in range(n_moves):

        traj = compass_0.get_next_trajectory()

        # Calculate the new position based on the traj
        distance_0 = traj.get_distance() #here we get the distance of the entity
        #here we get the direction of the entity
        direction_0 = traj.get_direction_in_degrees()
        
        new_row = row
        new_col = col
        if (direction_0 == 0) or (direction_0 == 360):
            new_col += distance_0
        if (direction_0 == 45):
            new_row += distance_0
            new_col += distance_0
        if (direction_0 == 90):
            new_row += distance_0
        if (direction_0 == 135):
            new_row += distance_0
            new_col -= distance_0
        if (direction_0 == 180):
            new_col -= distance_0
        if (direction_0 == 225):
            new_row -= distance_0
            new_col -= distance_0
        if (direction_0 == 270):
            new_row -= distance_0
        if (direction_0 == 315):
            new_row -= distance_0
            new_col += distance_0
        
        # Bound the movement by the map size
        if new_row not in range(0, size-1):
            if new_row < 0:
                new_row = 0
            elif new_row >= size:
                new_row = size - 1
        if new_col not in range(0, size-1):
            if new_col < 0:
                new_col = 0
            elif new_col >= size:
                new_col = size - 1

        # exchange values
        row = new_row
        col = new_col
        #append the new coordinates
        list.append((row, col))
        # Print the new position
        #stdio.writeln(f"{row}, {col}")
    return list

def bee_coordinates(row, col, speed, size, n_moves):
    '''getting the new coordinates of the bee'''
    return test_compass(row, col, speed, size, n_moves)

def game_loop():
    global bee_coord
    read_map()

    # displaying the original board
    # board.game_map(size, size)
    running = True
    move = 0
    if bee == None:
        pass
    else:
        bee_coord = bee_coordinates(bee.x_coord, bee.y_coord, speed, size, iterations)
        
    while running: # game loop

        if move == iterations:
            running = False
        
        # moving the bee
        if bee == None:
            pass
        else:
            row, col = bee_coord[move]
            if board.board[row][col] == "B":
                board.game_map(size, size)
                pass
            elif board.board[row][col] == " ":
                board.board[row][col] = "b"
                board.game_map(size, size) # display the board
                board.board[row][col] = " "  # after displaying the board move the entity from the position
            elif board.board[row][col] == "F": # if it encounters a flower
                board.board[row][col] = "F"
                board.game_map(size,size)
                board.board[row][col] = "F"
            else:
                stdio.writeln("OCCUPIED")
        
        move+=1  # this controls how many times the program runs (iterations)



if __name__ == "__main__":
    #start by calling the read_map function
    game_loop()
    # displaying the pollen collected
    stdio.writeln("Answer:")
    if pollen_type=="f":
        if len(pollen_calc) == 0:
            pollen = "No pollen collected"
        if bee == None:
            pollen = "No pollen collected"
        stdio.writeln(pollen)
    if pollen_type == "s":
        if len(pollen_string)==0:
            pollen_string = "No pollen collected"
        if bee == None:
            pollen_string = "No pollen collected"
        stdio.writeln(pollen_string)
    # print(iterations)