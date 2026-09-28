Erişim Kontrol ve Yönetim Paneli Simülasyonu

Python ile yazılmış, IP ve parola tabanlı rol bazlı erişim kontrolü simülasyonu. Python'da koşullu ifadeleri (if/elif/else) öğrenirken yaptığım bir çalışma.

Nasıl çalışır?
Kara listedeki IP'ler girişte reddedilir.
Admin listesindeki IP'ler parola girer. Root parolası tüm menüye, admin parolası kısıtlı menüye erişim sağlar.
Bilinmeyen IP'ler sadece sistem durumunu görebilir veya yetki talebi gönderebilir.
Çalıştırma

python erisim_kontrol_simulasyonu.py

Not

Tüm veriler ve çıktılar örnektir; gerçek IP/TC sorgusu yapılmaz. Parolalar simülasyon amacıyla kodun içinde tutulur, gerçek sistemlerde hash'lenerek saklanmalıdır.

Geliştirme planı
Parolaları hash'leyerek saklamak
Giriş denemelerini log dosyasına yazmak
Fonksiyonlara bölmek
