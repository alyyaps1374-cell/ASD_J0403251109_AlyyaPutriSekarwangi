#=================================================
#Nama   : Alyya Putri Sekarwangi
#NIM    : J0403251109
#Kelas  : B1
#=================================================

#=================================================
#Materi Rekursif : Call Stack
# Tracing bilangan (masuk-keluar)
#input 3
#Masuk 3 - 2 - 1
#Keluar 1- 2 - 3
#=================================================

def hitung(n):
    
    # Base case (kondisi berhenti)
    if n == 0:
        print("Selesai")
        return
    
    # Proses sebelum pemanggilan rekursif
    print("Masuk:", n)
    
    # Recursive call (fungsi memanggil dirinya sendiri dengan n-1)
    hitung(n - 1)
    
    # Proses setelah rekursif selesai (backtracking)
    print("Keluar:", n)


print("==== Program Tracing ====")

# Memanggil fungsi dengan nilai awal 3
hitung(3)