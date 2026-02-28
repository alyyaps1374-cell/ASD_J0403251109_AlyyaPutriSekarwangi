#=================================================
#Nama   : Alyya Putri Sekarwangi
#NIM    : J0403251109
#Kelas  : B1
#=================================================

# ==========================================================
# Latihan 2: Tracing Rekursi
# ==========================================================

def countdown(n):
    
    # Base case: berhenti saat n bernilai 0
    if n == 0:
        print("Selesai")
        return
    
    # Proses sebelum rekursi
    print("Masuk:", n)
    
    # Pemanggilan fungsi secara rekursif dengan n-1
    countdown(n - 1)
    
    # Proses setelah rekursi selesai (backtracking)
    print("Keluar:", n)


# Memulai countdown dari 3
countdown(3)