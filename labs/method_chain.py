class Satellite:
  def __init__(self):
    self.orbits = 0

  def orbit(self):
    self.orbits += 1
    print("Bleep bloop... I have orbited the earth {} times.".format(self.orbits))
    return self

sputnik = Satellite()
sputnik.orbit().orbit().orbit() # Make this work!
