from compass import *
import stdio
import stdarray
import sys
from bee import *
from honeybee import *
from desertbee import *
from wasp import *
from map import Map
class Map:
    def __init__(self, size: int):
        self.size = size
        self.board = stdarray.create2D(size, size, " ")

    def place_entity(self, entity, entity_type: str):
        if entity == Flower:
            pass
        else:
            if self.board[entity.col][entity.row] == " ":
                self.board[entity.col][entity.row] = entity_type
            else:
                stdio.writeln(f"ERROR: Cannot place {entity_type} at already occupied location "
                            f"({entity.col}, {entity.row})")

    def display_board(self):
        for row in self.board:
           stdio.writeln(" ".join(row))
           
    def game_map(self, row, col):

        stdio.write("    ")
        for i in range(col):
            stdio.write(f"{i:03}")
            stdio.write(" ")
        stdio.writeln()

        stdio.write("   ")
        for ii in range(col):
            stdio.write("+---")
        stdio.writeln("+")
        
        for iii in range(row-1,0-1, -1):
            stdio.write(f"{iii:03}")
            for block in self.board[iii]:
                stdio.write("|")
                stdio.write(f" {block} ")
            stdio.writeln("|") 
            #add the +-- below the blocks
            stdio.write("   ")
            stdio.write("+---"*col)
            stdio.writeln("+")

class BeeHive:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.position = (row, col)
        self.bees = []
        
    def add_bee(bee):
        bees.append(bee)

class Bee:
    def __init__(self, row, col, speed, perception, size):
        self.row = row
        self.col = col
        self.speed = speed
        self.perception = perception
        self.size = size
        self.compass = Compass(row, col, speed)
        
    def move_to_hive(self):
        #shortest path strategy
        row, col = self.position
        hive_x, hive_y = self.hive.position
        if col < hive_x:
            col += 1
        elif col > hive_x:
            col -= 1
        if row < hive_y:
            row += 1
        elif row > hive_y:
            row -= 1
        self.postion = (col, row)
        
    def move_bee(self):
        """Updates the bee's coordinates using the compass logic."""
        traj = self.compass.get_next_trajectory()
        distance_0 = traj.get_distance()
        direction_0 = traj.get_direction_in_degrees()

        # Calculate new row and col based on direction
        new_row, new_col = self.row, self.col
        if direction_0 == 0 or direction_0 == 360:
            new_col += distance_0
        elif direction_0 == 45:
            new_row += distance_0
            new_col += distance_0
        elif direction_0 == 90:
            new_row += distance_0
        elif direction_0 == 135:
            new_row += distance_0
            new_col -= distance_0
        elif direction_0 == 180:
            new_col -= distance_0
        elif direction_0 == 225:
            new_row -= distance_0
            new_col -= distance_0
        elif direction_0 == 270:
            new_row -= distance_0
        elif direction_0 == 315:
            new_row -= distance_0
            new_col += distance_0

        # Keep bee within the board bounds
        if new_row < 0:
            new_row = 0
        elif new_row >= self.size:
            new_row = self.size - 1

        if new_col < 0:
            new_col = 0
        elif new_col >= self.size:
            new_col = self.size - 1

        self.row, self.col = new_row, new_col
    
class Flower:
    def __init__(self, row, col,):
        self.row = row
        self.col = col
        self.position = (row, col)
        self.pollen = []
        
    def add_pollen(self, pollen):
        self.pollen.append(pollen)

class WaspHive:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.wasps = []
        
    def add_wasp(wasp):
        wasps.append(wasp)
    
class Wasp:
    def __init__(self, row: int, col: int, speed: int, size: int):
        self.row = row
        self.col = col
        self.speed = speed
        self.size = size
        self.compass = Compass(row, col, speed)
    
        
    def move_wasp(self):
        """Updates the bee's coordinates using the compass logic."""
        traj = self.compass.get_next_trajectory()
        distance_0 = traj.get_distance()
        direction_0 = traj.get_direction_in_degrees()

        # Calculate new row and col based on direction
        new_row, new_col = self.row, self.col
        if (direction_0 == 0) or (direction_0 == 360):
            new_col += distance_0
        elif direction_0 == 45:
            new_row += distance_0
            new_col += distance_0
        elif direction_0 == 90:
            new_row += distance_0
        elif direction_0 == 135:
            new_row += distance_0
            new_col -= distance_0
        elif direction_0 == 180:
            new_col -= distance_0
        elif direction_0 == 225:
            new_row -= distance_0
            new_col -= distance_0
        elif direction_0 == 270:
            new_row -= distance_0
        elif direction_0 == 315:
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

        self.row, self.col = new_row, new_col

class DesertBee:
    def __init__(self, row: int, col: int, speed: int, perception: int, size: int):
        self.row = row
        self.col = col
        self.speed = speed
        self.perception = perception
        self.size = size
        self.compass = Compass(row, col, speed)
        
    def move_dbee(self):
        """Updates the bee's coordinates using the compass logic."""
        traj = self.compass.get_next_trajectory()
        distance_0 = traj.get_distance()
        direction_0 = traj.get_direction_in_degrees()

        # Calculate new row and col based on direction
        new_row, new_col = self.row, self.col
        if direction_0 == 0 or direction_0 == 360:
            new_col += distance_0
        elif direction_0 == 45:
            new_row += distance_0
            new_col += distance_0
        elif direction_0 == 90:
            new_row += distance_0
        elif direction_0 == 135:
            new_row += distance_0
            new_col -= distance_0
        elif direction_0 == 180:
            new_col -= distance_0
        elif direction_0 == 225:
            new_row -= distance_0
            new_col -= distance_0
        elif direction_0 == 270:
            new_row -= distance_0
        elif direction_0 == 315:
            new_row -= distance_0
            new_col += distance_0

        # Keep bee within the board bounds
        if new_row < 0:
            new_row = 0
        elif new_row >= self.size:
            new_row = self.size - 1

        if new_col < 0:
            new_col = 0
        elif new_col >= self.size:
            new_col = self.size - 1

        self.row, self.col = new_row, new_col

class DesertBeeHive:
    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col
        self.dbees = []

    def add_bee(bee):
        dbees.append(bee)
        
class HoneyBeeHive:
    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col
        self.hbees = []

    def add_bee(bee):
        hbees.append(bee)
    
class HoneyBee:
    def __init__(self, row: int, col: int, speed: int, perception: int, size: int):
        self.row = row
        self.col = col
        self.speed = speed
        self.size = size
        self.perceptiion = perception
        self.compass = Compass(row, col, speed)
    
    def move_dbee(self):
        """Updates the bee's coordinates using the compass logic."""
        traj = self.compass.get_next_trajectory()
        distance_0 = traj.get_distance()
        direction_0 = traj.get_direction_in_degrees()

        # Calculate new row and col based on direction
        new_row, new_col = self.row, self.col
        if direction_0 == 0 or direction_0 == 360:
            new_col += distance_0
        elif direction_0 == 45:
            new_row += distance_0
            new_col += distance_0
        elif direction_0 == 90:
            new_row += distance_0
        elif direction_0 == 135:
            new_row += distance_0
            new_col -= distance_0
        elif direction_0 == 180:
            new_col -= distance_0
        elif direction_0 == 225:
            new_row -= distance_0
            new_col -= distance_0
        elif direction_0 == 270:
            new_row -= distance_0
        elif direction_0 == 315:
            new_row -= distance_0
            new_col += distance_0

        # Keep bee within the board bounds
        if new_row < 0:
            new_row = 0
        elif new_row >= self.size:
            new_row = self.size - 1

        if new_col < 0:
            new_col = 0
        elif new_col >= self.size:
            new_col = self.size - 1

        self.row, self.col = new_row, new_col


    
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
    global bees
    global bee_hive
    global wasp_hive
    global wasps
    global dbees
    global dbee_hive
    global hbees
    global hbee_hive
    
    user_input = stdio.readLine().split()
    size = int(user_input[0])
    iterations = int(user_input[1])
    pollen_type = user_input[2]
    pollen_action = user_input[3]
    pollen_calc = []
    pollen_string = ""
    bee = None
    bees = []
    wasps = []
    dbees = []
    hbees = []
    
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
            
            col = int(object_data[1])
            row = int(object_data[2])
            
            if col not in range(0, size) or row not in range(0, size):
                stdio.writeln(f"ERROR: Invalid object setup on line {line}")
                return
            
            # FLOWER VALIDATION
            if object_data[0] == "F":
                n_pollen = int(object_data[3])
                flower = Flower(row=row, col=col)
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
                #bee = Bee(row, col, speed, perception, size)
                for i in range(n_entities):
                    bee = Bee(col, row, speed, perception, size)
                    BeeHive.add_bee(bee)
                    # bees.append(Bee(col, row, speed, perception, size))
                bee_hive = BeeHive(row, col)
                board.place_entity(bee, "B")
                
                
            # WASP HIVE VALIDATION
            elif object_data[0] == "W":
                n_entities = int(object_data[3])
                characteristics = stdio.readLine().split()
                if len(characteristics)!=1:
                    stdio.writeln(f"ERROR: Invalid object setup on line {line}")
                    return
                speed = int(characteristics[0])
                for i in range(n_entities):
                    wasp = Wasp(col, row, speed, size)
                    WaspHive.add_wasp(wasp)
                    # wasps.append(Wasp(row, col, speed))
                wasp_hive = WaspHive(row, col)
                board.place_entity(wasp, "W")
            
            # HONEYBEE HIVE VALIDATION
            elif object_data[0] == "H":
                n_entities = int(object_data[3])
                characteristics = stdio.readLine().split()
                if len(characteristics)!=2:
                    stdio.writeln(f"ERROR: Invalid object setup on line {line}")
                    return
                speed = int(characteristics[0])
                perception = int(characteristics[1])
                for i in range(n_entities):
                    hbee = HoneyBee(col, row, speed, perception, size)
                    DesertBeeHive.add_bee(hbee)
                    hbee_hive = DesertBeeHive(row, col)
                board.place_entity(hbee, "H")
            
            #DESERTBEE HIVE VALIDATION
            elif object_data[0]=="D":
                n_entities = int(object_data[3])
                characteristics = stdio.readLine().split()
                if len(characteristics)!=2:
                    stdio.writeln(f"ERROR: Invalid object setup on line {line}")
                    return
                speed = int(characteristics[0])
                perception = int(characteristics[1])
                for i in range(n_entities):
                    dbee = DesertBee(col, row, speed, perception, size)
                    DesertBeeHive.add_bee(dbee)
                dbee_hive = DesertBeeHive(row, col)
                board.place_entity(dbee_hive, "D")
        
        if (len(pollen_calc)==0) and (len(pollen_string)==0):
            pollen = "No pollen collected"
            
    except EOFError:
        stdio.writeln("ERROR: Invalid configuration line")
        return
    except ValueError:
        return
    except IndexError:
        return


def test_compass(row, col, speed, size):
    # Initialize the compass with the given row, column, and speed
    compass_0 = Compass(row, col, speed)

    # Get the next trajectory
    traj = compass_0.get_next_trajectory()

    # Calculate the new position based on the trajectory
    distance_0 = traj.get_distance()  # Get the distance the entity should move
    direction_0 = traj.get_direction_in_degrees()  # Get the direction of the entity

    new_row = row
    new_col = col

    if direction_0 == 0 or direction_0 == 360:
        new_col += distance_0
    elif direction_0 == 45:
        new_row += distance_0
        new_col += distance_0
    elif direction_0 == 90:
        new_row += distance_0
    elif direction_0 == 135:
        new_row += distance_0
        new_col -= distance_0
    elif direction_0 == 180:
        new_col -= distance_0
    elif direction_0 == 225:
        new_row -= distance_0
        new_col -= distance_0
    elif direction_0 == 270:
        new_row -= distance_0
    elif direction_0 == 315:
        new_row -= distance_0
        new_col += distance_0

    # Bound the movement within the map size
    if new_row < 0:
        new_row = 0
    elif new_row >= size:
        new_row = size - 1

    if new_col < 0:
        new_col = 0
    elif new_col >= size:
        new_col = size - 1

    # Return the new coordinates
    return new_row, new_col

def check_for_pollen(bee, flowers):
    for flower in flowers:
        if bee.position == flower.position:
            bee.has_flower = True
            # flowers.remove(flower)
            return True
    return False



def bee_movement(board, bees, bee_hive):
    
    board.board[bee_hive.row][bee_hive.col] = "B" #this is to display the BeeHive
    for bee in bees:
        if board.board[bee.row][bee.col] == "B":
            bee.move_bee()
        else:
            board.board[bee.row][bee.col] = "b"
            bee.move_bee()
    
def wasp_movement(board, wasps, wasp_hive):
    
    board.board[wasp_hive.row][wasp_hive.col] = "W" #this is to display the WaspHive
    for wasp in wasps:
        if board.board[wasp.row][wasp.col] == "W":
            wasp.move_wasp()
        else:
            board.board[wasp.row][wasp.col] = "w"
            wasp.move_wasp()

def dbee_movement(board, dbees, dbee_hive):
    
    board.board[dbee_hive.row][dbee_hive.col] = "D" #this is to display the WaspHive
    for dbee in dbees:
        if board.board[dbee.row][dbee.col] == "D":
            dbee.move_dbee()
        else:
            board.board[dbee.row][dbee.col] = "d"
            dbee.move_dbee()

def hbee_movement(board, hbees, hbee_hive):
    board.board[hbee_hive.row][hbee_hive.col] = "H" #this is to display the WaspHive
    for hbee in hbees:
        if board.board[hbee.row][hbee.col] == "h":
            hbee.move_wasp()
        else:
            board.board[hbee.row][hbee.col] = "d"
            hbee.move_wasp()

def game_loop():
    read_map()
    
    board.game_map(size, size)
    
    for i in range(iterations):
        board.board = stdarray.create2D(size, size, " ")
        try:
            
            bee_movement(board = board , bees = bees, bee_hive = bee_hive)
            wasp_movement(board = board, wasps = wasps, wasp_hive = wasp_hive)
            dbee_movement(board = board, dbees = dbees, dbee_hive = dbee_hive)
            hbee_movement(board = board, hbees = hbees, hbee_hive = hbee_hive)
            
            board.game_map(size, size)
        except NameError:
            pass
                
        board.game_map(size, size)


if __name__ == "__main__":
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
    