"""
Ambil Seluruh Kolom dalam Suatu Tabel
"""
select * from ms_produk

"""
Ambil satu kolom
"""
select nama_produk from ms_produk

"""
Ambil lebih dari satu kolom
"""
select nama_produk, harga from ms_produk

"""
Batasi pengambilan row data
"""
select nama_produk, harga
from ms_produk
limit 5;

"""
Select distinct statement
"""
select distinct nama_customer, alamat
from ms_pelanggan 

""" Prefix dan Alias """
"""
Prefix pada nama kolom
"""
select ms_produk.kode_produk
from ms_produk

"""
Alias pada kolom
"""
select no_urut as nomor,
nama_produk as nama
from ms_produk

"""
Hilangkan keyword 'AS'
"""
select no_urut nomor, nama_produk nama from ms_produk

"""
Gabungkan prefix dan alias
"""
select ms_produk.harga as harga_jual from ms_produk

"""
Alias pada tabel
"""
select * from ms_produk t2

"""
Prefix dgn alias tabel
"""
select t2.nama_produk, t2.harga 
from ms_produk t2

""" Menggunakan Filter """
"""
Where
"""
select *
from ms_produk
where nama_produk = 'Tas Travel Organizer DQLab'

"""
Operand OR
"""
select *
from ms_produk
where nama_produk = 'Gantungan Kunci DQLab' or nama_produk = 'Tas Travel Organizer DQLab' or nama_produk = 'Flashdisk DQLab 64 GB'

"""
Filter untuk angka
"""
select *
from ms_produk
where harga > 50000

"""
Operand AND
"""
select *
from ms_produk
where nama_produk = 'Gantungan Kunci DQLab' and harga < 50000

"""
Proyek dari Cabang A
Siapkan data transaksi penjualan dengan total revenue >= IDR 100.000.
Format datanya yang akan ditampilkan adalah: kode_pelanggan, nama_produk, qty, harga, 
dan total, serta diurutkan mulai dari total revenue terbesar.
Maka perlu query data tersebut dari tabel tr_penjualan yang terdapat di database perusahaan.
Dapat dilakukan perkalian antara kolom qty dan harga untuk memperoleh total revenue setiap 
kode pelanggan yang dinyatakan ke dalam kolom total, dan menggunakan “ORDER BY total DESC” 
pada akhir query untuk mengurutkan data.
"""
select kode_pelanggan, 
nama_produk, qty,
harga, qty*harga as total
from tr_penjualan
where qty*harga >= 100000
order by total desc
