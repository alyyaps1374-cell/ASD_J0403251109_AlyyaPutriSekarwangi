#=================================================
#Nama   : Alyya Putri Sekarwangi
#NIM    : J0403251109
#Kelas  : B1
#=================================================

# ==========================================================
# Latihan 4: Kombinasi Huruf
# ==========================================================

def kombinasi(n, hasil=""):
    
    # Base case: jika panjang kombinasi sudah mencapai n
    if len(hasil) == n:
        print(hasil)
        return
    
    # Rekursi dengan menambahkan huruf 'A'
    kombinasi(n, hasil + "A")
    
    # Rekursi dengan menambahkan huruf 'B'
    kombinasi(n, hasil + "B")


# Contoh pemanggilan fungsi
kombinasi(2)