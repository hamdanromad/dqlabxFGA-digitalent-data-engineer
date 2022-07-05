""" Fungsi di SQL """
"""
Fungsi Skalar Matematika - Abs
"""
select StudentID, FirstName, LastName, 
Semester1, Semester2, abs(MarkGrowth) as MarkGrowth
from students

"""
Fungsi Skalar Matematika - Ceiling
"""
select StudentID, FirstName, LastName,ceiling(Semester1) as Semester1, ceiling(Semester2) as Semester2, MarkGrowth
from students

"""
Fungsi Skalar Matematika - Floor
"""
select StudentID, FirstName, LastName, floor(Semester1) as Semester1, floor(Semester2) as Semester2, MarkGrowth
from students

"""
Fungsi Skalar Matematika - Round
"""
select StudentID, FirstName, LastName, round(Semester1,1) as Semester1, round(Semester2,0) as Semester2, MarkGrowth
from students

"""
Fungsi Skalar Matematika - Sqrt
"""
select StudentID, FirstName, LastName, sqrt(Semester1) as Semester1, Semester2, MarkGrowth
from students

"""
Task: Gunakan fungsi MOD() untuk menghitung nilai sisa jika nilai 
Semester1 dibagi 2 dan fungsi EXP() untuk menghitung nilai 
eksponensial dari nilai MarkGrowth. Gunakan kedua 
fungsi tersebut dalam satu SELECT-Statement. 
"""
select StudentID, FirstName, LastName, mod(Semester1,2) as Semester1, Semester2, EXP(MarkGrowth)
from students


""" Fungsi Text di SQL """
"""
Fungsi Text - CONCAT
"""
select StudentID, concat(FirstName, LastName) as Name, Semester1, Semester2, MarkGrowth
from students

"""
Fungsi Text - Substring Index
"""
select StudentID, substring_index(Email, '@', 1) as Name
from students;

"""
Fungsi Text - Substr
"""
select StudentID, substr(FirstName,2,3) as Initial
from students;

"""
Fungsi Text - Length
"""
select StudentId, FirstName, length(FirstName) as Total_Char
from students

"""
Fungsi Text - Replace
"""
select StudentID, Email, replace(Email, 'yahoo', 'gmail') as New_Email
from students

"""
Task: Gunakan fungsi UPPER() untuk mengubah kolom FirstName menjadi 
seluruhnya kapital dan gunakan LOWER() untuk mengubah kolom LastName
menjadi seluruhnya non-kapital. Gunakan kedua fungsi tersebut dalam 
satu SELECT-Statement.
"""
select StudentID, upper(FirstName) FirstName, lower(LastName) LastName
from students

""" Fungsi Aggregate dan Group By """
"""
Fungsi Aggregate - SUM()
"""
select sum(Semester1) as total_1, sum(Semester2) as total_2 
from students

"""
Fungsi Aggregate - Count
"""
select count(FirstName) as Total_Student
from students

"""
Fungsi Aggregate - average
"""
select avg(Semester1) as AVG_1, avg(Semester2) as AVG_2
from students

""" 
Task: Setelah memahami fungsi-fungsi sebelumnya, gunakan
fungsi MIN() dan MAX() untuk menghitung nilai dari 
kolom Semester1 dan Semester2. Gunakan fungsi tersebut 
dalam satu SELECT-Statement.
"""
select min(Semester1) Min1,
max(Semester1) Max1, min(Semester2) Min2, max(Semester2) Max2
from students

"""
Group by single column
"""
select province,
count(distinct order_id) as total_order,
sum(item_price) as total_price
from sales_retail_2019
group by province;

"""
Group by multiple columns
"""
select province, brand,
count(distinct order_id) as total_order,
sum(item_price) as total_price
from sales_retail_2019
group by province, brand

"""
Fungsi aggregate dgn grouping
"""
select province,
count(distinct order_id) as total_unique_order, sum(item_price) as revenue
from sales_retail_2019
group by province

"""
Case - When
"""
SELECT ColumnName1, ColumnName2,  
CASE  
    WHEN condition1 THEN result1  
    WHEN condition2 THEN result2  
    WHEN conditionN THEN resultN  
    ELSE result  
END as alias  
FROM TableName; 

"""
Task: Dengan menggunakan data sales_retail_2019,  buatlah syntax query yang 
menggunakan fungsi skalar MONTH() untuk mengubah order_date dari tanggal 
ke bulan, fungsi aggregate SUM() untuk menjumlahkan kolom item_price.
Tambahkan kolom remark menggunakan CASE… WHEN… statement. 
Jika sum(item_price) >= 30.000.000.000, maka remark-nya 'Target Achieved'; 
Jika sum(item_price) <= 25.000.000.000 maka remark-nya 'Less performed'; 
Selain itu, beri remark 'Follow Up'.
"""
SELECT month(order_date) AS order_month, sum(item_price) AS total_price, 
CASE  
    WHEN sum(item_price) >= 30000000000 THEN 'Target Achieved'
    WHEN sum(item_price) <= 25000000000 THEN 'Less performed'
    ELSE 'Follow up'
END as remark
FROM sales_retail_2019
GROUP BY order_month;
