#=================================================
#Nama   : Alyya Putri Sekarwangi
#NIM    : J0403251109
#Kelas  : B1
#=================================================

#=================================================
#Materi Rekursif : Faktorial
# recursive case => 3! = 3 x 2 x 1
# base case => kondisi berhenti
#=================================================

def faktorial(n):
    # Fungsi untuk menghitung nilai faktorial menggunakan rekursi
    
    # Base case (kondisi berhenti)
    if n == 0:
        return 1
    
    # Recursive case (fungsi memanggil dirinya sendiri)
    return n * faktorial(n - 1)


print("========= Program Faktorial =========")

# Menampilkan hasil faktorial dari angka 3
print("Hasil Faktorial :", faktorial(3))