# musteri-segmentasyon
Proje Adı: K-Means ile Müşteri Segmentasyonu
Açıklama:

Bu projede, bir şirketin müşteri veri seti üzerinde K-Means kümeleme algoritması kullanılarak müşteri segmentasyonu gerçekleştirildi. Hedefim, farklı harcama ve ziyaret davranışlarına sahip müşteri gruplarını tespit ederek işletmelerin pazarlama stratejilerine katkı sağlamak.
Kullanılan Yöntem - K-Means Kümeleme:

K-Means, denetimsiz öğrenmeye dayalı bir algoritmadır. Amacı, verileri birbirine benzeyen gruplara ayırmaktır. Burada kullanılan temel özellikler şunlardır:

    Yıllık gelir

    Harcama skoru

    Ziyaret sıklığı

    Sadakat süresi

Elbow yöntemi ile en uygun küme sayısı belirlendi ve K=4 olarak seçildi. Her bir müşteri bu 4 segmentten birine atandı.
Veri Seti Özellikleri:

    Simüle edilmiş 200 müşteri verisi

    5 farklı davranış özelliği içeriyor

    Gerçekçi dağılımlarla oluşturuldu

Sonuçlar ve Gözlemler:

    4 ayrı segment elde edildi: bazıları yüksek gelirli ve yüksek sadakatli, bazıları ise düşük gelirli ama yüksek harcama skoruna sahip

    Harcama skorunun, yıllık gelirle doğrudan paralel gitmediği görüldü

    Sadakat süresi ile ziyaret sıklığı arasında anlamlı farklılıklar var

Uygulama Alanları:

    Hedefli kampanya tasarımları

    Sadakat programları

    Müşteri yaşam boyu değeri tahmini

    Ürün öneri sistemleri
