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


    
