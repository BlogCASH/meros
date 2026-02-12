class doctor:
    def __init__(self , ism):
        self.name = ism
        self.bemorlar = []
    def add_bemor(self,bemor_name):
        self.bemorlar.append(bemor_name)
    def show_bemor(self):
        return self.bemorlar
    def count_bemor(self):
        return len(self.bemorlar)
    
class kasalxona :
    def __init__(self, name):
        self.name = name
        self.doctors = []
    def add_doctor(self , doctor_name):
        self.doctors.append(doctor_name)
    def show_doctors(self):
        for nomeri , doctor_ismi in enumerate(self.doctors):
            print(f"{nomeri+1}.{doctor_ismi.name} Navbat soni : {doctor_ismi.count_bemor()}")
class bemor :
    def __init__(self , name):
        self.name = name
    def choos_doctor(self , doctor_name):
        doctor_name.add_bemor(self.name)
        print(f"{self.name} {doctor_name.name} ga navbatga yozildingiz")
        print("Navbatdagi bemorlar" , doctor_name.show_bemor())
        print("Jami bemorlar soni : " , doctor_name.count_bemor())
shifoxona = kasalxona("1-son markaziy polikilinika")
doc1 = doctor("Dr.vali")
doc2 = doctor("dr.ali")
shifoxona.add_doctor(doc1)
shifoxona.add_doctor(doc2)

bemor1 =bemor("valijon")

bemor1.choos_doctor(doc1)

shifoxona.show_doctors()


        
