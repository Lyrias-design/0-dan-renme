yasakli_ip_listesi = ["127.0.0.1", "192.168.1.1", "10.0.0.1", "8.8.8.8"]

sifre = input("Sisteme erismek icin sifreyi giriniz: ")

if sifre == "cyber123":
    print("[+] Giriş başarili! Analiz araçlari yükleniyor...")
    
    hedef_ip = input("Lutfen tarama yapilacak hedef IP adresini giriniz: ")
    tarama_modu = input("Tarama modunu seçiniz (Hizli/Detayli): ")

    print("\n--- İŞLEM BAŞLATILIYOR ---")
    print("Hedef IP:", hedef_ip)
    print("Seçilen Mod:", tarama_modu)

    if hedef_ip in yasakli_ip_listesi:
        print(f"\n[!] HATA: {hedef_ip} adresi yasakli listededir!")
        print("[!] İşlem güvenlik nedeniyle durduruldu.")
    else:
        print("\n--- ANALİZ BAŞLATILDI ---")
        print(f"Hedef: {hedef_ip}")
        print("Durum: %100 Güvenli. Tarama izni verildi.")

else:
    print("[!] HATALI ŞİFRE! Erişim reddedildi.")

    #Evet basit ama benim ilk sorgu tarzı kodum bu kodu yazarken ve ilk çıktıyı aldığımda çok eğlendim umarım sizde eğlenirsiniz :D iyi günler!