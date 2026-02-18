import numpy

def arrays(arr):
    # 1. Konversi list 'arr' menjadi numpy array
    # 2. Set tipe data menjadi float
    # 3. Balik urutan menggunakan slicing [::-1]
    return numpy.array(arr, float)[::-1]

arr = input().strip().split(' ')
result = arrays(arr)
print(result)