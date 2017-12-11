import re

class Corrector:
  mapCorrection = {}

  def __init__(self, inputFile):
    file = open(inputFile, 'r')
    for sentence in file.readlines():
      sentence = sentence.strip()
      key = sentence.split(' = ')[0]
      value = sentence.split(' = ')[1]
      self.mapCorrection[key] = value

  def getCorrectValue(self, key):
    return self.mapCorrection[key]

  def getSize(self):
    return len(self.mapCorrection)

  def isExist(self, key):
    return key in self.mapCorrection

  def correct(self, sentence, map_emoticon):
    new_sentence = ""
    for word in sentence.split():
      # If it is emoticon
      if word in map_emoticon:
        new_sentence += word
      else:
        word = re.sub('[^a-zA-Z ]', '', word) # Clear special characters
        # Only get alphabet, remove emoji
        if (word.isalpha()):
          if word in self.mapCorrection:
            new_sentence = new_sentence + self.mapCorrection[word] + " "
          else:
            new_sentence = new_sentence + word + " "
    return new_sentence
