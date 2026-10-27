from pathlib import Path


def baca_data(path):
    """Membaca seluruh baris dari file data nilai."""
    lokasi = Path(path)

    with lokasi.open("r", encoding="utf-8") as file:
        return file.readlines()


def simpan_laporan(isi_laporan, path):
    """Menyimpan laporan ke file teks."""
    lokasi = Path(path)
    lokasi.parent.mkdir(parents=True, exist_ok=True)

    with lokasi.open("w", encoding="utf-8") as file:
        file.write(isi_laporan)
        file.write("\n")

    return lokasi