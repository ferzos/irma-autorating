import sys
import re
import timeit
from Corrector import Corrector
from Cutter import Cutter
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

map_emoticon = {}

def erase_question_sentence(review):
  new_review = ''
  for sentence in re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', review):
   if (len(re.findall(r'\?', sentence)) == 0): # Not question sentence
     new_review = new_review + sentence.strip() + " "
  return new_review

def generateEmotMap(file):
  new_map_emoticon = {}
  file_read = open(str(file), "r")
  for line in file_read.readlines():
    new_map_emoticon[line.split(" | ")[0].strip()] = line.split(" | ")[1].strip()
  return new_map_emoticon
  
def main(inputFile):
  print("Start making emoticon map")
  map_emoticon = generateEmotMap('emoticon_id.txt')
  print("Finished")
  
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
  
  file_read = open(str(inputFile), "r", encoding='utf-8')
  file_write = open("output.txt", "w", encoding='utf-8')
  start = timeit.default_timer()
  review_number = 0;
  for line in file_read.readlines():
    review_number += 1
    user_rating = line.split('<>')[0]
    review = line.split('<>')[1]
    review = erase_question_sentence(review) # Erase question sentence
    for sentence in re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', review):
      sentence = sentence.lower()
      sentence = corrector.correct(sentence, map_emoticon).strip()
      sentence = cutter.cut(sentence, map_emoticon).strip()
      if (sentence != ''):
        print(sentence)


    # line = line.lower()
    # line = re.sub('[^a-zA-Z ]', ' ', line) # Clear special characters
    # line = corrector.correct(line).strip()
    # line = cutter.cut(line).strip()
    # line = stemmer.stem(line)
    # if line:
    #   print("Line Number: " + str(i+1) + "... Done")
    #   file_write.write(line + "\n")
    # else:
    #   print("Line Number " + str(i+1) + ' was deleted')
  stop = timeit.default_timer()
  print("Running time: " + str(stop - start))
  print("Finished.\nOutput file: output.txt")
  file_read.close()
  file_write.close()
  
main(sys.argv[1])
