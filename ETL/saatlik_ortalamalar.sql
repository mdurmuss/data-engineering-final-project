/****** 
"Beşiktaş Hava Durumu.csv" dosyası veritabanına varchar olarak atıldı.   
Sütun isimleri default olarak kaldı, veritabanına atabilmek için : işaretleri ; ile virgüller de noktayla değiştirildi.
Dönüşümler aşağıdaki sorgu ile yapıldı.
******/
with cte as
(
SELECT SUBSTRING(convert(varchar, ZAMAN, 20),0,14) as zaman,
		cast(SICAKLIK as float) as sicaklik,
		cast(NEM as float) as nem,
		cast(RUZGAR_HIZI as float) as ruzgar,
		cast(YAGIS as float) as yagis
		--,cast(zaman as datetime) as zaman2
FROM [besiktas].[dbo].[havadurumu]
) 
select zaman,
	AVG(sicaklik) as ort_sicaklik,
	AVG(nem) as ort_nem,
	AVG(ruzgar) as ort_ruzgar,
	AVG(yagis) as ort_yagis
FROM cte
GROUP BY zaman
ORDER BY zaman
