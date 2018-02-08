from coordclass import Coord

equivalents = {
  "empty": " ",
  "wall": "x",
  "corr": "o",
}

class Tile(Coord):
  def __init__(self, x, y, within, content="empty"):
    self.content = content
    self.owner = within
    super(Tile, self).__init__(x, y)

  def __str__(self):
    return equivalents[self.content]
