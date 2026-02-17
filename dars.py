# # # class auto : 
# # #     def __init__(self , nomi , yili , probeg , rangi , holati , matori):
# # #         self.nomi=nomi
# # #         self.yili=yili
# # #         self.probeg=probeg
# # #         self.rangi=rangi
# # #         self.holati=holati
# # #         self.mator=matori

# # #     def get_info(self):
# # #         return f"Mashina nomi : {self.nomi} \n Mashina yili : {self.yili} \n Mashina yurgan masofasi {self.probeg} \n Mashina rangi {self.rangi}\nMashina holati {self.holati}\n Mashina matori {self.mator} "
# # #     def get_yers(self, joriy_yil):
# # #         self.yili - joriy_yil
# # #     def get_price(self, narx):
# # #         self.narx = narx

# # #     if 
# # # Avto=auto("Lacetti", 2015 , 250000 , "Qora" , "Yaxshi" , 1.8)
# # # Avto1=auto("Malubo", 2020 , 1000 , "Qora" , "Ideal" , 2.4)
# # # print(Avto1.get_info())

# # # class auto : 
# # #     def __init__(self , model , yil , probeg , rang , holat , mator):
# # #         self.model = model
# # #         self.yili = yil 
# # #         self.probeg = probeg
# # #         self.rang = rang
# # #         self.holat = holat 
# # #         self.mator = mator 
# # #     def get_info(self):
# # #         return f"Mashina nomi : {self.model} \n Mashina yili : {self.yili} \n Mashina yurgan masofasi : {self.probeg} \n Mashina rangi  : {self.rang}\nMashina holati : {self.holat}\n Mashina matori : {self.mator} "
# # #     def yers_old(self , corrent_yers , percentage_of_color):
# # #         coun_year = coun_year-self.yili
# # #         if coun_year>=5:
# # #             self.yers_old -=10000
# # #         else:
# # #              self.yers_old -=5000
# # #         if percentage_of_color !=0:
# # #             self.yers_old = self.yers_old-self.yers_old*percentage_of_color*2/100
# # #         else:
# # #             self.yers_old
# # #             return f""
# # # mashina = auto("Malibu" , 2026 , 000 , "Qora" , "Ideal" , 2.4)
# # # print(mashina.get_info())
# # class avto :
# #     def __init__(self , rusmi , rangi , mator , ):
# #         self.model=rusmi 
# #         self.rang=rangi
# #         self.mator=mator
# #     def malumotlar(self):
# #         return f"{self.model} mashina haqida malumotlar "
# # class damas(avto):
# #     def __init__(self, rusmi, rangi, mator):
# #         super().__init__(rusmi, rangi, mator)
# class ota : 
#     def __init__(self , ism , yosh):
#         self.ism = ism 
#         self.yosh = yosh 
#     def get_info(self):
#         return f"Ism : {self.ism}\n Yoshi : {self.yosh}"
    
# class bola(ota):
#     def __init__(self, ism, yosh , maktab):
#         super().__init__(ism, yosh)
#         self.school = maktab 

#     def get_data(self):
#         return f"{self.get_info()}\n Maktabi : {self.school} \n"
# talaba1 = bola("Laziz" , 16 , "20-maktab")
# print(talaba1.get_data())

# 3-misol
# class hayvon : 
    # def __init__(self , rang , yosh):
        # self.rang = rang 
        # self.yosh = yosh 
    
# class It(hayvon):
    # def __init__(self, rang, yosh , tur):
        # super().__init__(rang, yosh)
        # self.tur = tur
    # def get_info(self):
        # return f"rangi : {self.rang}\n Yoshi : {self.yosh}\n Turi : {self.tur}"
# hayvonlar = It("QORA" , 5 , "Gurji" )
# print(hayvonlar.get_info())
# 4-misol
# class Avto:
#     def __init__(self , model , yil , narx):
#         self.model = model 
#         self.yil = yil 
#         self.narx = narx
# class labo(Avto):
    # 5-misol
# class Talaba:
#     def __init__(self , ismi , yoshi ):
#         self.ism = ismi
#         self.yosh = yoshi
# class bakalavur (Talaba):
#     def __init__(self, ismi, yoshi , yili ):
#         self.yil = yili
#         super().__init__(ismi, yoshi)
#     def get_info(self):
#         return f"Talaba ismi : {self.ism}\n Talaba Yoshi : {self.yosh}\n Talaba o'qigan yil : {self.yil}"
# talaba1 = bakalavur("Munisbek" , 16 , 3)
# print(talaba1.get_info())
# # 6-msiol
# class Ustoz:
#     def __init__(self , ismi , yoshi , maktabi , dars):
#         self.ism = ismi 
#         self.yoshi = yoshi 
#         self.maktab = maktabi
#         self.dars = dars 
# class IT_ustoz(Ustoz):
#     def __init__(self, ismi, yoshi, maktabi, dars , kampyuter):
#         self.kampyuter = kampyuter
#         super().__init__(ismi, yoshi, maktabi, dars)
#     def get_info(self):
#         return f"Ustoz ismi : {self.ism}\n Ustoz yoshi : {self.yoshi}\n O'qitadigan maktabi : {self.maktab}\n O'tadigan dars nomi : {self.dars}\n Kampyuteri nomi : {self.kampyuter}"
# Ustoz1 = IT_ustoz("Mirzabek" , 25 , "IT PARK" , "Dasturchilik" , "hp")
# print(Ustoz1.get_info())
# 7-misol
# class texnika :
#     def __init__(self , telfon , ):
# 8-misol
# class kampyuter :
#     def __init__(self , nomi , ekran):
#         self.ekran = ekran 
#         self.nomi = nomi 
#     def get_info(self):
#         return f"Kompyuter nomi{self.nomi}\n Kampyuter ekran o'lchami : {self.ekran}"
# class Noutbook(kampyuter):
#     def __init__(self, nomi, ekran , shlef , touchbat , akumliator):
#         self.shlef = shlef 
#         self.touch = touchbat
#         self.akumliator = akumliator
#         super().__init__(nomi, ekran)
#     def get_info(self):
#         return f"Noutbook ochilish gradusi : {self.shlef}\n Touchbat bor yoki yo'q  : {self.touch}\n Zaryadkasi :{self.akumliator}\n Nomi : {self.nomi}\n Ekran hajmi : {self.ekran}"
# kampyuter1 = Noutbook("135 gradus" , "bor" , 2 , "Acer" , 16.5)
# print(kampyuter1.get_info())
# 10-misol
# class mashina:
#     def __init__(self , kuzf_turi , mator_hajmi , odam_sigimi):
#         self.turi = kuzf_turi
#         self.hajmi = mator_hajmi
#         self.sigim = odam_sigimi
#     def get_info(self):
#         return f"Yengil mashina kuzf turi : {self.turi}\nYengil mashina mator hajmi : {self.hajmi}\nYengil mashina odam sig'imi {self.sigim}"
# class Yuk_mashina(mashina):
#     def __init__(self, kuzf_turi, mator_hajmi, odam_sigimi , yuk_sigimi):
#         self.yuk = yuk_sigimi
#         super().__init__(kuzf_turi, mator_hajmi, odam_sigimi)
#     def malumot(self):
#         return f"Yuk sig'imi : {self.yuk}\n"
# auto = Yuk_mashina("Sedan" , 2.4 , 4 , "1 tonna")
# print(auto.get_info())
# 11 -misol
# class uchuvchi :
#     def __init__(self , samoliyot , forma):
#         self.samoliyot = samoliyot
#         self.forma = forma
# class harbiy_uchuvchi(uchuvchi):
#     def __init__(self, samoliyot, forma , shlem , qurol):
#         self.qurol = qurol
#         self.shlem = shlem
#         super().__init__(samoliyot, forma)
#     def get_info(self):
#         return f"Uchuvchida bo'ladigan : {self.samoliyot}\n Harbiy uchuvchida bo'ladigan : {self.shlem}\n Uchuvchida bo'ladigan : {self.forma}\n Harbiy uchuvchida bo'ladigan : {self.qurol}"
# samoliyot = harbiy_uchuvchi("samoliyot" , "shlem" , "forma" , "qurol")
# print(samoliyot.get_info())
# 12-misol
# class kitob:
#     def __init__(self , bet , bob , mavzu ):
#         self.bet = bet
#         self.bob = bob
#         self.mavzu = mavzu
#     def info(self):
#         return f"Kitob beti : {self.bet}\nKitob bobi : {self.bob}\n Kitob mavzusi : {self.mavzu}"
# class darslik(kitob):
#     def __init__(self, bet, bob, mavzu , munda_reja):
#         self.reja = munda_reja
#         super().__init__(bet, bob, mavzu)
#     def get_info(self):
#         return f"Darslik beti : {self.bet}\nDarslik bobi : {self.bob}\n darslik mavsusi : {self.mavzu}\n Darslik munda rejasi : {self.reja}"
# dars = darslik(100 , 5 , "hisob kitob" , "100 betli")
# kitoblar = kitob(110 , 10 , "O'tkan kunlar" )
# print(dars.get_info())
# 13-misol
# class hayvon:
#     def ovoz(self):
#         return f"Mushuk ovozi : "
# class mushuk(hayvon):
#     def 
    

# 14-misol
# class Qurulma : 
#     def __init__(self , tok , prasesor  ):
#         self.tok = tok 
#         self.prasesor = prasesor
#     def info(self):
#        return f"Batarekali / Kabelli : {self.tok}\n Prasesor Bor/Yo'q : {self.prasesor}" 
# class telefon(Qurulma):
#     def __init__(self, tok, prasesor , ekran , tugma , kamera , diktafon , rang ):
#         self.ekran = ekran
#         self.tugma = tugma 
#         self.kamera = kamera
#         self.diktafon = diktafon
#         self.rang = rang
#         super().__init__(tok, prasesor)
#     def malumot(self):
#         return f"Ekran hajmi : {self.ekran}\n Tugma borligi : {self.tugma}\n Kamera mp : {self.kamera}\n Diktafon ishlashi : {self.diktafon}\n Telefon rangi : {self.rang}\n Tok olish turi : {self.tok}\n Prasesor Bor/Yo'q : {self.prasesor}"
# class kampyuter(Qurulma):
#     def __init__(self, tok, prasesor , Usb ):
#         self.usb = Usb
#         super().__init__(tok, prasesor)
#     def get_info(self):
#         return f"Usb port bor/yo'q : {self.usb}\n Prasesor bor/yo'q : {self.prasesor} Tok olish turi : {self.tok}"
# Notebook=kampyuter("usb bor" , "prasesor bor" , "Batarekali")
# smartfon = telefon( 720 , "Yoqish tugmasi bor" , 48 , "Diktafon bor" , "ko'k" , "zaryadka orqali" , "prasesor bor")
# Qurilma1 = Qurulma("220 w" , "Prasesor bor")
# print(smartfon.malumot())
# 15-misol
# class kampaniya :
#     def __init__(self , ishchi_nomi , lavozimi , ish_vaqti , oylik_maoshi):
#         self.nomi = ishchi_nomi
#         self.lavozim = lavozimi
#         self.vaqt = ish_vaqti
#         self.maosh = oylik_maoshi
# class ishchi(kampaniya):
#     def __init__(self, ishchi_nomi, lavozimi, ish_vaqti, oylik_maoshi , diplom , tajribasi):
#         self.diplom = diplom
#         self.tajriba = tajribasi
#         super().__init__(ishchi_nomi, lavozimi, ish_vaqti, oylik_maoshi)
#     def info(self):
#         return f"Ishchi nomi : {self.nomi}\n Ish lovozimi : {self.lavozim}\n Ish vaqti : {self.vaqt}\n Oylik maoshi : {self.maosh}\n Diplom sohasi : {self.diplom}\n Tajribasi : {self.tajriba}"
# ish = ishchi("Elbek" , "Raxbar" , "9:00 dan 18:00 gacha" , "5000$" , "Axborot texnalogiyalar" , "2-yil")
# print(ish.info())
# 16-misol
# 17-misol
# class transport:
#     def __init__(self , rang , km , yil , holati , kraska , sigim , tezlik):
#         self.rang = rang
#         self.km =km
#         self.yil = yil
#         self.holat = holati
#         self.kraska = kraska
#         self.sigim = sigim 
#         self.tez =tezlik
# class autobus(transport):
#     def __init__(self, rang, km, yil, holati, kraska, sigim, tezlik , sideniya):
#         self.sideniya = sideniya
#         super().__init__(rang, km, yil, holati, kraska, sigim, tezlik)
#     def get_info(self):
#         return f"Auftobus rangi : {self.rang}\n Autobus bosgan masofasi : {self.km}\n Autobus ishlab chiqarilgan yili : {self.yil}\n Autobus holati : {self.holat}\n Autobusda kraska bor/yo'q : {self.kraska}\n Autobus odam sig'imi : {self.sigim}\n Odam olib borish tezligi : {self.tez}\n O'tirgichlar soni : {self.sideniya}"
# class poyezd(autobus):
#     def __init__(self, rang, km, yil, holati, kraska, sigim, tezlik, sideniya , kapinka_soni):
#         super().__init__(rang, km, yil, holati, kraska, sigim, tezlik, sideniya)
#         self.kapinka = kapinka_soni
#     def info(self):
#          return f"Poyezd rangi : {self.rang}\n Poyezd bosgan masofasi : {self.km}\n Poyezd ishlab chiqarilgan yili : {self.yil}\n Poyezd holati : {self.holat}\n Poyezd kraska bor/yo'q : {self.kraska}\n Poyezd odam sig'imi : {self.sigim}\n Odam olib borish tezligi : {self.tez}\n O'tirgichlar soni : {self.sideniya}\n Yotib borish honalar soni : {self.kapinka}"
# poyezd1 = poyezd("ko'k , oq , yashil" , "500 ming km" , "2015-yil" , "O'rta" , "Yo'q" , 150 , "12 soat" , 150 , 100 )       
# print(poyezd1.info())
    
# 18-misol
# class shaxs :
#     def __init__(self , ism , familya , yosh , pasport):
#         self.ism = ism
#         self.familya = familya
#         self.yosh = yosh 
#         self.pasport =pasport
# class talaba(shaxs):
#     def __init__(self, ism, familya, yosh, pasport , oqish_joyi , fan , oqish_turi):
#         self.oqish_turi = oqish_turi
#         self.fan = fan
#         self.oqish = oqish_joyi
#         super().__init__(ism, familya, yosh, pasport)
# class oqtuvchi(shaxs):
#     def __init__(self, ism, familya, yosh, pasport , diplom ):
#         self.diplom = diplom
#         super().__init__(ism, familya, yosh, pasport)
#     def info(self):
#         return f"Ism : {self.ism}\n familya : {self.familya}\n yosh : {self.yosh}\n shaxsini  tastiqlovchi hujjat : {self.pasport}\n Diplom : {self.diplom}"
# oqtuvchi1 = oqtuvchi("Sulaymon" , "Axmedov" , 16 , "Guvohnoma" , "Bakalavur")
# print(oqtuvchi1.info())
# 19-misol
# class mahsulot:
#     def __init__(self , nomi , narxi , turi):
#         self.nom = nomi
#         self.narxi =narxi
#         self.turi = turi
# class meva(mahsulot):
#     def __init__(self, nomi, narxi, turi ,rangi):
#         self.rang = rangi
#         super().__init__(nomi, narxi, turi)
#     def info(self):
#         return f"Nomi : {self.nom}\n Narxi : {self.narxi}\n Turi : {self.turi}\n Rangi : {self.rang}"
# savdo = meva("olma" , 20 , "5 barmoq" , "Qizil")
# print(savdo.info())
# 20-misol
# class bino:
#     def __init__(self , ):
# 22-misol
# class kitob:
#     def __init__(self , nomi , mavzusi , ):
#         self.nom = nomi
#         self.mavzusi =mavzusi
#         self.turi = turi
# class meva(kitob):
#     def __init__(self, nomi, narxi, turi ,rangi):
#         self.rang = rangi
#         super().__init__(nomi, narxi, turi)
#     def info(self):
#         return f"Nomi : {self.nom}\n Narxi : {self.narxi}\n Turi : {self.turi}\n Rangi : {self.rang}"
# savdo = meva("olma" , 20 , "5 barmoq" , "Qizil")
# print(savdo.info())
# 23-misol
# class mashina :
#     def __init__(self , rang , mator):
#         self.rang = rang
#         self.mator = mator 
# class elektomabil(mashina):
#     def __init__(self, rang, mator , zaryadka):
#         self.zaryad = zaryadka
#         super().__init__(rang, mator)
#     def info(self):
#         return f"mashina rangi : {self.rang}\n mashina mator hajmi : {self.mator}\n zaryadka necha km ga yetadi : {self.zaryad}"
# auto = elektomabil("Qora" , 3 , 17.000)
# print(auto.info())
# 26-misol
# class maktab : 
#     def __init__(self , manzil , nomi):
#         self.manzil = manzil
#         self.nomi = nomi 
# class sinf (maktab):
#     def __init__(self, manzil, nomi , xona_soni):
#         super().__init__(manzil, nomi)
#         self.xona = xona_soni
#     def info(self):
#         return f"maktab manzili : {self.manzil}\n maktab nomi : {self.nomi}\n sinf soni : {self.xona}"
# school = sinf("50 metrlik" , "20-maktab" , 60)
# print(school.info())
# 27-misol
# class mers :
#     def __init__(self , autopilot ):
#         self.pilot = autopilot
# class chevrolet(mers):
#     def __init__(self, autopilot , mator):
#         self.mator = mator
#         super().__init__(autopilot)
#     def info(self):
#         return f"autopilot : {self.pilot}\n mator turi : {self.mator}"
# auto = chevrolet("bor", "v8 turbosiz")
# print(auto.info())
# 28-MISOL
# class texnika :
#     def __init__(self , tok):
#         self.tok = tok 
# class skaner(texnika):
#     def __init__(self, tok , kamera , prasesor):
#         self.kamera = kamera
#         self.prasesor = prasesor
#         super().__init__(tok)
#     def get_info(self):
#         return f"Tok olish kuchi : {self.tok}w\n Kamera sifati : {self.kamera}K\n Prasesor bor/yo'q : {self.prasesor}"
# class printer(texnika):
#     def __init__(self, tok , kamera , kraska):
#         self.kamera = kamera
#         self.kraska = kraska
#         super().__init__(tok)
#     def info(self):
#         return f"Tok olish kuchi : {self.tok}w\n Kamera sifati : {self.kamera}K\n Kraska soni : {self.kraska} ta"
# printer1 = printer(220 ,4 , 5)
# scaner = skaner(220 , 4 , "Bor")
# print(printer1.info() , scaner.get_info())
# 29-misol
# class sportchi :
#     def __init__(self , sport_turi , vaxti ):
#         self.turi = sport_turi
#         self.vaxt = vaxti
# class futbolchi(sportchi):
#     def __init__(self, sport_turi, vaxti , formasi , team):
#         self.team = team
#         self.forma = formasi
#         super().__init__(sport_turi, vaxti)
#     def info (self):
#         return f"Sport turi : {self.turi}\n Trenirovka vaqti : {self.vaxt}S\n formasi : {self.forma}\n jamoasi soni : {self.team}ta"
# sport = futbolchi("Futbol" , "1:30" , "butsi , shortik , futbolka" , 12 )
# print(sport.info())
# 30-misol
# class student : 
#     def __init__(self , ismi , yosh , kursi):
#         self.ism = ismi
#         self.yosh = yosh 
#         self.kurs = kursi
# class talaba(student):
#     def __init__(self, ismi, yosh, kursi):
#         super().__init__(ismi, yosh, kursi)
#     def info (self):
#         return f"Ismi : {self.ism}\n Yoshi : {self.yosh}\n Nechanchi kurs : {self.kurs}"
# universitet = talaba("Sulaymon" , 16 , 4)
# print(universitet.info())
# 31-misol
# class damas : 
#     def __init__(self , sigim , turi , tezlik):
#         self.sigim = sigim
#         self.tur = turi 
#         self.tezlik = tezlik
# class nexia2(damas):
#     def __init__(self, sigim, turi, tezlik , mator):
#         self.mator = mator
#         super().__init__(sigim, turi, tezlik)
#     def info (self):
#         return f"Odam sig'imi : {self.sigim}\n Kuzuf turi : {self.tur}\n Tezliki : {self.tezlik}\n Mator kuchi : {self.mator}"
# auto = nexia2(4 , "sedan" , 200 , 1.6)
# print(auto.info())
# 34-misol
# class dokon : 
#     def __init__(self , nomi , turi , manzil):
#         self.nom = nomi
#         self.tur = turi 
#         self.manzil = manzil
# class cafe(dokon):
#     def __init__(self, nomi, turi, manzil , ishchi):
#         self.ishchi =ishchi
#         super().__init__(nomi, turi, manzil)
#     def info (self):
#         return f" Nomi : {self.nom}\n Sotuv turi : {self.tur}\n Manzil : {self.manzil}\n Ishchi soni : {self.ishchi}"
# savdo =cafe ("MAXSEED" , "Yegulik" , "IT PARK", 20)
# print(savdo.info())
# 35-misol
# class hayvon :
#     def __init__(self , nomi , rang):
#         self.nom = nomi
#         self.rang = rang
# class mushuk (hayvon):
#     def __init__(self, nomi, rang , yung):
#         self.yung = yung
#         super().__init__(nomi, rang)
#     def info(self):
#         return f"Mushuk nomi : {self.nom}\n Mushuk ranggi : {self.rang}\n Mushuk yunggi : {self}"
# mushuk1 = mushuk("mosh" , "Qorali oq" , "uzun")
# print(mushuk1.info())
# 36-misol
# class kampaniya : 
#     def __init__(self, ishchi):
#         self.ishchi = ishchi
# class Itkampaniya (kampaniya):
#     def __init__(self, ishchi , kamyuter):
#         self.kampyuter = kamyuter
#         super().__init__(ishchi)
#     def info(self):
#         return f"ishchilar soni : {self.ishchi}\n Kampyuter soni : {self.ishchi}"
# kam1 = Itkampaniya(10 , 20)
# print(kam1.info())
# 37-misol
# class mahsulot : 
#     def __init__(self , sroq , nomi , malumot ):
#         self.sroq = sroq 
#         self.nomi = nomi 
#         self.malumot = malumot
# class ichimlik (mahsulot):
#     def __init__(self, sroq, nomi, malumot , qadoq):
#         self.qadoq = qadoq
#         super().__init__(sroq, nomi, malumot) 
#     def info(self):
#         return f"Yaroqlilik muddati : {self.sroq}\n Nomi : {self.nomi}\n U haqida malumot : {self.malumot}\n Qadoqlangami ? {self.qadoq}"
# market = ichimlik("05.06.2026 gacha" , "CocaCola" , "gazlangan mazali ichimlik" , "ha" )
# print(market.info())
# 38-misol
# class uskuna :
#     def __init__(self , tok , nomi ):
#         self.nomi = nomi
#         self.tok = tok
# class televizor(uskuna):
#     def __init__(self, tok, nomi , ekran_kattaligi , smart):
#         self.ekran = ekran_kattaligi
#         self.smart = smart
#         super().__init__(tok, nomi)
#     def info(self):
#         return f"Tok olishi : {self.tok} W \n Nomi : {self.nomi} \n Ekran kattaligi : {self.ekran}\n TV/smart TV : {self.smart}"
# moslama = televizor(220 , "Roison" , 43 , "smart TV")
# print(moslama.info())
# 39-misol
# class auto :
#     def __init__(self , rang , mator):
#         self.rang = rang
#         self.mator = mator 
# class elektomabil(auto):
#     def __init__(self, rang, mator , zaryadka):
#         self.zaryad = zaryadka
#         super().__init__(rang, mator)
#     def info(self):
#         return f"mashina rangi : {self.rang}\n mashina mator hajmi : {self.mator}\n zaryadka necha km ga yetadi : {self.zaryad}"
# auto1 = elektomabil("Qora" , 3 , 17.000)
# print(auto1.info())
# 40-misol
# class shaxs :
#     def __init__(self , ism , familya , yosh , pasport):
#         self.ism = ism
#         self.familya = familya
#         self.yosh = yosh 
#         self.pasport =pasport
# class talaba(shaxs):
#     def __init__(self, ism, familya, yosh, pasport , oqish_joyi , fan , oqish_turi):
#         self.oqish_turi = oqish_turi
#         self.fan = fan
#         self.oqish = oqish_joyi
#         super().__init__(ism, familya, yosh, pasport)
# class oqtuvchi(shaxs):
#     def __init__(self, ism, familya, yosh, pasport , diplom ):
#         self.diplom = diplom
#         super().__init__(ism, familya, yosh, pasport)
#     def info(self):
#         return f"Ism : {self.ism}\n familya : {self.familya}\n yosh : {self.yosh}\n shaxsini  tastiqlovchi hujjat : {self.pasport}\n Diplom : {self.diplom}"
# oqtuvchi1 = oqtuvchi("Sulaymon" , "Axmedov" , 16 , "Guvohnoma" , "Bakalavur")
# print(oqtuvchi1.info())
# 41-misol
# class inson :
#     def __init__(self , ismi , yoshi , manzili):
#         self.ism = ismi 
#         self.yosh = yoshi
#         self.manzil = manzili
# class shifokor(inson):
#     def __init__(self, ismi, yoshi, manzili , diplomi):
#         self.diplom = diplomi
#         super().__init__(ismi, yoshi, manzili) 
#     def info (self):
#         return f"Ismi : {self.ism}\n Yoshi : {self.yosh}\n Yashash manzili : {self.manzil}\n diplom bor/yo'q : {self.diplom}"
# shaxs = shifokor("Doctor" , 35 , "Yakkachuqur MFY" , "bor" )
# print(shaxs.info())
# 42-misol
# class kitob:
#     def __init__(self , nomi , mavzusi , turi ):
#         self.nom = nomi
#         self.mavzusi =mavzusi
#         self.turi = turi
# class audikitob(kitob):
#     def __init__(self, nomi, mavzusi, turi , dizayni , ovozi):
#         self.dizayn = dizayni
#         self.ovoz = ovozi
#         super().__init__(nomi, mavzusi, turi)
#     def info(self):
#         return f"Nomi : {self.nom}\nTuri : {self.turi}\n dizayni : {self.dizayn}\n mavzusi : {self.mavzusi}\n ovoz sozlamasi : {self.ovoz}"
# savdo = audikitob("Biznes boshlash 202 loyiha" , "badiy" , "oq jigarrang " , "Biznes boshlash" , "mayin ")
# print(savdo.info())
# 43-misol
# class Qurilma :
#     def __init__(self , tok , nomi ):
#         self.nomi = nomi
#         self.tok = tok
# class televizor(Qurilma):
#     def __init__(self, tok, nomi , ekran_kattaligi , smart):
#         self.ekran = ekran_kattaligi
#         self.smart = smart
#         super().__init__(tok, nomi)
#     def info(self):
#         return f"Tok olishi : {self.tok} W \n Nomi : {self.nomi} \n Ekran sifati : {self.ekran}Full HDc\n smart watch/ watch: {self.smart}"
# smartwatch = televizor("batareka" , "Iwatch" , 1080 , "smart ")
#44-misol
# class sportchi :
#     def __init__(self , sport_turi , vaxti ):
#         self.turi = sport_turi
#         self.vaxt = vaxti
# class futbolchi(sportchi):
#     def __init__(self, sport_turi, vaxti , formasi , team):
#         self.team = team
#         self.forma = formasi
#         super().__init__(sport_turi, vaxti)
#     def info (self):
#         return f"Sport turi : {self.turi}\n Trenirovka vaqti : {self.vaxt}S\n formasi : {self.forma}\n jamoasi soni : {self.team}ta"
# class baskedbolchi(sportchi):
#     def __init__(self, sport_turi, vaxti , formasi , team):
#         self.team = team
#         self.forma = formasi
#         super().__init__(sport_turi, vaxti)
#     def get_info (self):
#         return f"Sport turi : {self.turi}\n Trenirovka vaqti : {self.vaxt}min\n formasi : {self.forma}\n jamoasi soni : {self.team}ta"
# game = baskedbolchi( "basketboll" , 45 , "butsi , shortik , futbolka" , 6)
# sport = futbolchi("Futbol" , "1:30" , "butsi , shortik , futbolka" , 12 )
# print(sport.info() , game.get_info())
# 45-misol
# class kampaniya : 
#     def __init__(self, ishchi):
#         self.ishchi = ishchi
# class Raxbar (kampaniya):
#     def __init__(self, ishchi , kamyuter , lavozim , ismi):
#         self.lavozim = lavozim
#         self.ism = ismi
#         self.kampyuter = kamyuter
#         super().__init__(ishchi)
#     def info(self):
#         return f"ishchilar soni : {self.ishchi}\n Kampyuter soni : {self.ishchi}\n Raxbar ismi : {self.ism}\n lavozimi : {self.lavozim}"
# kam1 = Raxbar(10 , 20 , "Sulaymon" , "rahbar" )
# print(kam1.info())
# 46-misol
# class hayvon :
#     def __init__(self , nomi , rang):
#         self.nom = nomi
#         self.rang = rang
# class Ot (hayvon):
#     def __init__(self, nomi, rang , tezlik):
#         self.tez = tezlik
#         super().__init__(nomi, rang)
#     def info(self):
#         return f"ot nomi : {self.nom}\n ot ranggi : {self.rang}\n ot tezligi : {self.tez}"
# ot1 = Ot("qorabayr" , "Qorali oq" , "juda tez")
# print(ot1.info())