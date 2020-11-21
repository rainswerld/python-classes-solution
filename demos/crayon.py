"""Defines crayon class"""

class Crayon():
  def __init__(self, color, length):
    self.color = color
    self.length = length
    self.form = 'solid'

  def draw(self):
    if self.length > 0:
      self.length -= 1
    else:
      print('This crayon is all used up!')

  def melt(self):
    if (self.form == 'solid'):
      self.length = 0
      self.form = 'liquid'
    else:
      print('This crayon is already melted!')

blue_crayon = Crayon('blue', 5)
yellow_crayon = Crayon('yellow', 5)
print(blue_crayon)
print(yellow_crayon)
