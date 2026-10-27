# Proposal Proyek Analisis Nilai Kelas

# Identitas Mahasiswa
- Nama : Salsabila Thahira
- NIM : 2225250214
- Kelas : 3B

## 1. Judul Proyek

**Program Rekap dan Analisis Nilai Matematika Kelas**

## 2. Latar Belakang

Dalam proses pembelajaran matematika, guru perlu mengolah nilai siswa untuk mengetahui hasil belajar dan tingkat ketuntasan kelas. Pengolahan nilai secara manual dapat membutuhkan waktu lebih lama, terutama ketika jumlah siswa cukup banyak. Selain itu, perhitungan yang dilakukan secara berulang berisiko menimbulkan kesalahan.

Berdasarkan permasalahan tersebut, dibuat proyek Analisis Nilai Kelas menggunakan bahasa pemrograman Python. Program ini dirancang untuk membaca data nilai dari file teks, memvalidasi data, menghitung statistik nilai, menentukan ketuntasan siswa berdasarkan KKM, dan menyimpan hasilnya ke dalam laporan. Dengan adanya program ini, proses rekap nilai diharapkan menjadi lebih mudah, cepat, dan konsisten.

## 3. Pengguna dan Tujuan

**Pengguna utama:** Guru matematika.

**Tujuan proyek:**

1. Membantu guru mengolah data nilai siswa secara otomatis.
2. Menghitung rata-rata, nilai minimum, dan nilai maksimum kelas.
3. Mengetahui jumlah siswa yang tuntas dan belum tuntas berdasarkan KKM.
4. Memeriksa validitas data nilai sebelum dianalisis.
5. Menghasilkan laporan analisis nilai yang dapat dibaca kembali.

**User Story:**

Sebagai guru matematika, saya ingin membaca dan mengolah data nilai siswa melalui program Python agar saya dapat mengetahui statistik kelas dan status ketuntasan siswa dengan lebih mudah.

## 4. Ruang Lingkup

### Fitur wajib

1. Membaca data nama dan nilai siswa dari file teks.
2. Memvalidasi format data dan memastikan nilai berada pada rentang 0–100.
3. Menghitung rata-rata, nilai minimum, dan nilai maksimum kelas.
4. Menentukan status tuntas atau belum tuntas berdasarkan KKM.
5. Menampilkan hasil analisis dan menyimpan laporan ke file teks.

### Batasan proyek

- Program menggunakan bahasa Python.
- Program dijalankan melalui terminal atau console di VS Code.
- Data dibaca dari file teks `data/nilai_contoh.txt`.
- Format data adalah `nama,nilai`, dengan satu siswa pada setiap baris.
- Nilai yang diterima berada pada rentang 0–100.
- KKM awal ditetapkan sebesar 75.
- Program tidak menggunakan database, antarmuka grafis, atau layanan eksternal.
- Data yang digunakan merupakan data contoh, bukan data pribadi siswa yang sebenarnya.

## 5. Kebutuhan

### 5.1 Kebutuhan Fungsional

| ID | Kebutuhan | Prioritas |
|---|---|---|
| F01 | Program dapat membaca data nilai dari file teks. | Wajib |
| F02 | Program dapat memvalidasi format data dan nilai 0–100. | Wajib |
| F03 | Program dapat menghitung rata-rata, minimum, dan maksimum. | Wajib |
| F04 | Program dapat menentukan status ketuntasan berdasarkan KKM. | Wajib |
| F05 | Program dapat menampilkan dan menyimpan laporan analisis. | Wajib |

### 5.2 Kebutuhan Nonfungsional

1. Program mudah dijalankan melalui terminal VS Code.
2. Nama fungsi dan variabel mudah dipahami.
3. Pesan kesalahan ditampilkan dengan jelas.
4. Program dapat diuji ulang menggunakan data yang sama.
5. Data contoh tidak mengandung informasi pribadi nyata.

## 6. IPO (Input, Proses, Output)

| Komponen | Keterangan |
|---|---|
| Input | File `data/nilai_contoh.txt` yang berisi nama dan nilai siswa, serta KKM sebesar 75. |
| Proses | Membaca file, memvalidasi format dan nilai, menyimpan data valid, menghitung statistik, menentukan ketuntasan, serta menyusun laporan. |
| Output | Daftar nilai valid, rata-rata, nilai minimum, nilai maksimum, jumlah siswa tuntas dan belum tuntas, serta laporan teks. |

## 7. Algoritma

### Pseudocode

```text
MULAI

    Tentukan lokasi file data
    Tentukan nilai KKM = 75

    Baca data dari file

    Jika file tidak ditemukan:
        Tampilkan pesan kesalahan
        SELESAI

    Siapkan daftar data siswa yang valid

    Untuk setiap baris data:
        Periksa format baris
        Periksa apakah nilai berupa angka

        Jika format dan nilai valid:
            Simpan data siswa
        Jika tidak:
            Tampilkan pesan bahwa data tidak valid
            Lewati baris tersebut

    Jika tidak ada data valid:
        Tampilkan pesan bahwa data tidak tersedia
        SELESAI

    Hitung rata-rata nilai
    Tentukan nilai minimum dan maksimum

    Untuk setiap siswa:
        Jika nilai >= KKM:
            Tentukan status Tuntas
        Jika tidak:
            Tentukan status Belum Tuntas

    Hitung jumlah siswa tuntas
    Hitung jumlah siswa belum tuntas

    Tampilkan ringkasan hasil analisis
    Susun laporan
    Simpan laporan ke folder output

SELESAI
```

### Alur Program

Data nilai → Membaca file → Validasi data → Menghitung statistik → Menentukan ketuntasan → Menampilkan hasil → Menyimpan laporan.

## 8. Struktur Program

| File/Modul | Tanggung Jawab |
|---|---|
| `src/main.py` | Mengatur alur utama program dan menghubungkan seluruh modul. |
| `src/data_io.py` | Membaca file data nilai dan menyimpan laporan. |
| `src/analisis.py` | Menghitung statistik nilai dan jumlah ketuntasan siswa. |
| `src/utilitas.py` | Memvalidasi nilai, memproses baris data, dan menyusun teks laporan. |
| `data/nilai_contoh.txt` | Menyimpan data contoh nama dan nilai siswa. |
| `tests/test_case.md` | Mendokumentasikan skenario dan hasil pengujian. |
| `output/` | Menyimpan laporan hasil analisis. |

Modularisasi dilakukan agar bagian pembacaan data, perhitungan, dan pengolahan teks memiliki tanggung jawab yang berbeda. Pembagian ini memudahkan pengujian, debugging, dan pengembangan program.

## 9. Struktur Data

### 9.1 List

List digunakan untuk menyimpan kumpulan data siswa yang valid agar dapat dihitung dan diproses secara berulang.

### 9.2 Dictionary

Dictionary digunakan untuk menyimpan informasi setiap siswa berdasarkan pasangan key-value, seperti nama, nilai, dan status ketuntasan.

Contoh:

```python
{
    "nama": "Ayu",
    "nilai": 85,
    "status": "Tuntas"
}
```

### 9.3 String

String digunakan untuk menyimpan nama siswa, membaca isi baris file, dan menyusun teks laporan.

### 9.4 File Teks

File teks digunakan sebagai sumber data nilai siswa dan tempat menyimpan laporan hasil analisis.

## 10. Test Case

Pengujian awal mencakup kondisi normal, batas, dan invalid untuk memastikan fitur utama dapat bekerja sesuai rancangan.

| ID | Kategori | Input/Kondisi | Hasil yang Diharapkan |
|---|---|---|---|
| TC01 | Normal | Nilai 80, 70, 90 | Rata-rata 80, minimum 70, maksimum 90. |
| TC02 | Batas | Nilai 0 | Nilai diterima sebagai nilai valid. |
| TC03 | Batas | Nilai 100 | Nilai diterima sebagai nilai valid. |
| TC04 | Invalid | Nilai 105 | Data ditolak dan dilewati. |
| TC05 | Invalid | Nilai berupa huruf | Data ditolak dan dilewati. |
| TC06 | Normal | Semua nilai minimal 75 | Semua siswa dinyatakan tuntas. |
| TC07 | Invalid | File data tidak ditemukan | Program menampilkan pesan kesalahan. |
| TC08 | Normal | File berisi data valid | Statistik ditampilkan dan laporan disimpan. |

Rincian pengujian terdapat pada file `tests/test_case.md`. Kolom hasil aktual dan status diisi setelah program benar-benar dijalankan.

## 11. Pembagian Tugas

Pembagian tugas berikut merupakan rancangan awal dan dapat disesuaikan dengan jumlah anggota kelompok.

| Peran | Nama/PIC | Tanggung Jawab |
|---|---|---|
| Koordinator | ... | Mengatur ruang lingkup, pembagian tugas, dan integrasi proyek. |
| Programmer Data I/O | ... | Membuat dan memeriksa fungsi pembacaan data serta penyimpanan laporan. |
| Programmer Logika | ... | Membuat perhitungan statistik dan ketuntasan siswa. |
| Tester/QA | ... | Menjalankan test case dan memeriksa hasil program. |
| Dokumentasi | ... | Menyusun README, proposal, dan dokumentasi pengujian. |

Jika jumlah anggota kelompok terbatas, satu anggota dapat memegang lebih dari satu peran. Setiap anggota tetap harus memahami alur program secara keseluruhan.

## 12. Jadwal

| Tahap | Target Pekerjaan |
|---|---|
| Pertemuan 14 | Menentukan masalah, menyusun proposal, merancang algoritma, membuat struktur folder, dan menyusun test case. |
| Antara Pertemuan 14–15 | Mengimplementasikan fungsi pembacaan data, analisis statistik, validasi, dan laporan. |
| Pertemuan 15 | Mengintegrasikan program, menjalankan pengujian, melakukan debugging, dan memperbaiki dokumentasi. |
| Pertemuan 16 | Mempresentasikan dan mendemonstrasikan hasil proyek serta melakukan evaluasi. |

## 13. Repository

**Nama repository:** `Proyek-Akhir-Individu-Salsabila-Thahira-2225250214`

**URL GitHub:** https://github.com/SalsabilaTha/Proyek-Akhir-Individu-Salsabila-Thahira-2225250214.git

Repository digunakan untuk menyimpan kode program, data contoh, proposal, README, dan test case. Perubahan proyek dicatat melalui commit bertahap dengan pesan yang menjelaskan pekerjaan yang dilakukan.

Contoh commit rancangan:

```bash
git add README.md proposal.md tests/
git commit -m "docs: menambahkan proposal dan test case proyek"
git push
```

## Referensi

1. Bahan Ajar Algoritma dan Pemrograman, Pertemuan 14, *Perancangan Proyek Program Sederhana: Masalah Matematika/Pembelajaran Matematika, VS Code, dan GitHub*. Program Studi S1 Pendidikan Matematika FKIP Untirta, Tahun Ajaran 2026/2027 Ganjil.
2. Python Software Foundation. Dokumentasi resmi Python.
