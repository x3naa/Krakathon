class boat:
  def __init__(self):
    self.life = 100
    self.alive = True

  def damage_taken(self):
    if(self.life > 0):
      self.life -= 10
      print("Boat has: ", self.life, " left")
    else:
      print("Boat has sinked")
      self.alive = False