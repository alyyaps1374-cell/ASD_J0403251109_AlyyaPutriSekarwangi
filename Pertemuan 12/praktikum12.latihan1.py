#=================================================
#Nama   : Alyya Putri Sekarwangi
#NIM    : J0403251109
#Kelas  : B1
#=================================================

# ==============================================================
# Materi 1: Memahami Weighted Graph dan Shortest Path Sederhana
# ==============================================================

# Representasi weighted graph menggunakan dictionary bersarang
graph = {
 'A': {'B': 4, 'C': 2},
 'B': {'D': 5},
 'C': {'D': 1},
 'D': {}
}

# Menghitung dua kemungkinan jalur dari A ke D
jalur_1 = graph['A']['B'] + graph['B']['D'] # A -> B -> D
jalur_2 = graph['A']['C'] + graph['C']['D'] # A -> C -> D

print("Jalur 1: A -> B -> D =", jalur_1)
print("Jalur 2: A -> C -> D =", jalur_2)

if jalur_1 < jalur_2:
    print("Jalur terpendek adalah A -> B -> D")
else:
    print("Jalur terpendek adalah A -> C -> D")


#Pertanyaan Analisis
#Tuliskan jawaban sebagai komentar di bagian bawah program.
# Jawaban Analisis:
# 1. Berapa total bobot jalur A -> B -> D? 
# 2 + 1 = 3

# 2. Berapa total bobot jalur A -> C -> D?
# 4 + 5 = 9

# 3. Jalur mana yang dipilih sebagai jalur terpendek? 
# Jalur terpendek adalah A -> C -> D dengan bobot 3

# 4. Mengapa jalur terpendek tidak selalu ditentukan dari jumlah edge yang paling sedikit?
# Karena jarak antara satu edge dengan lainnya bisa beda-beda, artinya bisa saja jarak dengan
# 2 edge yang dilewati bobotnya lebih kecil dibandingkan jarak dengan 1 edge yang dilewati