#=================================================
#Nama   : Alyya Putri Sekarwangi
#NIM    : J0403251109
#Kelas  : B1
#=================================================

# ==========================================================
# Merge Sort (Ascending)
# ==========================================================

def merge_sort(data,depth=0):
    indent = " " * depth #indentasi berdasarkan level rekursif
    print(f"{indent}merge_sort({data})")

    #base case
    if len(data) <= 1:
        return data

    #Divide : Membagi data menajdi 2 bagian
    mid = len(data) // 2
    left = data[:mid] #slicing data bagian kiri
    right = data[mid:] #Slicing data bgian kanan

    print(f"{indent}divide -> left = {left} | right = {right}")


    #8 ==> left 4  dan  right 4
    #left 4 ==> mergesort ==> left 2 dan  right 2
    #left 2 ==> mergesort
    #right 2 ==> mergesort

    #recursive call
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    merged = merge(left_sorted, right_sorted)
    print(f"{indent}merge -> {left_sorted} + {right_sorted} = {merged}")

    return merge(left_sorted, right_sorted)

def merge(left,right):

    result = []
    i = 0
    j = 0

    #Membandingkan elemen di kiri dan di kanan
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j+=1
    #Menambahkan sisa elemen jika ada
    result.extend(left[i:])
    result.extend(right[j:])

    return result

angka = [13,7,28,5,19,36,4]
print("Hasil Sorting: ", merge_sort(angka))