
#Centroid klass för K-means algoritm.
class Centroid:

  #Initierar en instans.
  def __init__(self):
    self.assigned = []
    self.old = []
    self.word_count = {}

  #Initiera centroidens position.
  def set_word_count(self, i, värde):
    self.word_count[i] = {"count" : värde}

  #Lägger till en blogg i assigned.
  def assign(self, blogg) : 
    self.assigned.append(blogg)

  #Lägger nodes från assigned till old,
  #för att kunna assigna nya och sen jämföra.
  def clearAssigned(self) :
    self.old = self.assigned
    self.assigned.clear()
  
  def getAssigned(self):
    return self.assigned