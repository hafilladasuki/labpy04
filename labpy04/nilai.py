data_mahasiswa = []

while True:
    print("\nMasukkan data mahasiswa:")
    nama = input("Nama: ")
    nim = input("Nim: ")
    tugas = int(input("Nilai Tugas: "))
    uts = int(input("Nilai UTS: "))
    uas = int(input("Nilai UAS: "))

    nilai_akhir = (tugas * 0.3) + (uts * 0.35) + (uas * 0.35)

    data_mahasiswa.append({
        'nama': nama,
        'nim' : nim,
        'tugas': tugas,
        'uts': uts,
        'uas': uas,
        'nilai_akhir': nilai_akhir
    })

    tambah = input("\nTambah data lagi? (y/t): ").lower()
    if tambah == 't':
        break

print("\nDaftar Nilai Mahasiswa:")
print("="*80)
print(f"{'Nama':<15} {'nim':<15} {'Tugas':<10} {'UTS':<10} {'UAS':<10} {'Nilai Akhir':<10}")
print("="*80)

for mhs in data_mahasiswa:
    print(f"{mhs['nama']:<15} {mhs['nim']:<15} {mhs['tugas']:<10} {mhs['uts']:<10} {mhs['uas']:<10} {mhs['nilai_akhir']:<10.2f}")

print("="*80)