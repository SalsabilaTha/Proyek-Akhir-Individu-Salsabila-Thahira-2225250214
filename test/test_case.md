# Test Case Analisis Nilai Kelas

## Tujuan Pengujian

Pengujian dilakukan untuk memastikan program dapat membaca data nilai, memvalidasi data, menghitung statistik kelas, menentukan ketuntasan siswa, dan menyimpan laporan dengan benar.

## Tabel Test Case

| ID | Kategori | Input/Kondisi | Hasil yang Diharapkan | Hasil Aktual | Status |
|---|---|---|---|---|---|
| TC01 | Normal | Nilai siswa 80, 70, 90 | Rata-rata 80, nilai minimum 70, nilai maksimum 90 | Belum diuji | Belum diuji |
| TC02 | Batas | Nilai siswa 0 | Nilai diterima sebagai nilai valid | Belum diuji | Belum diuji |
| TC03 | Batas | Nilai siswa 100 | Nilai diterima sebagai nilai valid | Belum diuji | Belum diuji |
| TC04 | Invalid | Nilai siswa 105 | Data ditolak dan baris dilewati | Belum diuji | Belum diuji |
| TC05 | Invalid | Nilai berisi huruf, misalnya `Ayu,abc` | Data ditolak dan baris dilewati | Belum diuji | Belum diuji |
| TC06 | Normal | Semua nilai siswa minimal 75 | Semua siswa dinyatakan tuntas | Belum diuji | Belum diuji |
| TC07 | Invalid | File `nilai_contoh.txt` tidak ditemukan | Program menampilkan pesan kesalahan dan berhenti dengan aman | Belum diuji | Belum diuji |
| TC08 | Normal | File berisi data nilai yang valid | Program menampilkan statistik dan menyimpan laporan ke `output/laporan_nilai.txt` | Belum diuji | Belum diuji |

## Kriteria Pengujian

1. **Lulus:** Hasil aktual sesuai dengan hasil yang diharapkan.
2. **Gagal:** Hasil aktual tidak sesuai dengan hasil yang diharapkan.
3. **Belum diuji:** Pengujian belum dilakukan sehingga hasilnya belum dapat dipastikan.

## Catatan

Test case dirancang sebelum implementasi penuh. Setelah program dijalankan, isi kolom hasil aktual dan ubah status sesuai hasil pengujian yang sebenarnya.
