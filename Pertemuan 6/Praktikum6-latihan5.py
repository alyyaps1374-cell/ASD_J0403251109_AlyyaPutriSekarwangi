#=============================================================
# Nama: Alyya Putri Sekarwangi
# NIM: J0403251109
# Kelas: B1
#=============================================================

#=============================================================
# Latihan 5
#=============================================================

#fungsi untuk menggabungkan dua list yang sudah terurut
def merge(left, right):
    #untuk menampung hasil penggabungan
    result = []

    #mulai dari index 0 untuk list left
    i = 0

    #mulai dari index 0 untuk list right
    j = 0

    #selama masih ada elemen di dua list
    while i < len(left) and j < len(right):

        #jika elemen left lebih kecil atau sama dengan right
        if left[i] <= right[j]:
            #tambahkan elemen left ke result
            result.append(left[i])
            i += 1
        
        #jika elemen left lebih besar dari right
        else:
            #tambahkan elemen right ke result
            result.append(right[j])
            j += 1
    #jika masih ada sisa elemen tambahkan semuanya ke result
    result.extend(left[i:])
    result.extend(right[j:])

### SOAL ###
# 1. Lengkapi kondisi agar menjadi ascending
# dibagian if menjadi: if left[i] <= right[j]:
# bertujuan agar hasilnya urut naik (kecil ke besar), kita harus mengambil elemen yang lebih kecil terlebih dahulu

### JAWABAN ###
# 2. Jelaskan fungsi result.extend()
# pada proses merge sort, result.extend() berfungsi untuk menambahan seluruh
# sisa elemen dari salah satu list ke dalam result setelah perulangan while berhenti.
# Perulangan berhenti ketika salah satu list sudah habis dibandingkan, sementara list
# lainnya masih memiliki elemen tersisa. Karena kedua list sudah dalam keadaan terurut,
# maka sisa elemen tersebut pasti sudah lebih besar (untuk ascending) dan tidak
# perlu dibandingkan lagi. Oleh karena itu, fungsi ini digunakan untuk langsung memasukkan 
# semua elemen yang tersisa sekaligus ke result.