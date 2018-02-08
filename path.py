from roomclass import Room
from coordclass import Coord
from tileclass import Tile

class Path(object):
  def __init__(self, dun, start, end):
    self.dun = dun
    self.start = start
    self.end = end
    
