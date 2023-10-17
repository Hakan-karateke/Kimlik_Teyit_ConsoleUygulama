while True:
    a=0
    while a==0:
        kimlik_no=int(input("Lütfen TEYİT EDECEĞİNİZ TC Kimlik Numaranızı girin: "))
        b=str(kimlik_no)
        if len(b)==11 and b[0]!="0":
            a=1
        else:
            print("Lütfen TC Kimlik Numaranızı Başında 0 olmaksızın 11 haneli olarak girin.\n")
    sayac=toplam_10=0
    toplam=toplam2=0
    for i in b:
        c=int(i)
        if sayac<10:
            if sayac%2==0 and sayac<9 :
                toplam=c+toplam
            elif sayac%2==1 and sayac<9:
                toplam2=toplam2+c
            toplam_10=toplam_10+c
        sayac+=1
    hane_10=(toplam*7-toplam2)%10
    hane_11=(toplam_10)%10
    if str(hane_10)==b[9] and str(hane_11)==b[10]:
        print("BİR TC KİMLİK NUMARASINI GİRDİNİZ")
    else:
        print("GİRİLEN TC KİMLİK NO TEYİT EDİLEMEDİ!!!")