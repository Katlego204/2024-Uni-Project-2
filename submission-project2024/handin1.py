from handin1api import * # command click will show you the contents of the library
import stdarray
from compass import *
import stdio
import sys
import math

def read_map():
    global pollen_outcome_s
    global pollen_outcome_f
    global map_info
    global flower_info
    global pollen_info
    global bee_hive_info
    global wasp_hive_info
    global desertBee_hive_info
    global honeyBee_hive_info
    
    pollen_outcome_f = []
    pollen_outcome_s = ""

    user_input = stdio.readLine().split()
    size = int(user_input[0])
    iterations = int(user_input[1])
    pollen_type = user_input[2]
    pollen_action = user_input[3]

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
        
    board = stdarray.create2D(size, size, "---")
    map_info = Map(size=size)
    
    x = None
    try:
        
        line = 1
        while not stdio.isEmpty():
            object = stdio.readLine().split()
            line += 1
            
            if len(object)!=4:
                stdio.writeln(f"ERROR: Invalid object setup on line {line}")
                return
                 
            if object[0] not in ["F", "B", "D", "H", "W"]:
                stdio.writeln(f"ERROR: Invalid object setup on line {line}")
                return
           
            
            #FLOWER VALIDATION
            if object[0]=="F":
                x_coord = int(object[1])
                y_coord = int(object[2])
                n_pollen = int(object[3])
                
                if x_coord not in range(0, size) or y_coord not in range(0, size):
                    stdio.writeln(f"ERROR: Invalid object setup on line {line}")
                    return
                
                if board[x_coord][y_coord]=="---":
                    board[x_coord][y_coord]=object[0]
                else:
                    stdio.writeln(f"ERROR: Cannot place flower at already occupied location ({x_coord}, {y_coord})")
                    return
                
                if n_pollen<0:
                    stdio.writeln(f"ERROR: Invalid object setup on line {line}")
                    return
                
                flower_info = Flower(row=x_coord ,col=y_coord, pollen_type=pollen_type)
                
                if pollen_type == "f":
                    if pollen_action == "sum":
                        for i in range(int(n_pollen)):
                            try:
                                x = float(stdio.readLine().split()[0])
                                line += 1
                            except ValueError:
                                stdio.writeln(f"ERROR: Invalid object setup on line {line+1}")
                            pollen_info = Pollen(x)
                            
                            flower_info.add_pollen(pollen_info)

                    if pollen_action == "min":
                        for i in range(int(n_pollen)):
                            try:
                                x = float(stdio.readLine().split()[0])
                                line += 1
                            except ValueError:
                                stdio.writeln(f"ERROR: Invalid object setup on line {line+1}")
                            pollen_info = Pollen(x)
                            flower_info.add_pollen(pollen_info)


                    if pollen_action == "max":
                        for i in range(int(n_pollen)):
                            try:
                                x = float(stdio.readLine().split()[0])
                                line += 1
                            except ValueError:
                                stdio.writeln(f"ERROR: Invalid object setup on line {line+1}")
                            pollen_info = Pollen(x)
                            flower_info.add_pollen(pollen_info)
                        
                if pollen_type == "s":
                    for j in range(int(n_pollen)):
                        try:
                            pollen_info = Pollen(stdio.readLine().split()[0])
                            line += 1
                        except ValueError:
                            stdio.writeln(f"ERROR: Invalid object setup on line {line+1}")
                        flower_info.add_pollen(pollen_info)
                    
                
                map_info.add_flower(flower_info)
                
                
            
            #BEE_HIVE VALIDATION
            if object[0]=="B":
                x_coord = int(object[1])
                y_coord = int(object[2])
                n_entities = int(object[3])

                if board[x_coord][y_coord]=="---":
                    board[x_coord][y_coord]=object[0]
                else:
                    stdio.writeln(f"ERROR: Cannot place hive at already occupied location ({x_coord}, {y_coord})")
                    return
                
                if x_coord not in range(0, size) or y_coord not in range(0, size):
                    stdio.writeln(f"ERROR: Invalid object setup on line {line}")
                    return

                charecteristics = stdio.readLine().split()
                line += 1
                if len(charecteristics)!=2:
                    stdio.writeln(f"ERROR: Invalid object setup on line {line}")
                    return
                speed = int(charecteristics[0])
                perception = int(charecteristics[1])

                bee_hive_info = BeeHive(row=x_coord, col=y_coord, num_bees=n_entities)
                #INSERTING VALUES
                for ii in range(n_entities):
                    bee_info = Bee(row=x_coord, col=y_coord, speed=speed, perception=perception)
                    bee_hive_info.add_bee(bee_info)
                    
                map_info.add_beehive(bee_hive_info)
                
                
            #DESERTBEE_HIVE VALIDATION
            if object[0]=="D":
                x_coord = int(object[1])
                y_coord = int(object[2])
                n_entities = int(object[3])
                
                if board[x_coord][y_coord]=="---":
                    board[x_coord][y_coord]=object[0]
                else:
                    stdio.writeln(f"ERROR: Cannot place hive at already occupied location ({x_coord}, {y_coord})")
                    return
                
                if x_coord not in range(0, size) or y_coord not in range(0, size):
                    stdio.writeln(f"ERROR: Invalid object setup on line {line}")
                    return
                    
                charecteristics = stdio.readLine().split()
                line += 1
                if len(charecteristics)!= 2:
                    stdio.writeln(f"ERROR: Invalid object setup on line {line}")
                    return
                speed = int(charecteristics[0])
                perception = int(charecteristics[1])
            
                #INSERTING VALUES
                desertBee_hive_info = DesertBeeHive(row=x_coord, col=y_coord, num_bees=n_entities)
                for iii in range(int(n_entities)):
                    desertBee_info = DesertBee(row=x_coord, col=y_coord, speed=speed, perception=perception)
                    desertBee_hive_info.add_bee(desertBee_info)
            
                map_info.add_desert_beehive(desertBee_hive_info)
                
                
            #WASP_HIVE VALIDATION
            if object[0]=="W":
                x_coord = int(object[1])
                y_coord = int(object[2])
                n_entities = int(object[3])
                
                if board[x_coord][y_coord]=="---":
                    board[x_coord][y_coord]=object[0]
                else:
                    stdio.writeln(f"ERROR: Cannot place hive at already occupied location ({x_coord}, {y_coord})")
                    return 
                
                if x_coord not in range(0, size) or y_coord not in range(0, size):
                    stdio.writeln(f"ERROR: Invalid object setup on line {line}")
                    return
                
                charecteristics = stdio.readLine().split()
                line += 1 
                if len(charecteristics)!=1:
                    stdio.writeln(f"ERROR: Invalid object setup on line {line}")
                    return
                speed = int(charecteristics[0])

                #INSERTING VALUES
                wasp_hive_info = WaspHive(row=x_coord, col=y_coord, num_wasps=n_entities)
                for iv in range(n_entities):
                    wasp_info = Wasp(row=x_coord, col=y_coord, speed=speed)
                    wasp_hive_info.add_wasp(wasp_info)
                    
                map_info.add_wasphive(wasp_hive_info)

            
            #HONEYBEE_HIVE VALIDATION
            if object[0]=="H":
                x_coord = int(object[1])
                y_coord = int(object[2])
                n_entities = int(object[3])
                
                if board[x_coord][y_coord]=="---":
                    board[x_coord][y_coord]=object[0]
                else:
                    stdio.writeln(f"ERROR: Cannot place hive at already occupied location ({x_coord}, {y_coord})")
                    return
                
                if x_coord not in range(0, size) or y_coord not in range(0, size):
                    stdio.writeln(f"ERROR: Invalid object setup on line {line-1}")
                    return
                    
                charecteristics = stdio.readLine().split()
                line += 1
                if len(charecteristics)!=2:
                    stdio.writeln(f"ERROR: Invalid object setup on line {line}")
                    return
                speed = int(charecteristics[0])
                
                #INSERTING VALUES
                honeyBee_hive_info = HoneyBeeHive(row=x_coord, col=y_coord, num_bees=n_entities)
                
                for v in range(n_entities):
                    honeyBee_info = HoneyBee(row=x_coord, col=y_coord, speed=speed, perception=perception)
                    honeyBee_hive_info.add_bee(honeyBee_info)
                    
                map_info.add_honey_beehive(honeyBee_hive_info)

 
    except EOFError:
        stdio.writeln("ERROR: Invalid configuration line")
        return
    except ValueError:
        #stdio.writeln(f"ERROR: Invalid configuration line {line+1}")
        return
    except IndexError:
        return
        #stdio.writeln("#")


    
    # '''create a compass for an entity using the given row, col and speed
    # print the current location of the entitiy in the form (row, column)
    # calculate and print the subsequent locations by moving according to the trajectories given by the compass
    # it must bound the entity to the size of the map
    # the number of moves to be calc and printed by the fourth argument in the fuction (num)'''

def test_compass(row, col, speed, size, n_moves):
    # Initialize the compass with the given row, column, and speed
    compass_0 = Compass(row, col, speed)

    # Print the initial position
    print(f"{row}, {col}")

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
        # Print the new position
        stdio.writeln(f"{row}, {col}")


        
if __name__ == "__main__":
    #read_map()
    test_compass(2, 3, 1, 10, 4)
    # git add .
    # git commit -m "message"
    # git push
    #read_map()
