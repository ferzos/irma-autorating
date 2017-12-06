class Cutter:
  mapCutter = []

  def __init__(self, inputFile):
    file = open(inputFile, 'r')
    for word in file.readlines():
      self.mapCutter.append(word.strip())
    
  def getSize(self):
    return len(self.mapCutter)

  def isExist(self, key):
    return key in self.mapCutter

  def cut(self, sentence):
    new_sentence = ""
    for word in sentence.split():
      if word not in self.mapCutter:
        new_sentence = new_sentence + word + " "
    return new_sentence


