""" Intro with Pandas """
import pandas as pd
import numpy as np

"""
Dataframe and Series
"""
import pandas as pd
# Series
number_list = pd.Series([1, 2, 3, 4, 5, 6])
print("Series:")
print(number_list)
# DataFrame
matrix = [[1, 2, 3],
          ['a', 'b', 'c'],
          [3, 4, 5],
          ['d', 4, 6]]
matrix_list = pd.DataFrame(matrix)
print("DataFrame:")
print(matrix_list)

"""
Atribut DataFrame & Series - Part 1
"""
# [1] method .info()
print("[1] method .info()")
print(matrix_list.info())
# [2] attribute .shape
print("\n[2] attribute .shape")
print("    Shape dari number_list:", number_list.shape)
print("    Shape dari matrix_list:", matrix_list.shape)
# [3] attribute .dtypes
print("\n[3] attribute .dtypes")
print("    Tipe data number_list:", number_list.dtypes)
print("    Tipe data matrix_list:", matrix_list.dtypes)
# [4] attribute .astype()
print("\n[4] method .astype()")
print("    Konversi number_list ke str:", number_list.astype("str"))
print("    Konversi matrix_list ke str:", matrix_list.astype("str"))

"""
Atribut DataFrame & Series - Part 2
"""
# [5] attribute .copy()
print("[5] attribute .copy()")
num_list = number_list.copy()
print("    Copy number_list ke num_list:", num_list)
mtr_list = matrix_list.copy()
print("    Copy matrix_list ke mtr_list:", mtr_list)	
# [6] attribute .to_list()
print("[6] attribute .to_list()")
print(number_list.to_list())
# [7] attribute .unique()
print("[7] attribute .unique()")
print(number_list.unique())

"""
Atribut DataFrame & Series - Part 3
"""
import pandas as pd
# Series
number_list = pd.Series([1,2,3,4,5,6])
# DataFrame
matrix_list = pd.DataFrame([[1,2,3],
				            ['a','b','c'],
				            [3,4,5],
				            ['d',4,6]])
# [8] attribute .index
print("[8] attribute .index")
print("    Index number_list:", number_list.index)
print("    Index matrix_list:", matrix_list.index)
# [9] attribute .columns
print("[9] attribute .columns")
print("    Column matrix_list:", matrix_list.columns)
# [10] attribute .loc
print("[10] attribute .loc")
print("    .loc[0:1] pada number_list:", number_list.loc[0:1])
print("    .loc[0:1] pada matrix_list:", matrix_list.loc[0:1])
# [11] attribute .iloc
print("[11] attribute .iloc")
print("    iloc[0:1] pada number_list:", number_list.iloc[0:1])
print("    iloc[0:1] pada matrix_list:", matrix_list.iloc[0:1])

"""
Creating Series & Dataframe from List
"""
import pandas as pd
# Creating series from list
ex_list = ['a',1,3,5,'c','d']
ex_series = pd.Series(ex_list)
print(ex_series)
# Creating dataframe from list of list
ex_list_of_list = [[1, 'a', 'b', 'c'],
                   [2.5, 'd', 'e', 'f'],
		           [5, 'g', 'h', 'i'],
		           [7.5, 'j', 10.5, 'l']]
index = ['dq', 'lab', 'kar', 'lan']
cols = ['float', 'char', 'obj', 'char']
ex_df = pd.DataFrame(ex_list_of_list, index=index, columns=cols)
print(ex_df)

"""
Creating Series & Dataframe from Dictionary
"""
import pandas as pd
# Creating series from dictionary
dict_series = {'1':'a',
			   '2':'b',
			   '3':'c'}
ex_series = pd.Series(dict_series)
print(ex_series)
# Creating dataframe from dictionary
df_series = {'1':['a', 'b', 'c'],
             '2':['b', 'c', 'd'],
             '4':[2, 3, 'z']}
ex_df = pd.DataFrame(df_series)
print(ex_df)
cols = ['float', 'char', 'obj', 'char']
ex_df = pd.DataFrame(ex_list_of_list, index=index, columns=cols)
print(ex_df)

"""
Creating Series & Dataframe from Numpy Array
"""
import pandas as pd
import numpy as np
# Creating series from numpy array (1D)
arr_series = np.array([1, 2, 3, 4, 5, 6, 6, 7])
ex_series = pd.Series(arr_series)
print(ex_series)
# Creating dataframe from numpy array (2D)
arr_df = np.array([[1, 2, 3, 5],
                   [5, 6, 7, 8],
                   ['a', 'b', 'c', 10]])
ex_df = pd.DataFrame(arr_df)
print(ex_df)

""" Dataset I/O """
"""
Read Dataset - CSV dan TSV
"""
import pandas as pd
# File CSV
df_csv = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/sample_csv.csv")
print(df_csv.head(3)) # Menampilkan 3 data teratas
# File TSV
df_tsv = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/sample_tsv.tsv", sep='\t')
print(df_tsv.head(3)) # Menampilkan 3 data teratas

"""
Read Dataset - Excel
"""
import pandas as pd
# File xlsx dengan data di sheet "test"
df_excel = pd.read_excel("https://storage.googleapis.com/dqlab-dataset/sample_excel.xlsx", sheet_name="test")
print(df_excel.head(4)) # Menampilkan 4 data teratas

"""
Read Dataset - JSON
"""
import pandas as pd
# File JSON
url = "https://storage.googleapis.com/dqlab-dataset/covid2019-api-herokuapp-v2.json"
df_json = pd.read_json(url)
print(df_json.head(10)) # Menampilkan 10 data teratas

"""
Read Dataset - SQL
"""
import mysql.connector
import pandas as pd
# Membuat koneksi ke database financial di https://relational.fit.cvut.cz/dataset/Financial
my_conn = mysql.connector.connct(host='relational.fit.cvut.cz',
                                 port=3306,
                                 user='guest',
                                 passdw='relational',
                                 database='financial',
                                 use_pure=True)
# Buatlah query sql untuk membaca tabel lain
my_query = """
SELECT *
FROM loan;
"""
# If use .read_sql_query
df_loan = pd.read_sql_query(my_query, my_conn)
# Tampilkan 5 data teratas
df_load.head(5)

# If use .read_sql
df_loan = pd.read_sql(my_query, my_conn)
# Tampilkan 5 data teratas
df_load.head(5)

"""
Read Dataset - Google BigQuery
"""
import pandas as pd
# Buat query
query = """
SELECT *
FROM 'bigquery-public-data.covid19_jhu_csse_eu_summary'
LIMIT 1000;
"""
# Baca data dari Google Big Query
df_covid19_eu_summary = (
  pd.read_gbq(query, project_id='XXXXXXXX')
             ) #ID dari Google BigQuery account.
# Tampilkan 5 data teratas
df_covid19_eu_summary.head()
                                    
"""
Head and Tail
"""
import pandas as pd
# Baca file sample_csv.csv
df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/sample_csv.csv")
# Tampilkan 3 data teratas
print("Tiga data teratas:\n", df.head(3))
# Tampilkan 3 data terbawah
print("Tiga data terbawah:\n", df.tail(3))

""" Indexing, Slicing, dan Transforming """
"""
Single Index
"""
import pandas as pd
# Baca file TSV sample_tsv.tsv
df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/sample_tsv.tsv", sep="\t")
# Index dari df
print("Index:", df.index)
# Column dari df
print("Columns:", df.columns )

"""
Multi Index
"""
# Set multi index df
df_x = df.set_index(['order_date', 'city', 'customer_id'])
# Print nama dan level dari multi index
for name, level in zip(df_x.index.names, df_x.index.levels):
    print(name,':',level)

"""
Set Index
"""
# Baca file sample_tsv.tsv untuk 10 baris pertama saja
df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/sample_tsv.tsv", sep="\t", nrows=10)
# Cetak data frame awal
print("Dataframe awal:\n", df)
# Set index baru
df.index = ["Pesanan ke-" + str(i) for i in range(1, 11)]
# Cetak data frame dengan index baru
print("Dataframe dengan index baru:\n", df)

"""
Set column as index
"""
# Baca file sample_tsv.tsv dan set lah index_col sesuai instruksi
df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/sample_tsv.tsv", sep="\t", index_col=["order_date", "order_id"])
# Cetak data frame untuk 8 data teratas
print("Dataframe:\n", df.head(8))

"""
Slicing
"""
import pandas as pd
# Baca file sample_csv.csv
df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/sample_csv.csv")
# Slice langsung berdasarkan kolom
df_slice = df.loc[(df["customer_id"] == 18055) &
		          (df["product_id"].isin(["P0029","P0040","P0041","P0116","P0117"]))
				 ]
print("Slice langsung berdasarkan kolom:\n", df_slice)

"""
Slicing Part 2
"""
# Set index dari df sesuai instruksi
df = df.set_index(["order_date", "order_id", "product_id"])
# Slice sesuai intruksi
df_slice = df.loc[("2019-01-01",1612339,["P2154","P2159"]),:]
print("Slice df:\n", df_slice)

"""
Transforming Part 1
"""
# Tampilkan tipe data
print("Tipe data df:\n", df.dtypes)
# Ubah tipe data kolom order_date menjadi datetime
df["order_date"] = pd.to_datetime(df["order_date"])
# Tampilkan tipe data df setelah transformasi
print("\nTipe data df setelah transformasi:\n", df.dtypes)

"""
Transforming Part 2
"""
# Tampilkan tipe data
print("Tipe data df:\n", df.dtypes)
# Ubah tipe data kolom quantity menjadi tipe data numerik float
df["quantity"] = pd.to_numeric(df["quantity"], downcast="float")
# Ubah tipe data kolom city menjadi tipe data category
df["city"] = df["city"].astype("category")
# Tampilkan tipe data df setelah transformasi
print("\nTipe data df setelah transformasi:\n", df.dtypes)

"""
Transforming Part 3
"""
# Cetak 5 baris teratas kolom brand
print("Kolom brand awal:\n", df["brand"].head())
# Gunakan method apply untuk merubah isi kolom menjadi lower case
df["brand"] = df["brand"].apply(lambda x: x.lower())
# Cetak 5 baris teratas kolom brand
print("Kolom brand setelah apply:\n", df["brand"].head())
# Gunakan method map untuk mengambil kode brand yaitu karakter terakhirnya
df["brand"] = df["brand"].map(lambda x: x[-1])
# Cetak 5 baris teratas kolom brand
print("Kolom brand setelah map:\n", df["brand"].head())

"""
Transforming Part 4
"""
import numpy as np
import pandas as pd
# number generator, set angka seed menjadi suatu angka, bisa semua angka, supaya hasil random nya selalu sama ketika kita run
np.random.seed(1234)
# create dataframe 3 baris dan 4 kolom dengan angka random
df_tr = pd.DataFrame(np.random.rand(3,4)) 
# Cetak dataframe
print("Dataframe:\n", df_tr)
# Cara 1 dengan tanpa define function awalnya, langsung pake fungsi anonymous lambda x
df_tr1 = df_tr.applymap(lambda x: x**2 + 3*x + 2) 
print("\nDataframe - cara 1:\n", df_tr1)
# Cara 2 dengan define function 
def qudratic_fun(x):
	return x**2 + 3*x + 2
df_tr2 = df_tr.applymap(qudratic_fun)
print("\nDataframe - cara 2:\n", df_tr2)

""" Handling Missing Values """
"""
Inspeksi Missing Value
"""
import pandas as pd
# Baca file "https://storage.googleapis.com/dqlab-dataset/datacovid19.csv"
df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/datacovid19.csv")
# Cetak info dari df
print(df.info())
# Cetak jumlah missing value di setiap kolom
mv = df.isna().sum()
print("\nJumlah missing value per kolom:\n", mv)

"""
Treatment dgn drop
"""

# Cetak ukuran awal dataframe
print("Ukuran awal df: %d baris, %d kolom." % df.shape)
# Drop kolom yang seluruhnya missing value dan cetak ukurannya
df = df.dropna(axis=1, how="all")
print("Ukuran df setelah buang kolom dengan seluruh data missing: %d baris, %d kolom." % df.shape)
# Drop baris jika ada satu saja data yang missing dan cetak ukurannya
df = df.dropna(axis=0, how="any")
print("Ukuran df setelah dibuang baris yang memiliki sekurangnya 1 missing value: %d baris, %d kolom." % df.shape)

"""
Ganti dengan string
"""
# Cetak unique value pada kolom province_state
print("Unique value awal:\n", df["province_state"].unique())
# Ganti missing value dengan string "unknown_province_state"
df["province_state"] = df["province_state"].fillna("unknown_province_state")
# Cetak kembali unique value pada kolom province_state
print("Unique value setelah fillna:\n", df["province_state"].unique())

"""
Isi dengan median atau mean
"""
# Cetak nilai mean dan median awal 
print("Awal: mean = %f, median = %f." % (df["active"].mean(), df["active"].median()))
# Isi missing value kolom active dengan median
df_median = df["active"].fillna(df["active"].median())
# Cetak nilai mean dan median awal setelah diisi dengan median
print("Fillna median: mean = %f, median = %f." % (df_median.mean(), df_median.median()))
# Isi missing value kolom active dengan mean
df_mean = df["active"].fillna(df["active"].mean())
# Cetak nilai mean dan median awal setelah diisi dengan mean
print("Fillna mean: mean = %f, median = %f." % (df_mean.mean(), df_mean.median()))

"""
Handle dgn interpolasi linier
"""
import numpy as np
import pandas as pd
# Data
ts = pd.Series({
   "2020-01-01":9,
   "2020-01-02":np.nan,
   "2020-01-05":np.nan,
   "2020-01-07":24,
   "2020-01-10":np.nan,
   "2020-01-12":np.nan,
   "2020-01-15":33,
   "2020-01-17":np.nan,
   "2020-01-16":40,
   "2020-01-20":45,
   "2020-01-22":52,
   "2020-01-25":75,
   "2020-01-28":np.nan,
   "2020-01-30":np.nan
})
# Isi missing value menggunakan interpolasi linier
ts = ts.interpolate()
# Cetak time series setelah interpolasi linier
print("Setelah diisi missing valuenya:\n", ts)
