# Diminta untuk menyiapkan data sebelum dilakukan permodelan.
# Akan dilakukan Data Preprocessing (Data Cleansing) bulan lalu, yakni Juni 2020.
# Langkah yang akan dilakukan adalah,
# 1. Mencari ID pelanggan (Nomor telepon) yang valid
# 2. Mengatasi data-data yang masih kosong (Missing Values)
# 3. Mengatasi Nilai-Nilai Pencilan (Outlier) dari setiap Variable
# 4. Menstandardisasi Nilai dari Variable

#import library
import pandas as pd
pd.options.display.max_columns = 50

#import dataset
df_load = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/dqlab_telco.csv')

#Tampilkan jumlah baris dan kolom
print(df_load.shape)

#Tampilkan 5 data teratas
print(df_load.head(5))

#Jumlah ID yang unik
print(df_load.customerID.unique())

"""
Memfilter ID Number Pelanggan Format Tertentu
"""
# Mencari format ID Number (Phone Number) Pelanggan customerID yang benar, dengan kriteria:
# 1. Panjang karakter adalah 11-12.
# 2. Terdiri dari angka Saja, tidak diperbolehkan ada karakter selain angka
# 3. Diawali dengan angka 45 2 digit pertama.

# Gunakan fungsi count() untuk menghitung banyaknya rows Customer ID, 
# anda juga bisa menggunakan str.match() & regex untuk mencocokan dengan kriteria diatas. 
# Jangan lupa gunakan astype() untuk merubah tipe datanya yang semula numeric.
# Notes : Buat kolom bantuan baru dengan nama `valid_id`
df_load['valid_id'] = df_load['customerID'].astype(str).str.match(r'(45\d{9,10})')
df_load = (df_load[df_load['valid_id'] == True]).drop('valid_id', axis = 1)
print('Hasil jumlah ID Customer yang terfilter adalah', df_load['customerID'].count())

"""
Memfilter Duplikasi ID Number Pelanggan
"""
# Memastikan bahwa tidak ada Id Number pelanggan yang duplikat. 
# Biasanya duplikasi ID number ini tipenya:
# 1. Duplikasi dikarenakan inserting melebihi satu kali dengan nilai yang sama tiap kolomnya
# 2. Duplikasi dikarenakan inserting beda periode pengambilan data
# Gunakan hasil dari pengolahan di tahap sebelumnya df_load untuk diolah di tahap ini. 
# Gunakan fungsi drop_duplicates() untuk menghapus duplikasi rows, dan gunakan sort_values() 
# untuk mengecek pengambilan data terakhir.

# Drop Duplicate Rows
df_load.drop_duplicates()
# Drop duplicate ID sorted by Periode
df_load = df_load.sort_values('UpdatedAt', ascending=False).drop_duplicates('customerID')
print('Hasil jumlah ID Customer yang sudah dihilangkan duplikasinya (distinct) adalah',df_load['customerID'].count())

"""
Mengatasi Missing Values dengan Penghapusan Rows
"""
