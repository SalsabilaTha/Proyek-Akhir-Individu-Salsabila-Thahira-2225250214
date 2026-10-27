from pathlib import Path

from data_io import baca_data, simpan_laporan
from analisis import hitung_statistik
from utilitas import proses_baris, format_nilai, format_laporan


def main():
    folder_proyek = Path(__file__).resolve().parent.parent
    path_data = folder_proyek / "data" / "nilai_contoh.txt"
    path_laporan = folder_proyek / "output" / "laporan_nilai.txt"

    kkm = 75

    print("=" * 40)
    print("PROGRAM ANALISIS NILAI KELAS")
    print("=" * 40)

    try:
        baris_data = baca_data(path_data)
    except (FileNotFoundError, OSError) as error:
        print(f"Data gagal dibaca: {error}")
        return

    data_valid = []
    jumlah_data_tidak_valid = 0

    for nomor, baris in enumerate(baris_data, start=1):
        if not baris.strip():
            continue

        siswa = proses_baris(baris)

        if siswa is None:
            jumlah_data_tidak_valid += 1
            print(f"Baris {nomor} tidak valid dan dilewati.")
            continue

        data_valid.append(siswa)

    if not data_valid:
        print("Tidak ada data nilai yang valid.")
        return

    statistik = hitung_statistik(data_valid, kkm)

    print(f"\nJumlah siswa valid: {statistik['jumlah_siswa']}")
    print(f"KKM: {format_nilai(kkm)}")
    print(f"Rata-rata kelas: {format_nilai(statistik['rata_rata'])}")
    print(f"Nilai minimum: {format_nilai(statistik['minimum'])}")
    print(f"Nilai maksimum: {format_nilai(statistik['maksimum'])}")
    print(f"Jumlah siswa tuntas: {statistik['jumlah_tuntas']}")
    print(
        "Jumlah siswa belum tuntas: "
        f"{statistik['jumlah_belum_tuntas']}"
    )
    print(f"Jumlah baris tidak valid: {jumlah_data_tidak_valid}")

    isi_laporan = format_laporan(data_valid, statistik, kkm)

    try:
        simpan_laporan(isi_laporan, path_laporan)
    except OSError as error:
        print(f"Laporan gagal disimpan: {error}")
        return

    print(f"\nLaporan berhasil disimpan di: {path_laporan}")


if __name__ == "__main__":
    main()