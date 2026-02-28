#=================================================
#Nama   : Alyya Putri Sekarwangi
#NIM    : J0403251109
#Kelas  : B1
#=================================================

#=================================================
#Materi rekursif : Menjumlahkan elemen list
#=================================================

def jumlah_list(data, index=0):

    # Base case: jika index sudah mencapai panjang list
    if index == len(data):
        return 0
    
    # Recursive call: menjumlahkan elemen saat ini
    # dengan hasil penjumlahan elemen berikutnya
    return data[index] + jumlah_list(data, index + 1)


print("===== Program Jumlah Data =====")

# Menampilkan hasil penjumlahan seluruh isi list
print(jumlah_list([2, 4, 6, 8]))