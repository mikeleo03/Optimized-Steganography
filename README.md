# Optimized Steganography using RSA and PRNG Algorithm
> Source code ini merupakan bentuk implementasi Pengembangan Algoritma RSA dan Pseudo-Random Prime-Number Generator dalam Optimalisasi Steganografi

## Daftar Isi
* [Abstrak](#abstrak)
* [Implementasi Program](#implementasi-program)
* [Sistematika File](#sistematika-file)
* [Cara Menjalankan Program](#cara-menjalankan-program)

## Abstrak
Sepanjang sejarah manusia, kriptografi telah digunakan untuk menutupi berbagai informasi dari badan atau
kelompok tertentu. Salah satu metode kriptografi yang banyak digunakan dalam hal pengiriman data dikenal dengan algoritma RSA. Algoritma yang telah digunakan puluhan tahun ini telah membuktikan betapa sulit dan kuatnya algoritma kriptografi ini. Selain dalam sebuah data, kriptografi dalam bentuk citra juga menjadi sebuah alternatif dewasa ini. Steganografi adalah ilmu dan seni menyembunyikan pesan rahasia (*hiding message*) sedemikian sehingga eksistensi sebuah pesan tidak terdeteksi oleh indera manusia.

Steganografi sudah kerap kali dikombinasikan dengan algoritma RSA, tetapi pada makalah ini akan dibahas
mengenai bagaimana melakukan optimalisasi pada steganografi menggunakan algoritma RSA yang disempurnakan dengan pembangkit bilangan prima acak semu (*Pseudo-Random Prime-Number Generator*) untuk menghasilkan pola yang lebih acak. Selain itu, metode ini diharapkan dapat menjadi optimalisasi yang baik dari metode LSB (*Least Significant Bit*) yang seringkali dijadikan basis melakukan steganografi.

## Implementasi Program
Program berhasil dibuat untuk melaksanakan beberapa fitur, salah satunya adalah sebagai perbandingan antara penggunaan steganografi biasa yang hanya memanfaatkan kriptografi sederhana, dengan steganografi yang dioptimalisasi dengan Pembangkit Bilangan Prima Acak Semu atau *Pseudo-Random Prime-Number Generator* dan algoritma kriptografi nir-simteri terkenal, RSA, untuk eksekusi kode yang lebih privat dengan pola yang lebih acak.

## Sistematika File
```bash
.
├─── doc
├─── img
│   ├─── nature_stegbasic.png
│   ├─── nature_stegoptim.png
│   └─── nature.png
├─── Decrypted.txt
├─── Encrypted.txt
├─── README.md
├─── SteganographyBasic.py
└─── SteganographyOptim.py
```

## Cara Menjalankan Program
### Prosedur Umum
1. Lakukan *clone repository* dengan command berikut
    ``` bash
    $ git clone https://github.com/mikeleo03/Optimized-Steganography.git
    ```
2. Anda dapat melakukan perbandingan hasil dari dua jenis steganografi yang telah dijelaskan sebelumnya, yaitu steganografi biasa yang terdapat pada `SteganographyBasic.py` dan steganografi yang telah dioptimalisasi pada `SteganographyOptim.py`. Anda bisa menjalankan `run` pada kedua file untuk melihat perbedaannya.
Referensi gambar dapat Anda lihat pada folder `img`.

### Steganografi Biasa
#### Enkripsi
1. Jalankan command `run` pada file.
2. Anda akan diminta *path* gambar yang akan disisipkan pesan. Masukkan *path* gambar tersebut dan program akan melakukan validasi apakah *path* yang dituliskan ada atau tidak.
3. Selanjutnya program akan meminta pesan yang akan dimasukkan ke dalam gambar. Tuliskan pesan yang ingin Anda sisipkan.
4. Program juga akan meminta *path* gambar yang telah disisipka akan disimpan. Setelah beberapa saat, maka gambar hasil enkripsi sudah dapat dilihat pada *path* penyimpanan gambar yang telah Anda tuliskan sebelumnya.

#### Dekripsi
1. Jalankan command `run` pada file.
2. Anda akan diminta *path* gambar yang akan didekripsi pesannya. Masukkan *path* gambar tersebut dan program akan melakukan validasi apakah *path* yang dituliskan ada atau tidak.
3. Selanjutnya program akan langsung melakukan proses dekripsi menggunakan algoritma steganografi. Tunggu beberapa saat, maka pesan hasil dekripsi sudah dapat Anda lihat pada terminal. Pesan yang telah didekripsi juga telah tertulis dan dapat Anda lihat melalui file `Decrypted.txt`.

### Steganografi Yang Telah Dioptimalisasi 
#### Enkripsi
1. Jalankan command `run` pada file.
2. Anda akan diminta *path* gambar yang akan disisipkan pesan. Masukkan *path* gambar tersebut dan program akan melakukan validasi apakah *path* yang dituliskan ada atau tidak.
3. Selanjutnya program akan meminta pesan yang akan dimasukkan ke dalam gambar. Tuliskan pesan yang ingin Anda sisipkan.
4. Program juga akan meminta *path* gambar yang telah disisipka akan disimpan. 
5. Setelah beberapa saat, maka gambar hasil enkripsi sudah dapat dilihat pada *path* penyimpanan gambar yang telah Anda tuliskan sebelumnya. Yang berbeda dari sebelumnya, Anda akan diberikan dua buah kunci, yaitu kunci publik dan kunci privat. Anda dapat menyebarkan kunci publik tersebut, tetapi Anda harus mengingat kunci privat untuk dapat membuka pesannya kembali. Pesan hasil enkripsi juga telah tertulis dan dapat Anda lihat melalui file `Encrypted.txt`.

#### Dekripsi
1. Jalankan command `run` pada file.
2. Anda akan diminta *path* gambar yang akan didekripsi pesannya. Masukkan *path* gambar tersebut dan program akan melakukan validasi apakah *path* yang dituliskan ada atau tidak.
3. Program juga akan meminta dua buah kunci yang teah dihasilkan dari proses enkripsi. Masukan kedua kunci tersebut untuk dapat menjalankan skema steganografi yang telah dioptimalisasi.
4. Setelah itu program akan langsung melakukan proses dekripsi menggunakan algoritma steganografi. Proses dekripsi dengan metode ini akan membutuhkan waktu yang relatif lebih lama untuk mencari pasangan bilangan prima yang memenuhi kondisi kunci publik dan kunci privat yang telah dibangkitkan sebelumnya (untuk lebih jelasnya dapat Anda baca pada [makalah berikut](doc/Implementasi%20Pengembangan%20Algoritma%20RSA%20dan%20Pseudo-Random%20Prime-Number%20Generator%20dalam%20Optimalisasi%20Steganografi%20-%20Michael%20Leon%20Putra%20Widhi%20-%2013521108.pdf).
5. Tunggu beberapa saat, maka pesan hasil dekripsi sudah dapat Anda lihat pada terminal. Pesan yang telah didekripsi juga telah tertulis dan dapat Anda lihat melalui file `Decrypted.txt`.