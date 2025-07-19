import stdio, stdarray

class Map:
    def __init__(self, size: int):
        self.size = size
        self.board = stdarray.create2D(size, size, " ")

    def place_entity(self, entity, entity_type: str):
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