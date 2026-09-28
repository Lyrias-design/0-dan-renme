root_password = ("123", "456")
admin_password = ("789", "741")
black_list = ("128.0.0.1", "129.0.1.0", "127.1.0.0")
admin_list = ("255.128.0.1", "123.248.1.0")
 
girilen_IP = input("Lütfen IP adresinizi giriniz: ")
 
if girilen_IP in black_list:
    print("Girişiniz reddedildi (yasaklı IP)")
 
elif girilen_IP in admin_list:
    hak = 3
    while hak > 0:
        sifre = input("Admin girişiniz onaylandı. Lütfen şifrenizi giriniz: ")
 
        if sifre in root_password:
            root_paneli = input("""Root girişi algılandı. Yetki: "HER ŞEY SERBEST"
Yapacağınız işlemi seçiniz:
Konum bulmak için 1'e basınız
IP sorgulamak için 2'ye basınız
TC sorgulamak için 3'e basınız
""")
            if root_paneli == "1":
                sorgu_IPsi = input("Konumunu bulmak istediğiniz IP adresini giriniz: ")
                print("Örnek konum: Örnek Mah. Test Sk. No:1, Düzce (örnek veri)")
            elif root_paneli == "2":
                sorgu_IPsi = input("Sorgulamak istediğiniz IP adresini giriniz: ")
                print("UYARI (örnek çıktı): Bu IP adresi 14 saldırı veritabanında 'zararlı' olarak işaretlenmiş!")
            elif root_paneli == "3":
                sorgu_TCsi = input("Sorgulamak istediğiniz TC'yi giriniz: ")
                print("TC doğrulanıyor... [OK]\nKayıt bulundu (örnek veri). Sistem erişim izni: Kısıtlı")
            else:
                print("Yanlış seçenek. Oturum kapatılıyor!")
            break
 
        elif sifre in admin_password:
            admin_paneli = input("""Admin girişi algılandı. Yetki: KISITLI
Yapacağınız işlemi seçiniz:
Konum bulmak için 1'e basınız
IP sorgulamak için 2'ye basınız
""")
            if admin_paneli == "1":
                sorgu_IPsi = input("Konumunu bulmak istediğiniz IP adresini giriniz: ")
                print("Örnek konum: Örnek Mah. Test Sk. No:1, Düzce (örnek veri)")
            elif admin_paneli == "2":
                sorgu_IPsi = input("Sorgulamak istediğiniz IP adresini giriniz: ")
                print("UYARI (örnek çıktı): Bu IP adresi 14 saldırı veritabanında 'zararlı' olarak işaretlenmiş!")
            else:
                print("Yanlış seçenek. Oturum kapatılıyor!")
            break
 
        else:
            hak = hak - 1
            print("Hatalı şifre. Kalan hak:", hak)
 
    if hak == 0:
        print("Çok fazla hatalı deneme. Bağlantı kesiliyor!")
 
else:
    print(f"Sistem mesajı: bilinmeyen IP ({girilen_IP}) tespit edildi!")
    anonim_istek = input("""Panelde ne yapmak istiyorsunuz?
Sistem durumunu görmek için 1'e basınız
Admin/Root yetki başvurusu için 2'ye basınız
""")
    if anonim_istek == "1":
        print("Sistem durumu: Çevrimiçi\nAktif kullanıcı sayısı: 3\n1 adet: ROOT\n2 adet: ADMİN")
    elif anonim_istek == "2":
        yetki_talebi = input("Neden yetki istiyorsunuz? ")
        print("Talebiniz alındı ve yetkililere iletildi. Oturum sonlanıyor!")
    else:
        print("Hatalı tuşlama. Bağlantınız kesiliyor!")
