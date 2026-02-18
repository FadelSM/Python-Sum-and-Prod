import numpy

# 1. Membaca dimensi N dan M
n, m = map(int, input().split())

# 2. Membaca baris matriks dan memasukkannya ke dalam array NumPy
# Kita gunakan list comprehension untuk membaca N baris
data = [list(map(int, input().split())) for _ in range(n)]
my_array = numpy.array(data)

# 3. Langkah 1: Hitung jumlah (sum) sepanjang axis 0
# Ini akan menghasilkan array 1D berisi jumlah dari setiap kolom
sum_axis_0 = numpy.sum(my_array, axis=0)

# 4. Langkah 2: Hitung hasil kali (product) dari hasil penjumlahan tadi
# Karena kita mencari produk total dari hasil sum, axis tidak perlu ditentukan (default None)
result = numpy.prod(sum_axis_0)

# 5. Cetak hasil akhir
print(result)
