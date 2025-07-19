from compass import *
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