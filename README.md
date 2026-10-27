# Analisis Nilai Kelas

# Identitas Mahasiswa
- Nama : Salsabila Thahira
- NIM : 2225250214
- Kelas : 3B

## Deskripsi

Analisis Nilai Kelas adalah program sederhana berbasis Python yang digunakan untuk membantu guru mengolah dan menganalisis nilai siswa. Program ini dapat membaca data nilai dari file teks, memeriksa validitas nilai, menghitung statistik kelas, menentukan status ketuntasan siswa berdasarkan KKM, serta menyimpan hasil analisis ke dalam laporan.

## Struktur data

- **List:** Menyimpan kumpulan data siswa yang valid.
- **Dictionary:** Menyimpan informasi setiap siswa, seperti nama, nilai, dan status ketuntasan.
- **String:** Menyimpan nama siswa dan isi laporan.
- **File teks:** Digunakan untuk membaca data nilai dan menyimpan laporan hasil analisis.

## Fitur

1. Membaca data nama dan nilai siswa dari file teks.
2. Memvalidasi nilai agar berada pada rentang 0–100.
3. Menghitung rata-rata, nilai minimum, dan nilai maksimum kelas.
4. Menentukan jumlah siswa yang tuntas dan belum tuntas berdasarkan KKM.
5. Menampilkan ringkasan hasil analisis di terminal.
6. Menyimpan laporan hasil analisis ke dalam file teks.

## Cara Menjalankan

Jalankan perintah berikut melalui terminal VS Code dari folder utama proyek:

```bash
python src/main.py
```

Jika menggunakan perintah `python3`, jalankan:

```bash
python3 src/main.py
```

## KKM

KKM awal ditetapkan sebesar 75. Siswa dinyatakan **tuntas** jika nilainya lebih besar dari atau sama dengan KKM. Siswa dinyatakan **belum tuntas** jika nilainya kurang dari KKM.

## Output

Program menampilkan jumlah siswa valid, rata-rata kelas, nilai minimum, nilai maksimum, jumlah siswa tuntas, jumlah siswa belum tuntas, dan jumlah baris yang tidak valid.

Laporan hasil analisis disimpan pada file `output/laporan_nilai.txt`.
