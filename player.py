import random
class Cube(object):
  def __init__(self, up=None):
    self.up = up

  def roll(self):
    sides = ['tank', 'deathray', 'deathray', 'human', 'cow', 'chicken']
    self.up = sides

  def __repr__(self):
    return str(self.up)

  def __str__(self):
    return self.up

  def __eq__(self, other):
    return self.up == other.up

class Player(object):
  def __init__(self,name):
    self.name = name
    self.score = 0

  def pick(self):
    choicedict = {'k': 'chicken', 'c': 'cow', 'h': 'human', 'd': 'deathray', 's': 'stop'}
    if not self.dice:
      return
    valid_choice = False
    while not valid_choice:
      selected = raw_input('Choice? k, c, d, h, s')
      if selected == 's':
        self.dice = []
        return
      elif selected not in choicedict.keys():
        print('Неверный выбор!')
      elif choicedict[selected] not in [str(x) for x in self.dice]:
        print('Нет %s для выбора' % choicedict[selected])
      elif selected in ['k', 'c', 'h']:

        if choicedict[selected] in [str(x) for x in self.saved]:
          print("Вы уже сохранили" % choicedict[selected])
        else:
          for index, d in enumerate(self.dice):
            if d.up == choicedict[selected]:
              self.saved.append(d)
          self.dice[:] = (value for value in self.dice if value.up != choicedict[selected])
          valid_choice = True
      elif selected == 'd':
        for index, d in enumerate(self.dice):
          if d.up == 'deathray':
            self.saved.append(d)
        self.dice[:] = (value for value in self.dice if value.up != 'deathray')
        valid_choice = True

  def take_turn(self):
    self.dice = [Cube() for x in range(0, 13)]
    self.tanks = []
    self.saved = []
    while self.dice:
      for d in self.dice:
        d.roll()
      for index, d in enumerate(self.dice):
        if d.up == 'tank':
          self.tanks.append(d)
      # Now remove all the tanks
      self.dice[:] = (value for value in self.dice if value.up != 'tank')
      print('Rolled: %s' % self.dice)
      print('Saved: %s' % self.saved)
      print('Tanks: %s' % self.tanks)
      self.pick()
    self.score_dice()

  def main():
    steve = Player('Steve')
    steve.take_turn()