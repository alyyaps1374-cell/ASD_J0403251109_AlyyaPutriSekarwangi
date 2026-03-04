#=================================================
#Nama   : Alyya Putri Sekarwangi
#NIM    : J0403251109
#Kelas  : B1
#=================================================

# ==========================================================
# Latihan 3
# ==========================================================

# Buat program dengan menggunakan algoritma insertion sort
# Tracing dengan data = [5, 2, 4, 6, 1, 3]

def insertion_sort(data):
    #loop mulai dari data ke 2 (indeks array ke 1)
    for i in range(1, len(data)):

        key = data[i] #simpan data yang disisipkan
        j = i-1 #index elemen terakhir di bagian kiri

        #geser
        while j>=0 and data[j] > key:
            data[j+1] = data[j]
            j -= 1
        #sisipkan key ke posisi yang benar
        data[j+1] = key
    return data 

data = [5, 2, 4, 6, 1, 3]
print("Data awal: ",data)
print("Hasil sorting: ",insertion_sort(data))

### SOAL ###
# 1. Tuliskan isi list setelah iterasi i = 1
# 2. Tuliskan isi list setelah iterasi i = 3
# 3. Berapa kali pergeseran terjadi pada iterasi i = 4

#### JAWABAN ###
# 1. Isi list setelah iterasi i = 1
# [2, 5, 4, 6, 1, 3]
# 2. Isi list setelah iterasi i = 3
# [2, 4, 5, 6, 1, 3]
# 3. Terjadi 4 kali pergeseran ke kiri, ketika j = -1 pergeseran akan berhenti