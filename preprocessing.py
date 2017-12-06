import sys
import re
import timeit
from Corrector import Corrector
from Cutter import Cutter
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

def main(inputFile):
  print("Start making abbreviation dictionary for bahasa")
  corrector = Corrector('singkatan.dic')
  print("Finished")

  print("Start making stopword dictionary for bahasa")
  cutter = Cutter('stopword.txt')
  print("Finished")

  print("Start making stemmer for bahasa")
  factory = StemmerFactory()
  stemmer = factory.create_stemmer()
  print("Finished")
  
  file_read = open(str(inputFile), "r")
  file_write = open("output.txt", "w")
  start = timeit.default_timer()
  for i,line in enumerate(file_read.readlines()):
    line = line.lower()
    line = re.sub('[^a-zA-Z ]', ' ', line) # Clear special characters
    line = corrector.correct(line).strip()
    line = cutter.cut(line).strip()
    line = stemmer.stem(line)
    if line:
      print("Line Number: " + str(i+1) + "... Done")
      file_write.write(line + "\n")
    else:
      print("Line Number " + str(i+1) + ' was deleted')
  stop = timeit.default_timer()
  print("Running time: " + str(stop - start))
  print("Finished.\nOutput file: output.txt")
  file_read.close()
  file_write.close()
  
main(sys.argv[1])
