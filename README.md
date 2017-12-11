# IR(MA) Preprocessing Sentence Bahasa

Preprocessing kalimat pada bahasa indonesia dengan menggunakan library python Sastrawi

### Prerequisites
```
python
- pip
- virtualenv
```
### Project Structure
```
- .gitigore
- Corrector.py # objek class yang melakukan spelling correction
- Cutter.py # objek class yang melakukan pemotongan stopword
- emoticon_id  # daftar emoticon untuk sentiment analysis
- Preprocessing.py # Main program yang melakukan preprocessing pada file input
- README.md
- requirements.txt # list package yang harus diinstall
- singkatan.dict # daftar singkatan bahasa indonesia
- Stemmer.py # objek class yang melakukan stemming
- stopword_bahasa.txt # daftar stopword bahasa indonesia

```

### Installing
##### Membuat dan mengaktifkan virtual environment
```
Linux:
$ virtualenv venv
New python executable in venv/bin/python
Installing setuptools, pip............done.
$ . venv/bin/activate

Windows:
> virtualenv venv
New python executable in venv/bin/python
Installing setuptools, pip............done.
> venv\Scripts\activate
```

Jika berhasil, akan muncul tampilan seperti ini di command line

```
(venv) E:\...
```

Menonaktifkan venv dengan cara
```
deactivate
```
####
##### Instalasi package Sastrawi 
```
pip install -r requirements.txt
```

## Running the program
Siapkan sebuah file yang berisi input dengan format seperti berikut:
```
rating1<>review1
rating1<>review1
rating1<>review1
.
.
ratingN<>reviewN
```
Contoh:
```
1.0<>Memantapkan tnpa yang nih mon :)
```
Kemudian jalankan
```
python Preprocessing.py <nama file input>
```
Expected ouput
```
Start making emoticon map
Finished
Start making abbreviation dictionary for bahasa
Finished
Start making stopword dictionary for bahasa
Finished
Start making stemmer for bahasa
Finished
Processing sentence 1 from review 1
Processing sentence 2 from review 1
Processing sentence 3 from review 1
Processing sentence 4 from review 1
Processing sentence 5 from review 1
Processing sentence 6 from review 1
Processing sentence 7 from review 1
Processing sentence 8 from review 1
Processing sentence 9 from review 1
Processing sentence 10 from review 1
Processing sentence 11 from review 1
Processing sentence 12 from review 1
Processing sentence 13 from review 1
Processing sentence 14 from review 1
Processing sentence 15 from review 1
Processing sentence 16 from review 1
Processing sentence 17 from review 1
Processing sentence 18 from review 1
Processing sentence 19 from review 1
Processing sentence 20 from review 1
Processing sentence 21 from review 1
Processing sentence 22 from review 1
Processing sentence 23 from review 1
Processing sentence 24 from review 1
Processing sentence 25 from review 1
Processing sentence 26 from review 1
Processing sentence 27 from review 1
Processing sentence 28 from review 1
Processing sentence 29 from review 1
Processing sentence 30 from review 1
Processing sentence 31 from review 1
Processing sentence 32 from review 1
Processing sentence 33 from review 1
Processing sentence 34 from review 1
Processing sentence 35 from review 1
Processing sentence 1 from review 2
Running time: 12.314342716031362
Finished.
Output file: output.txt
```
Terdapat file bernama *ouput.txt* yang merupakan hasil dari preprocessing
## Built With

* [Python](https://www.python.org/) - Programming Language
* [pySastrawi](https://github.com/har07/PySastrawi) - Stemmer Bahasa Library

## Authors

* **Kelompok IR(MA)** - Perolehan Informasi 2017/2018 Universitas Indonesia