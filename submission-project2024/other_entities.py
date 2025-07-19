
class Entity:
    def __init__(self, x_coord: int, y_coord: int):
        self.x_coord = x_coord
        self.y_coord = y_coord
        
class Hive(Entity):
    def __init__(self, x_coord: int, y_coord: int, n_entities: int, speed: int):
        super().__init__(x_coord, y_coord)
        self.n_entities = n_entities
        self.speed = speed
        
class  DesertBee(Hive):
    def __init__(self, x_coord: int, y_coord: int, n_entities: int, speed: int, perception: int):
        super().__init__(x_coord, y_coord, n_entities, speed)
        self.perception = perception

class HoneyBee(Hive):
    def __init__(self, x_coord: int, y_coord: int, n_entities: int, speed: int, perception: int):
        super().__init__(x_coord, y_coord, n_entities, speed)
        self.perception = perception
        

        
        