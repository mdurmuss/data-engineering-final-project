/****** 
"Beşiktaş Hava Durumu.csv" dosyası veritabanına varchar olarak atıldı.   
Sütun isimleri default olarak kaldı, veritabanına atabilmek için csv'de ayırıcı olarak kullanılan : işaretleri ; ile virgüller de noktayla değiştirildi.
Yağış verisinde olan -999 değerleri 0 olarak değiştirildi.
Dönüşümler aşağıdaki sorgu ile yapıldı.
******/
with cte as
(
SELECT SUBSTRING(convert(varchar, ZAMAN, 20),0,11) as tarih,
	   SUBSTRING(convert(varchar, ZAMAN, 20),12,2) as saat,
		cast(SICAKLIK as float) as sicaklik,
		cast(NEM as float) as nem,
		cast(RUZGAR_HIZI as float) as ruzgar,
		cast(YAGIS as float) as yagis
		--,cast(ZAMAN as datetime) as zaman2
FROM [zemin].[dbo].[besiktashavadurumu]
) 
select tarih,saat,
	AVG(sicaklik) as ort_sicaklik,
	AVG(nem) as ort_nem,
	AVG(ruzgar) as ort_ruzgar,
	AVG(yagis) as ort_yagis
FROM cte
GROUP BY tarih,saat
ORDER BY tarih,saat
