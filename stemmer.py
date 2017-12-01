import sys
import re
import timeit
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

factory = StemmerFactory()
stemmer = factory.create_stemmer()
stopword_set = set()

def store_stopword():
  print("Starting store stopword...")
  file = open("stopword_bahasa.txt", "r")
  for word in file.readlines():
    stopword_set.add(word.replace("\n", ""))
  print("Finished")
  
def cut_stopword(sentence):
  sentence = re.sub('[^a-zA-Z ]', ' ', sentence) # Clear special characters
  pattern = re.compile("^([a-zA-Z]+)+$")
  new_sentence = ""
  for word in sentence.split():
    word = word.lower()
    if not pattern.match(word):
      print("Tidak valid: " + word)
      break
    else:
      if word not in stopword_set:
        new_sentence += word
        new_sentence += " "
  return new_sentence

def main(filename):
  store_stopword()
  file_read = open(str(filename), "r")
  file_write = open("output.txt", "w")
  start = timeit.default_timer()
  print("Starting cutting and stemming...")
  for i,line in enumerate(file_read.readlines()):
    line = cut_stopword(line)
    line = stemmer.stem(line)
    print("Line Number: " + str(i+1) + "... Done")
    file_write.write(line + "\n")
  file_read.close()
  file_write.close()
  print("Finished.\nOutput file: output.txt")
  stop = timeit.default_timer()
  print("Running time: " + str(stop - start))

main(sys.argv[1])