from random import randint

class kraken:

  def __init__(self):
    self.life = 100
    self.energie = 500
    self.alive = True
    self.actions = ["attack","sword","miss"]

  def do_action(self):
    if(self.energie > 0):
      self.energie -= 10
    else:
      print("Kraken left")

  def attacked_sword(self):    
    if (self.life > 0):
      self.life -= 10
      print("Kraken has: ", self.life, " lives left")
    else:
      print("Kraken died")
      self.alive = False

  def determine_action(self):
    value = randint(0, 2)
    return self.actions[value]


  

