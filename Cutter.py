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

  def cut(self, sentence, map_emoticon, map_senti):
    new_sentence = ""
    for word in sentence.split():
      # If it is emoticon
      if word in map_emoticon:
        new_sentence = new_sentence + word + " "
      # If it is a sentiment word
      elif word in map_senti:
        new_sentence = new_sentence + word + " " 
      else:
        # Only get alphabet, remove emoji
        if (word.isalpha()):
          if word not in self.mapCutter:
            new_sentence = new_sentence + word + " "
    return new_sentence


