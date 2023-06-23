def cari_data(array, kata):
    for data in array:
        if data.lower() == kata.lower():
            return True
    return False

jml_kata = int(input("Masukkan jumlah kata: "))
kata_array = []
for i in range(jml_kata):
    kata = input("Masukkan kata: ")
    kata_array.append(kata)

mencari_kata = input("Masukkan kata yang ingin dicari: ")

if cari_data(kata_array, mencari_kata):
    print("Ditemukan")
else:
    print("Tidak ditemukan")
