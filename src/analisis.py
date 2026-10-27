def hitung_statistik(data, kkm):
    """Menghitung statistik nilai dan ketuntasan kelas."""
    if not data:
        return None

    daftar_nilai = [siswa["nilai"] for siswa in data]

    jumlah_tuntas = sum(
        1 for nilai in daftar_nilai if nilai >= kkm
    )

    jumlah_belum_tuntas = len(data) - jumlah_tuntas

    return {
        "jumlah_siswa": len(data),
        "rata_rata": sum(daftar_nilai) / len(daftar_nilai),
        "minimum": min(daftar_nilai),
        "maksimum": max(daftar_nilai),
        "jumlah_tuntas": jumlah_tuntas,
        "jumlah_belum_tuntas": jumlah_belum_tuntas
    }