import sys
import re
import timeit
from Corrector import Corrector
from Cutter import Cutter
from Stemmer import Stemmer

map_emoticon = {}
map_senti = set([])

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

def generateSentiMap(array_file):
  new_map_senti = set([])
  for file in array_file:
    file_read = open(str(file), 'r')
    if (file == 'negatingword.txt'):
      for line in file_read.readlines():
        new_map_senti.add(line.strip())
    else:
      for line in file_read.readlines():
        new_map_senti.add(line.split(':')[0].strip())
  return new_map_senti
  
def main(inputFile):
  print("Start making emoticon map")
  map_emoticon = generateEmotMap('emoticon_id.txt')
  print("Finished")

  print("Start making senti map")
  map_senti = generateSentiMap(['boosterwords_id.txt', 'idioms_id.txt', 'negatingword.txt', 'sentiwords_id.txt'])
  print("Finished")
  
  print("Start making abbreviation dictionary for bahasa")
  corrector = Corrector('singkatan.dic')
  print("Finished")

  print("Start making stopword dictionary for bahasa")
  cutter = Cutter('stopword.txt')
  print("Finished")

  print("Start making stemmer for bahasa")
  stemmer = Stemmer()
  print("Finished")
  
  output_file = sys.argv[2] + '.txt'
  file_read = open(str(inputFile), "r", encoding='utf-8')
  file_write = open(output_file, "w", encoding='utf-8')
  start = timeit.default_timer()
  review_number = 0;
  for line in file_read.readlines():
    review_number += 1
    user_rating = line.split('<>')[0]
    file_write.write('REVIEW-' + str(review_number) + ' [rating] ' + str(user_rating) + '\n')
    review = line.split('<>')[1]
    review = erase_question_sentence(review) # Erase question sentence
    for i, sentence in enumerate(re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', review)):
      print("Processing sentence " + str(i+1) + ' from review ' + str(review_number))
      sentence = sentence.lower()
      sentence = corrector.correct(sentence, map_emoticon, map_senti).strip()
      sentence = cutter.cut(sentence, map_emoticon, map_senti).strip()
      sentence = stemmer.stem(sentence, map_emoticon, map_senti).strip()
      if (sentence != ''):
        file_write.write(sentence + "\n")
  stop = timeit.default_timer()
  print("Running time: " + str(stop - start))
  print("Finished.\nOutput file: " + output_file)
  file_read.close()
  file_write.close()
  
main(sys.argv[1])
