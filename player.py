import random
class Cube(object):
  def __init__(self, up=None):
    self.up = up

  def roll(self):
    sides = ['tank', 'deathray', 'deathray', 'human', 'cow', 'chicken']
    self.up = random.choice(sides)

  def __repr__(self):
    return str(self.up)

  def __str__(self):
    return self.up

  def __eq__(self, other):
    return self.up == other.up
