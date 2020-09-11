import time

name = input("Adınızı Yazarak Başlayabilirsiniz: ")
time.sleep(0.6)

while True:
    kararsorusu = print("Yeni Üye Kaydı mı ? Üye Girişi mi Yapmak İstersin {} "
                        "\n1)Yeni Üye Kaydı \n2)Üye Girişi ".format(name))
    cevap = input()
    if (cevap != "1"):
        print("Hatalı Tuşlama Yaptınız!")
        print("Lütfen Tekrar Deneyiniz")
        continue
    if (cevap == "1"):
        Kullanıcı_Adın = input("Yeni Kullanıcı Adınızı Giriniz: ")
        time.sleep(0.6)
        Sifre = input("Yeni Şifrenizi Belirleyiniz: ")
        time.sleep(0.6)
        baba_adı = input("Lütfen Güvenlik Amaçlı Baba Adınızı Giriniz: ")
        time.sleep(0.6)
        print("Kaydınız Başarılıyla Oluşturuldu ")
        time.sleep(0.6)
        print("Kullanıcı Adınız:", Kullanıcı_Adın)
        time.sleep(0.6)
        print("Şifreniz:", Sifre)
        time.sleep(0.6)
        print("Baba Adınız:", baba_adı)
        time.sleep(0.6)
        print("Lütfen Bilgilerinizi Unutmayınız! ")
        time.sleep(0.6)
        print("Artık Üye Girişi Yapabilirsin {}.  Aramıza Hoşgeldin:) ".format(name))

    while True:
        kullanıcıadı = input("Username: ")
        time.sleep(0.4)
        sifre = input("Password: ")
        time.sleep(0.6)
        if (kullanıcıadı == Kullanıcı_Adın) and (Sifre == sifre):
            time.sleep(0.4)
            print("Giriş Başarılı")
            exit()
        if (kullanıcıadı != Kullanıcı_Adın) and (Sifre == sifre):
            time.sleep(0.6)
            print("Kullanıcı Adını Hatalı Girdiniz!")
            time.sleep(0.6)
            print("Lütfen Yeniden Deneyiniz")
            time.sleep(0.6)
            continue
        if (kullanıcıadı == Kullanıcı_Adın) and (Sifre != sifre):
            time.sleep(0.6)
            print("Şifrenizi Yanlış Girdiniz")
            time.sleep(0.6)
            print("Yeniden Denemek mi İstersin Yoksa Yeni Bir Şifre Almak mı İstersin {} ?".format(name))
            time.sleep(0.6)
            print("1-Yeniden Denemek İstiyorum \n2-Yeni Bir Şifre Almak İstiyorum")
            time.sleep(0.6)
            cevap2 = input()
            if (cevap2 == "1"):
                time.sleep(0.6)
                print("Yeniden Giriş Yapmak Üzere Ana Sayfaya Yönlendiriliyorsun {}".format(name))
                time.sleep(0.6)
                continue
            if (cevap2 == "2"):
                time.sleep(0.6)
                print("Talebiniz Alınmıştır. Lütfen Bekleyiniz...")
                time.sleep(0.6)
                güvenlik = input("Lütfen Kontrol Amaçlı Baba Adınızı Giriniz: ")
                time.sleep(0.6)
                if (baba_adı != güvenlik):
                    print("Kontrol Sağlanamadı...")
                    break
                else:
                    print("Kontrol Sağlandı...")
                    yenisifre = input("Lütfen Yeni Şifrenizi Belirleyiniz: ")
                time.sleep(0.6)
                if (Sifre == yenisifre):
                    print("Yeni Şifreniz Eskisi İle Aynı Olamaz!")
                    time.sleep(0.6)
                    print("Lütfen Başka Bir Şifre Deneyiniz")
                    time.sleep(0.6)
                    continue
                if (Sifre != yenisifre):
                    print("Yeni Şifren Oluşturuldu {}".format(name))
                    time.sleep(0.6)
                    print("Yeni Şifren: ", yenisifre)
                    time.sleep(0.6)
                    Sifre = yenisifre
                    print("Şimdi Giriş Yapabilirsiniz.")
                    time.sleep(0.6)
                Sifre  = yenisifre
        if (kullanıcıadı != Kullanıcı_Adın) and (Sifre != sifre):
            time.sleep(0.6)
            print("Kullanıcı Adınız veya Şifreniz Hatalı Girildi")
            time.sleep(0.6)
            print("Yeniden Görüşmek Üzere... ")
            break