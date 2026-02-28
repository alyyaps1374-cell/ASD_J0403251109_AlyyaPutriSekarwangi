#=================================================
#Nama   : Alyya Putri Sekarwangi
#NIM    : J0403251109
#Kelas  : B1
#=================================================

# ==========================================================
# Contoh Backtracking 1: Kombinasi Biner (n)
# ==========================================================

def biner(n, hasil=""):
    
    # Base case: jika panjang kombinasi sudah mencapai n
    if len(hasil) == n:
        print(hasil)
        return
    
    # Rekursi dengan menambahkan '0'
    biner(n, hasil + "0")
    
    # Rekursi dengan menambahkan '1'
    biner(n, hasil + "1")


# Pemanggilan fungsi untuk menghasilkan kombinasi biner sepanjang 3
biner(3)