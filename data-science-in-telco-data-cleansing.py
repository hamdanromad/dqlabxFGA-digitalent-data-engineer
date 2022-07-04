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
print('Total missing values data dari kolom Churn', df_load['Churn'].isnull().sum())
# Dropping all Rows with spesific column (churn)
df_load.dropna(subset=['Churn'], inplace=True)
print('Total Rows dan kolom Data setelah dihapus data Missing Values adalah', df_load.shape)

"""
Mengatasi Missing Values dengan Pengisian Nilai tertentu
"""
# Tenure pihak data modeller meminta setiap rows yang memiliki missing values untuk lama berlangganan di isi dengan 11.
# Variable yang bersifat numeric selain Tenure di isi dengan median dari masing-masing variable tersebut.
# Tentukan:
# 1. Apakah masih ada data yang missing values
# 2. Jumlah missing values dari masing-masing variable
# 3. Tangani missing values-nya
print('Status Missing Values :',df_load.isnull().values.any())
print('\nJumlah Missing Values masing-masing kolom, adalah:')
print(df_load.isnull().sum().sort_values(ascending=False))

#handling missing values Tenure fill with 11
df_load['tenure'].fillna(11, inplace=True)
#Loop
#Handling missing values num vars (except Tenure)
for col_name in list(['MonthlyCharges', 'TotalCharges']):
    #write your command here
	median = df_load[col_name].median()
	df_load[col_name].fillna(median, inplace=True)
	
print('\nJumlah Missing Values setelah di imputer datanya, adalah:')
print(df_load.isnull().sum().sort_values(ascending=False))

"""
Mendeteksi adanya Outlier (Boxplot)
"""
print('\nPersebaran data sebelum ditangani Outlier: ')
print(df_load[['tenure','MonthlyCharges','TotalCharges']].describe())

# Creating Box Plot
import matplotlib.pyplot as plt
import seaborn as sns

# Misal untuk kolom tenure
plt.figure()
sns.boxplot(x=df_load['tenure'])
plt.show()
# dan seterusnya untuk kedua kolom yang tersisa secara berurut
plt.figure()
sns.boxplot(x=df_load['MonthlyCharges'])
plt.show()
plt.figure()
sns.boxplot(x=df_load['TotalCharges'])
plt.show()

"""
Mengatasi Outlier
"""
# Your code goes here
# Handling with IQR
Q1 = (df_load[['tenure', 'MonthlyCharges', 'TotalCharges']]).quantile(0.25)
Q3 = (df_load[['tenure', 'MonthlyCharges', 'TotalCharges']]).quantile(0.75)

IQR = Q3 - Q1
maximum = Q3 + (1.5*IQR)
print('Nilai Maximum dari masing-masing Variable adalah: ')
print(maximum)
minimum = Q1 - (1.5*IQR)
print('\nNilai Minimum dari masing-masing Variable adalah: ')
print(minimum)

more_than = (df_load > maximum)
lower_than = (df_load < minimum)
df_load = df_load.mask(more_than, maximum, axis=1)
df_load = df_load.mask(lower_than, minimum, axis=1)

print('\nPersebaran data setelah ditangani Outlier: ')
print(df_load[['tenure', 'MonthlyCharges', 'TotalCharges']].describe())

"""
Mendeteksi Nilai yang Tidak Standar
"""
#Loop
for col_name in list([
  'gender',
  'SeniorCitizen',
  'Partner',
  'Dependents',		
  'PhoneService',
  'MultipleLines',
  'InternetService',
  'OnlineSecurity',
  'OnlineBackup',
  'DeviceProtection',
  'TechSupport',
  'StreamingTV',
  'StreamingMovies',
  'Contract',
  'PaperlessBilling',
  'PaymentMethod',
  'Churn'
]
):
	print('\nUnique Values Count \033[1m' + 'Before Standardized \033[0m Variable', col_name)
	print(df_load[col_name].value_counts())

"""
Menstandarisasi Variable Kategorik
"""

df_load = df_load.replace(
  ['Wanita', 'Laki-Laki', 'Churn', 'Iya'], 
  ['Female', 'Male', 'Yes', 'Yes']
)
#Loop
for col_name in list(['gender', 'Dependents', 'Churn']):
	print('\nUnique Values Count \033[1m' + 'After Standardized \033[0mVariable', col_name)
	print(df_load[col_name].value_counts())
