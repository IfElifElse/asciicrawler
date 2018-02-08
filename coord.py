class Coord(object):
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __str__(self):
    return "(%s, %s)" % (self.x, self.y)

  def plus(self, coord): # addition
    if type(coord) == type(()):
      coord = Coord(coord[0], coord[1])
    return Coord( self.x+coord.x, self.y+coord.y )

  def minus(self, coord): # subtraction
    if type(coord) == type(()):
      coord = Coord(coord[0], coord[1])
    return Coord( self.x-coord.x, self.y-coord.y )

  def times(self, magnitude): # multiplication
    return Coord( self.x*magnitude, self.y*magnitude )

  def over(self, magnitude): # division
    return Coord( self.x/magnitude, self.y/magnitude )

  def asTuple(self):
    return (self.x, self.y)

  def adjacent(self): # returns 4 adjacent coordinates
    return [Coord(self.x+1, self.y), Coord(self.x-1, self.y), Coord(self.x, self.y+1), Coord(self.x, self.y-1)]

  def distance(self, coord): #returns how many moves would need to be made to get to the target coord
    return abs(self.x, coord.x) + abs(self.y, coord.y)

  def dump(self):
    return Coord(self.x, self.y)
