from boat import boat
from kraken import kraken

kraken = kraken()
boat = boat()

def play():
  action = kraken.determine_action()
  kraken.do_action()
  if(action == "attack"):
    print("Kraken attacked boat")
    boat.damage_taken()
  elif(action == "sword"):
    print("Kraken attacked sword")
    kraken.attacked_sword()
  elif(action == "miss"):
    print("Kraken missed")

if __name__ == '__main__':
  while(boat.life > 0 and kraken.life > 0 and kraken.energie > 0):
    play()

