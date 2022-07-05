"""
Cobalah ketik query pada code editor untuk melihat keseluruhan 
isi dari kolom tabel ms_item_kategori dan ms_item_warna.
"""
select *
from ms_item_kategori;

select *
from ms_item_warna

"""
Menggabungkan Tabel dengan Key Columns
"""
select *
from ms_item_kategori, ms_item_warna
where nama_barang = nama_item

"""
Bagaimana jika urutan Tabel diubah?
"""
select * 
from ms_item_warna, ms_item_kategori
where nama_barang = nama_item

"""
Menggunakan prefix nama tabel
"""
select ms_item_kategori.*,
ms_item_warna.*
from ms_item_warna, ms_item_kategori
where nama_barang = nama_item

"""
Penggabungan tanpa kondisi
"""
select *
from ms_item_kategori, ms_item_warna

"""
Kesimpulan: Bahasa SQL diciptakan untuk sistem database relasional atau RDBMS. 
Dan aspek relasional inilah yang menjadi fitur paling penting dan unggul, 
dimana beberapa tabel dapat digabungkan menjadi satu sumber data baru.

Cara menggabungkan antar tabel disebut sebagai mekanisme join. 
Pada bab ini telah dicontohkan bagaimana dua tipe join, yaitu inner 
join dan cross join diterapkan dengan dua contoh tabel sederhana.

Inner join terjadi jika kedua tabel digabungkan melalui kolom kunci 
atau key column. Syarat penggabungan adalah dimana Isi data dari key 
column tabel yang satu harus dapat dicocokkan dengan isi data dari 
key column tabel yang lain.

Sedangkan cross join terjadi dari penggabungan tabel tanpa kondisi, 
dan menghasilkan seluruh penggabungan data seperti proses perkalian.

Untuk bab ini, inner join maupun cross join dilakukan dengan cara 
menggunakan operator koma dan pengkondisian where. Pada bab selanjutnya, 
akan terlihat penggunaan inner join dengan menggunakan keyword INNER JOIN … ON.
"""

""" INNER JOIN """
"""
Gunakan klausa INNER JOIN … ON …; 
untuk menggabungkan kedua ms_item_warna dan 
ms_item_kategori berdasarkan sintaks INNER JOIN.

Hasil yang diperoleh dengan penggunaan 
SELECT … FROM … INNER JOIN … ON …; 
adalah sama dengan penerapan SELECT … FROM … WHERE …;.
"""
select * 
from ms_item_warna
inner join ms_item_kategori 
on ms_item_warna.nama_barang = ms_item_kategori.nama_item

"""
Gunakan tabel tr_penjualan dan tabel ms_produk yang ada di-database
"""
select * from tr_penjualan;
select * from ms_produk

"""
Gabungkan tabel tr_penjualan dan ms_produk dan menampilkan seluruh kolom dari kedua tabel
"""
select *
from tr_penjualan
inner join ms_produk
on tr_penjualan.kode_produk = ms_produk.kode_produk

"""
Gabungkan tabel tr_penjualan dan ms_produk dengan kolom yang ditampilkan dari 
tabel tr_penjualan adalah kode_transaksi, kode_pelanggan, kode_produk, qty. 
Untuk tabel ms_produk tampilkan kolom nama_produk dan harga.

Kolom total yang merupakan hasil perkalian setiap baris pada 
kolom harga di tabel ms_produk dengan kolom qty di tabel tr_penjualan.

Tabel hasil penggabungan haruslah membentuk kolom-kolom dengan 
urutannya adalah kode_transaksi, kode_pelanggan, kode_produk, 
nama_produk, harga, qty, dan total.
"""
SELECT tr_penjualan.kode_transaksi, 
tr_penjualan.kode_pelanggan, 
tr_penjualan.kode_produk, 
ms_produk.nama_produk, 
ms_produk.harga, 
tr_penjualan.qty, 
ms_produk.harga*tr_penjualan.qty as total
FROM tr_penjualan
INNER JOIN ms_produk
ON tr_penjualan.kode_produk = ms_produk.kode_produk;

""" UNION """
"""
Union dua tabel
"""
select * from tabel_A
union
select * from tabel_B

"""
Union dengan klausa where
"""
select * from tabel_A
where kode_pelanggan = 'dqlabcust03'
union 
select * from tabel_B
where kode_pelanggan = 'dqlabcust03'

"""
Union dengan Conforming column
"""
select CustomerName, ContactName, City, PostalCode
from Customers
union
select SupplierName, ContactName, City, PostalCode
from Suppliers;

"""
Task INNER JOIN: Dalam database, terdapat tabel ms_pelanggan yang berisi data - data 
pelanggan yang membeli produk dan tabel tr_penjualan yang berisi 
data transaksi pembelian di suatu store.
Suatu hari, departemen marketing & promotion meminta bantuan 
untuk meng-query data-data pelanggan yang membeli produk 
Kotak Pensil DQLab, Flashdisk DQLab 32 GB, 
dan Sticky Notes DQLab 500 sheets.
Buatlah query menggunakan tabel ms_pelanggan dan tr_penjualan 
untuk mendapatkan data - data yang diminta oleh marketing 
yaitu kode_pelanggan, nama_customer, alamat.
NB: Gunakan SELECT DISTINCT untuk menghilangkan duplikasi, jika diperlukan.
"""
select distinct ms_pelanggan.kode_pelanggan, ms_pelanggan.nama_customer, ms_pelanggan.alamat

from ms_pelanggan
inner join tr_penjualan
on ms_pelanggan.kode_pelanggan = tr_penjualan.kode_pelanggan

where tr_penjualan.nama_produk = 'Kotak Pensil DQLab' 
or tr_penjualan.nama_produk = 'Flashdisk DQLab 32 GB' 
or tr_penjualan.nama_produk = 'Sticky Notes DQLab 500 sheets'

"""
Task UNION: Persiapkanlah data katalog mengenai mengenai nama - nama produk 
yang akan dijual di suatu store. Data tersebut akan digunakan dalam meeting
untuk mereview produk mana saja yang akan dilanjutkan 
penjualannya dan mana yang tidak akan dilanjutkan.
Siapkan hanya data produk dengan harga di bawah 100K untuk
kode produk prod-1 sampai prod-5; dan dibawah 50K untuk kode 
produk prod-6 sampai prod-10, tanpa mencantumkan kolom no_urut.
"""
select nama_produk, kode_produk, harga
from ms_produk_1
where harga < 100000
union

select nama_produk, kode_produk, harga
from ms_produk_2
where harga < 50000
