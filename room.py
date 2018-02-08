import random
from coordclass import Coord

oppDirMap = {
  "u": "d",
  "d": "u",
  "l": "r",
  "r": "l"
}

class Room(object):
  def __init__(self, dungeon, upLeft, downRight):
    print("creating room at UL %s and DR %s" % (str(upLeft), str(downRight)))
    self.dun = dungeon
    self.u = upLeft.y
    self.d = downRight.y
    self.l = upLeft.x
    self.r = downRight.x
    self.UL = upLeft
    self.DR = downRight
    self.UR = Coord(self.u, self.r)
    self.DL = Coord(self.d, self.l)
    self.canvas = []
    for row in range(self.u-1, self.d):
      self.canvas.append([])
      for col in range(self.l-1, self.r):
        pos = Coord(col, row)
        self.canvas[-1].append(self.dun.grab(pos.dump()))
    for row in self.canvas:
      for tile in row:
        tile.content = "empty"
        tile.owner = self

  def randEdge(self, edge=random.choice(["u","d","l","r"])):
    print(edge)
    if edge in "u":
      return Coord(random.randint(self.l, self.r-1), self.u-2)
    if edge in "d":
      return Coord(random.randint(self.l, self.r-1), self.d)
    if edge in "l":
      return Coord(self.l-2, random.randint(self.u, self.d-1))
    if edge in "r":
      return Coord(self.r, random.randint(self.u, self.d-1))

  def makeConnection(self):
    values = lambda: 0 # creating an empty object w no attrs so i can cheat scopes
    values.u = {}
    values.d = {}
    values.l = {}
    values.r = {}
    for room in self.dun.rooms:
      if room == self:
        continue
      u = self.u - room.d
      d = -( self.d - room.u ) # must be flipped because higher y = lower disp (and vice versa)
      l = self.l - room.r
      r = -( self.r - room.l ) # ^^
      print( "u: %s, d: %s, l: %s, r: %s" % ( u, d, l, r ) )
      # if the distance is large enough, we can add the room to the list of proposals
      if   u > 0:
        values.u[ u ] = room # top wall
      elif d > 0:
        values.d[ d ] = room # bot wall
      elif l > 0:
        values.l[ l ] = room # left wall
      elif r > 0:
        values.r[ r ] = room # right wall

    choices = [ ] # actually select the closest room from each of the proposals
    if values.u.keys( ): choices.append( [ min( values.u.keys( ) ), "u" ] )
    if values.d.keys( ): choices.append( [ min( values.d.keys( ) ), "d" ] )
    if values.l.keys( ): choices.append( [ min( values.l.keys( ) ), "l" ] )
    if values.r.keys( ): choices.append( [ min( values.r.keys( ) ), "r" ] )

    val, direction = random.choice( choices ) # choose a random dir from the closest rooms
    print(val)
    print(direction)
    if direction == "u":
      conn = values.u[val]
    if direction == "d":
      conn = values.d[val]
    if direction == "r":
      conn = values.r[val]
    if direction == "l":
      conn = values.l[val]

    start = self.randEdge( direction )
    end = conn.randEdge( oppDirMap[ direction ] ) # created with the exec function
    print(start)
    print(end)
    diff = start.minus( end )

    # check = checkpoint to stop halfway through and fix lateral position
    if direction in "ud":
      check1 = Coord( start.x, end.y + int( diff.y / 2 ) )
      check2 = Coord( end.x, end.y + int( diff.y / 2 ) )
    if direction in "lr":
      check1 = Coord( end.x + int( diff.x / 2 ), start.y )
      check2 = Coord( end.x + int( diff.x / 2 ), end.y )
    # if point a was more than point b, do the thing backwards
    run1Y = range( start.y, check1.y + 1 )
    if not run1Y: run1Y = range( start.y, check1.y, -1 )
    run1X = range( start.x, check1.x + 1 )
    if not run1X: run1X = range( start.x, check1.x, -1 )
    run2Y = range( check1.y, check2.y + 1 )
    if not run2Y: run2Y = range( check1.y, check2.y, -1 )
    run2X = range( check1.x, check2.x + 1 )
    if not run2X: run2X = range( check1.x, check2.x, -1 )
    run3Y = range( check2.y, end.y + 1 )
    if not run3Y: run3Y = range( check2.y, end.y, -1 )
    run3X = range( check2.x, end.x + 1 )
    if not run3X: run3X = range( check2.x, end.x, -1 )
    # iterate over the things
    for y in run1Y:
      for x in run1X:
        tile = self.dun.grab(Coord(x, y))
        if tile.owner != self.dun:
          print("encountered room, stopping corr")
          return True
        tile.content = "empty"
    for y in run2Y:
      for x in run2X:
        tile = self.dun.grab(Coord(x, y))
        if tile.owner != self.dun:
          print("encountered room, stopping corr")
          return True
        tile.content = "empty"
    for y in run3Y:
      for x in run3X:
        tile = self.dun.grab(Coord(x, y))
        if tile.owner != self.dun:
          print("encountered room, stopping corr")
          return True
        tile.content = "empty"
    self.dun.grab(end).content = "empty"
    return True
