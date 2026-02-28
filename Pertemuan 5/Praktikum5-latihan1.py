#=================================================
#Nama   : Alyya Putri Sekarwangi
#NIM    : J0403251109
#Kelas  : B1
#=================================================

# ==========================================================
# Latihan 1: Rekursi Pangkat
# ==========================================================

def pangkat(a, n):
    
    # Base case: jika pangkat bernilai 0
    if n == 0:
        return 1
    
    # Recursive case: a dikali hasil pemanggilan fungsi dengan n-1
    return a * pangkat(a, n - 1)


# Menghitung 2 pangkat 4
print(pangkat(2, 4))  # Output: 16