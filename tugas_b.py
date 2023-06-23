def hitung_rata_nilai(nilai_array):
    total = sum(nilai_array)
    rerata = total / len(nilai_array)
    return rerata

def cari_predikat(nilai):
    if nilai > 100 or nilai < 0:
        return "Tidak valid"
    elif nilai > 90:
        return "A"
    elif nilai >= 70:
        return "B"
    elif nilai >= 50:
        return "C"
    elif nilai >= 30:
        return "D"
    else:
        return "E"

jml_matkul = int(input("Masukkan jumlah Mata Kuliah: "))
nilai_matkuls = []

for i in range(jml_matkul):
    nilai = int(input(f"Masukkan nilai mata kuliah ke-{i+1}: "))
    nilai_matkuls.append(nilai)

valid = True
for nilai in nilai_matkuls:
    if nilai > 100 or nilai < 0:
        valid = False
        break

if valid:
    print("\nHasil Predikat B dengan nilai")
    for i in range(len(nilai_matkuls)):
        predikat = cari_predikat(nilai_matkuls[i])
        print(f"Mata kuliah ke-{i}: {nilai_matkuls[i]} dengan predikat {predikat}")
else:
    print("Nilai tidak valid!")
