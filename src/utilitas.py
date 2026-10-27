def validasi_nilai(nilai):
    """Memeriksa apakah nilai berada pada rentang 0 sampai 100."""
    return 0 <= nilai <= 100


def proses_baris(baris):
    """Mengubah satu baris teks menjadi data siswa yang valid."""
    bagian = baris.strip().split(",")

    if len(bagian) != 2:
        return None

    nama = bagian[0].strip()
    teks_nilai = bagian[1].strip()

    if not nama or not teks_nilai:
        return None

    try:
        nilai = float(teks_nilai)
    except ValueError:
        return None

    if not validasi_nilai(nilai):
        return None

    return {
        "nama": nama,
        "nilai": nilai
    }


def format_nilai(nilai):
    """Menampilkan nilai tanpa angka desimal jika bilangan bulat."""
    if nilai.is_integer():
        return str(int(nilai))

    return f"{nilai:.2f}"


def format_laporan(data, statistik, kkm):
    """Menyusun laporan analisis nilai dalam bentuk teks."""
    baris = [
        "LAPORAN ANALISIS NILAI KELAS",
        "=" * 35,
        f"Jumlah siswa valid: {len(data)}",
        f"KKM: {format_nilai(kkm)}",
        "",
        "DAFTAR NILAI SISWA",
        "-" * 35
    ]

    for siswa in data:
        status = (
            "Tuntas"
            if siswa["nilai"] >= kkm
            else "Belum Tuntas"
        )

        baris.append(
            f'{siswa["nama"]}: '
            f'{format_nilai(siswa["nilai"])} - {status}'
        )

    baris.extend([
        "",
        "STATISTIK KELAS",
        "-" * 35,
        f'Rata-rata: {format_nilai(statistik["rata_rata"])}',
        f'Nilai minimum: {format_nilai(statistik["minimum"])}',
        f'Nilai maksimum: {format_nilai(statistik["maksimum"])}',
        f'Jumlah tuntas: {statistik["jumlah_tuntas"]}',
        f'Jumlah belum tuntas: {statistik["jumlah_belum_tuntas"]}'
    ])

    return "\n".join(baris)