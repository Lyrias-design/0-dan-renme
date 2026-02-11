root_password = ("123" , "456")
admin_password = ("789" , "741")
black_list = ("128.0.0.1" , "129.0.1.0" , "127.1.0.0")
admin_list = ("255.128.0.1" , "123.248.1.0")
girilen_IP = str(input("Lütfen IP adresinizi giriniz: "))
if girilen_IP in black_list:
    print("Girisiniz Reddedildi (yasakli IP)")
elif girilen_IP in admin_list:
    sifre = input("Admin girisiniz onaylandi LÜtfen şifrenizi giriniz: ")
    if sifre in root_password:
        root_paneli = input("""Root girişi algilandi Yetki: "HERŞEY SERBEST" Yapacağiniz işlemi seçiniz!!!\nKonum bulmak için lütfen 1'e basiniz\nIP sorgulamak için lütfen 2'e basiniz\nTC sorgulamak için lütfen 3'e basiniz
""") 
        if root_paneli == "1":
            sorgu_IPsi = input("Lütfen konumunu bulmak istediğiniz IP adresiniz giriniz: ")
            print("Girmiş olduğunuz IP adresi: TÜRKİYE Düzce/Merkez aziziye mahallesi 883. sokak")
        elif root_paneli == "2":
            sorgu_IPsi = input("Lütfen Sorgulamak istediğiniz IP adresnizi giriniz: ")
            print("UYARI: Bu IP adresi 14 farkli siber saldiri veritabaninda 'Zararli' olarak işaretlenmiş! Erişim derhal kisitlaniyor")
        elif root_paneli == "3":
            sorgu_TCsi = input("Lütfen sorgulamak istediğiniz TC'yi giriniz: ")
            print("TC Kimlik Numarasi doğrulaniyor... [OK]\nKayit Bulundu: Şahis hakkinda 'Kritik Seviye' güvenlik soruşturmasi devam etmektedir. Sistemsel erişim izni: Kisitli")
        else:
            print("Yanliş seçeneği seçtiniz. Oturumuz kapatiliyor!!!")
    
    elif sifre in admin_password:
        admin_paneli = input("""Admin girişi algilandi Yetki: KISITLI "SERBETLİK" Yapacağiniz işlemi seçiniz!!!\nKonum bulmak için lütfen 1'e basiniz\nIP sorgulamak için lütfen 2'e basiniz
""")
        if admin_paneli == "1":
            sorgu_IPsi = input("Lütfen konumunu bulmak istediğiniz IP adresiniz giriniz: ")
            print("Girmiş olduğunuz IP adresi: TÜRKİYE Düzce/Merkez aziziye mahallesi 883. sokak no:13 daire:3 kat:1")
        elif admin_paneli == "2":
            sorgu_IPsi = input("Lütfen Sorgulamak istediğiniz IP adresnizi giriniz: ")
            print("UYARI: Bu IP adresi 14 farkli siber saldiri veritabaninda 'Zararli' olarak işaretlenmiş! Erişim derhal kisitlaniyor")
        else:
            print("Yanliş seçeneği seçtiniz. Oturumuz kapatiliyor!!!")
else:
    print(f"Sistem mesaji: bilinmeyen Ip({girilen_IP}) tespit edildi!!!")
    anonim_istek = input("""Panelde ne yapmak istiyorsaniz seçiniz: \nSistem durumunu görmek için 1'e basiniz\nAdmin/Root Yetki başvurusu için 2'ye basiniz
""")
    if anonim_istek == "1":
        print("""Sistem durumu: Çevrimiçi\nAktif kullanici sayisi 3\n1 Adet: ROOT \n2 Adet: ADMİN  
""")
    elif anonim_istek == "2":
        Yetki_Talebi = input("Neden yetki istiyorsunuz ve neden biz verelim ?")
        print("Talebiniz alindi ve Yetkililere teslim edildi. Oturumunuz sonlaniyor!!!")
    else:
        print("Hatali tuşlama yaptiniz. Bağlantiniz Kesiliyor! ")
