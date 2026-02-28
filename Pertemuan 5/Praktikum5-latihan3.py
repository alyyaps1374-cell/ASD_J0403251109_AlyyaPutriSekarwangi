#=================================================
#Nama   : Alyya Putri Sekarwangi
#NIM    : J0403251109
#Kelas  : B1
#=================================================

# ==========================================================
# Latihan 3: Mencari Nilai Maksimum
# ==========================================================

def cari_maks(data, index=0):
    
    # Base case: jika sudah di elemen terakhir
    if index == len(data) - 1:
        return data[index]
    
    # Recursive call untuk mencari maksimum pada sisa list
    maks_sisa = cari_maks(data, index + 1)
    
    # Membandingkan elemen sekarang dengan maksimum sisa
    if data[index] > maks_sisa:
        return data[index]
    else:
        return maks_sisa


angka = [3, 7, 2, 9, 5]

# Menampilkan nilai maksimum dalam list
print("Nilai maksimum:", cari_maks(angka))