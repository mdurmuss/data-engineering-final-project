# Makine Ögrenmesi ile Bakim Çalışması Zamanı Önerme

<p> <img src="https://pbs.twimg.com/profile_images/1341352412540530688/EJfGb11W_400x400.jpg"> </img></p>

[Data Engineering Masterclass (DEMC–201)](https://datamasterclass.zeministanbul.ist/) eğitimi kapsamında 6.ekip olarak geliştirilen final projesi kaynak kodlarını içermektedir.

## Eğitim

Data Engineering Masterclass (DEMC–201) veri odaklı teknolojik ürün geliştirme ekiplerinin veri mühendisliği ihtiyaçları gözetilerek hazırlanmış bir uzmanlık sınıfıdır. Bu uzmanlık sınıfı, data engineering alanında uzun yıllar çalışmış, deneyim sahibi yazılım geliştiriciler, veri mühendisleri, veri bilimcileri ve sistem mühendisleri tarafından hazırlanmıştır.



## Proje Süreci

**Makine öğrenmesi teknikleri kullanılarak uygun bakım saati tahmin edilerek bakımların optimum zaman aralığında yapılmasının sağlanması hedeflenmiştir.**

**Kullanılan Veriler**

- İlgili tarih aralığında saatlik hız verisi

- Seçili yol üzerinde yapılmış bakım çalışması verisi

- İlgili yılın ulusal ve okul tatil verisi

- Saatlik yağış miktarı verisi

**Karşılaşılan zorluklar**

- Yol bakım çalışmalarının saatlik yerine gece/gündüz olarak ayrılmış olması.

- Seçtiğimiz yol üzerinde kaydedilmiş bakım çalışmalarının az olması.

- Tahmin etmeye çalıştığımız hız verisine etki eden çok fazla değişken olması. 

**Yaklaşımların Değerlendirilmesi**

- Bu çalışma kapsamında hız verisi; üç ana kümeye k-means kümeleme yöntemi ile ayrıldı. 

- Model eğitimi için Perceptron, Naive Bayes, K- Neighbors, Decision Tree ve Support Vector Machine gibi birçok yaklaşım ele alındı.

- Modelin eğitiminde en yüksek başarı oranı yakalanan K- Neighbors modeli kullanıldı. 

- Modeli test etmek için K-Fold Cross Validation yöntemi uygulandı.

- K- Neighbors Modeli test verisi üzerinde %75 başarı oranı yakalandı. 

**To Do**

- [ ] Maç günleri ya da toplumsal olaylar gibi normal olmayan durumlar analiz edilmeli.
- [ ] Veri tabanı bağlantısı sağlanmalı.
- [ ] Makine öğrenmesi için geliştirilen kod, web uygulamasından ayrılmalı.
- [ ] Harita eklentisi ile tam olarak bakım noktası kaydedilmeli. 
- [ ] Bakım sonrası bakımın sürdüğü saatler not edilmeli. Bakım raporu hazırlanan web sitesinde tutulabilir.



**Not:** Proje sürecinde veri önişleme, veri görselleştirme ile makine öğrenmesi modelleri gibi tüm arge kodları bu repoda tutulmuş olup, canlıya alınan kısmına [link](https://github.com/yasarcelep/bakim-planla) üzerinden erişilebilir.



## Ekip

- [Fatih Bilgin](https://linkedin.com/in/fatihbilgin)
- [Merve Timurlenk](https://linkedin.com/in/merve-timurlenk-758910119)
- [Yaşar Celep](https://linkedin.com/in/yasarcelep)
- [Mustafa Durmuş](https://www.linkedin.com/in/mustafadurmuss/)

