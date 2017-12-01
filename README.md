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
- README.md
- requirements.txt #list package yang harus diinstall
- stemmer.py #source code
- stopword_bahasa.txt #list stopword bahasa indonesia

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
String1
String2
.
.
String-n
```
Contoh:
```
Microsoft Indonesia mengumumkan presiden direktur baru untuk Indonesia. Haris sendiri sudah 20 tahun berkecimpung di bisnis profesional.
Perusahaan pembesut sistem operasi Windows itu menunjuk Haris Izmee untuk menggantikan Andreas Diantoro yang telah lima tahun menahkodai Microsoft Indonesia.
Sebelumnya, dia bekerja di General Electric Healthcare (GEHC) Indonesia sebagai Country Manager dan Direktur.Sebelum GEHC, Haris sempat berkarier menjadi Senior Sales Director di GE Aviation.
Dalam masa jabatannya, Haris sukses memperluas usaha dalam bidang kesehatan, yang menjadi bidang usaha terbesar GE pada saat ini.
Pria lulusan Queen Mary University di London dengan gelar Sarjana Teknik Penerbangan ini bertanggung jawab memimpin seluruh penjualan mesin pesawat komersial dan memegang peranan penting dalam memenangkan beberapa proyek terbesar dalam sejarah GE Indonesia.
Semua pengalaman dan pengetahuan industri yang dimilikinya diharapkan dapat mendorong misi Microsoft di Indonesia.
```
Kemudian jalankan
```
python stemmer.py <nama file input>
```
Expected ouput
```
Starting store stopword...
Finished
Starting cutting and stemming...
Line Number: 1... Done
Line Number: 2... Done
Line Number: 3... Done
Line Number: 4... Done
Line Number: 5... Done
Line Number: 6... Done
Finished.
Output file: output.txt
Running time: 7.047039363586758
```




## Built With

* [Python](https://www.python.org/) - Programming Language
* [pySastrawi](https://github.com/har07/PySastrawi) - Stemmer Bahasa Library

## Authors

* **Kelompok IR(MA)** - Perolehan Informasi 2017/2018 Universitas Indonesia