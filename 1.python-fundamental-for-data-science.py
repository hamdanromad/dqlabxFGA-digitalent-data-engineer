"""
If Statement
"""
i = 7
if(i==10):
	print("ini adalah angka 10")
  
"""
If Else
"""
i = 5
if(i==10):
	print("ini adalah angka 10")
else:
	print("bukan angka 10")
  
"""
If Else Elif
"""
i = 3
if(i==5):
	print("ini adalah angka 5")
elif(i>5):
	print("lebih besar dari 5")
else:
	print("lebih kecil dari 5")
  
"""
Nested IF
"""
i=2
if (i<7):
	print("nilai i kurang dari 7")
	if(i<3):
		print("nilai i kurang dari 7 dan kurang dari 3")
	else:
		print("nilai i kurang dari 7 tapi lebih dari 3")
  
"""
Operasi Math
"""
a=10
b=5
selisih= a-b
jumlah = a+b
kali = a*b
bagi = a/b
print("Hasil penjumlahan a dan b adalah", jumlah)
print("Selisih a dan b adalah:", selisih)
print("Hasil perkalian a dan b adalah:", kali)
print("Hasil pembagian a dan b adalah:", bagi)

"""
Modulus
"""
c=10
d=3
modulus=c%d
print("Hasil modulus", modulus)

"""
Task
"""
angka=5

if(angka%2==0):
    print("angka termasuk bilangan genap")
else:
    print("angka termasuk bilangan ganjil")

""" Looping """
"""
While
"""
j = 0
while j<6:
	print("Ini adalah perulangan ke -",j)
	j=j+1
  
"""
For (1)
"""
for i in range(1,6):
	print("Ini adalah perulangan ke -", i)
  
"""
For (2)
"""
for i in range (1, 11):
    if(i%2==0):
        print("Angka genap",i)
    else:
         print("Angka ganjil",i)
       
""" Function """
"""
Buat Fungsi
"""
def salam():
	print("Hello, Selamat Pagi")
salam()

"""
Parameter pada Fungsi
"""
def luas_segitiga(alas, tinggi):
	luas = (alas*tinggi)/2
	print("Luas segitiga: %f" % luas)
luas_segitiga(4, 6)

"""
Functiong with return value
"""
def luas_segitiga(alas, tinggi):
	luas = (alas*tinggi) / 2
	return luas
print("Luas segitiga: %d" % luas_segitiga(4, 6))

""" Modul and Package """
"""
Import Package and Using Modul
"""
import math
print("Nilai pi adalah:", math.pi)

"""
Import with modul rename/as
"""
import math as m
print("Nilai pi adalah:", m.pi)

"""
Import sebagian Fungsi
"""
from math import pi
print("Nilai pi adalah", pi)

""" 
Import Semua Isi Modul
"""
from math import *
print("Nilai e adalah:", e)

""" Membaca dari File """
"""
Baca Teks File csv
"""
import requests
from contextlib import closing
import csv
url = 'https://storage.googleapis.com/dqlab-dataset/penduduk_gender_head.csv'
with closing(requests.get(url, stream=True)) as r:
	f = (line.decode('utf-8') for line in r.iter_lines())
	reader = csv.reader(f, delimiter=',')
	for row in reader:
		print(row)
    
"""
Baca file using pandas
"""
import pandas as pd

pd.set_option("display.max_columns", 50)
table = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/penduduk_gender_head.csv")
table.head()
print(table)

""" Grafik Dasar dengan Matplotlib """
"""
Bar Chart
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

table = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/penduduk_gender_head.csv")
table.head()
x_label = table['NAMA KELURAHAN']
plt.bar(x=np.arange(len(x_label)), height=table['LAKI-LAKI WNI'])

plt.show()

"""
Parameter dalam Grafik (beri nilai axis)
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

table = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/penduduk_gender_head.csv")
table.head()

x_label = table['NAMA KELURAHAN']
plt.bar(x=np.arange(len(x_label)), height=table['LAKI-LAKI WNI'])
plt.xticks(np.arange(len(x_label)), table['NAMA KELURAHAN'], rotation=30)

plt.show()

"""
Tambah title dan label
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

table = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/penduduk_gender_head.csv")
table.head()

x_label = table['NAMA KELURAHAN']
plt.bar(x=np.arange(len(x_label)), height=table['LAKI-LAKI WNI'])
plt.xticks(np.arange(len(x_label)), table['NAMA KELURAHAN'], rotation=90)
plt.xlabel('Kelurahan di Jakarta Pusat')
plt.ylabel('Jumlah Penduduk Laki - Laki')
plt.title('Persebaran Jumlah Penduduk Laki - Laki di Jakarta Pusat')

plt.show()
