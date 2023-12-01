
#Centroid klass för K-means algoritm.
class Centroid:

  #Initierar en instans.
  def __init__(self):
    self.assigned = []
    self.word_count = {}

  #Sätter centroidens position.
  def set_word_count(self, i, värde):
    self.word_count[i] = {"count" : värde}

  #Lägger till en blogg i assigned.
  def assign(self, blogg) : 
    self.assigned.append(blogg)

  #Tar bort noder från assigned
  #så att det inte blir dubletter.
  def clearAssigned(self) :
    self.assigned.clear()
