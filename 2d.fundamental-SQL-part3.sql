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
"""
