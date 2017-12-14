import re
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

class Stemmer:
  factory = None
  stemmer = None

  def __init__(self):
    self.factory = StemmerFactory()
    self.stemmer = self.factory.create_stemmer()

  def stem(self, sentence, map_emoticon, map_senti):
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
          new_sentence = new_sentence + self.stemmer.stem(word) + " "
    return new_sentence