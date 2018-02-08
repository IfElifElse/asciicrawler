from room import Room
from coord import Coord
from tile import Tile

class Path(object):
  def __init__(self, dun, start, end):
    self.dun = dun
    self.start = start
    self.end = end
