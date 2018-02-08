import random
from room import Room
from coord import Coord
from tile import Tile

class Dungeon(object):
  def __init__(self):
    self.canvas = []
    self.width = 30
    self.height = 30
    for y in range(self.height):
      self.canvas.append([])
      for x in range(self.width):
        self.canvas[y].append(Tile(x, y, self, "wall"))
    self.rooms = []
    roomCount = random.randint(3, 6)
    timeout = 200
    while roomCount > 0:
      success = self.addRoom()
      if success: # if the room was successfully created (no overlaps)
        roomCount -= 1
      timeout -= 1
      if timeout <= 0:
        break
    for room in self.rooms:
        room.makeConnection()

  def addRoom(self):
    u = random.randint(2, self.height-7)
    l = random.randint(2, self.width-7)
    upLeft = Coord(u, l)
    d = random.randint(u+4, u+7)
    r = random.randint(l+4, l+7)
    downRight = Coord(d, r)
    try:
      for row in range(u-3, d+2): # add 2 to u and 1 to d for room borders
        for col in range(l-3, r+2): # same as above
          pos = Coord(row, col) # used to grab tile
          tile = self.grab(pos) # used to see the tile's owner
          if tile.owner != self: # if the tile has not already been claimed by a room
            print("overlap occurred at %s, %s" % (col, row))
            return False
    except IndexError:
      print("too close to wall")
      return False
    newRoom = Room(self, upLeft, downRight)
    self.rooms.append(newRoom)
    return True # signifies successful creation

  def grab(self, coord):
    return self.canvas[coord.y][coord.x]

  def asciiDisplay(self):
    display = []
    for row in self.canvas:
      for tile in row:
        display.append(str(tile))
      display.append("\n")
    print("".join(display))
