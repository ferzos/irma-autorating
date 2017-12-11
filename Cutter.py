import re

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

  def cut(self, sentence, map_emoticon):
    new_sentence = ""
    for word in sentence.split():
      # If it is emoticon
      if word in map_emoticon:
        new_sentence += word
      else:
        # Only get alphabet, remove emoji
        if (word.isalpha()):
          word = re.sub('[^a-zA-Z ]', ' ', word) # Clear special characters
          word = word.strip()
          if word in self.mapCutter:
            new_sentence = new_sentence + self.mapCutter[word] + " "
          else:
            new_sentence = new_sentence + word + " "
    return new_sentence


