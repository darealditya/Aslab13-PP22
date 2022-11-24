
class Human:
    def __init__(self, name, isMale):
        self.name = name
        self.age = 20
        self.isMale = isMale
    
    def setName(self):
        self.name = 'Joko'
        print("Nama elu", self.name)
        
    def getName(self):
        return self.setName()
        
    def setAge(self):
        self.age = 35
        print("Umur elu", self.age)
        
    def getAge(self):
        return self.setAge()
        
    def setGender(self):
        if self.isMale :
            print('Lu Laki, bukan Netral')
        else:
            print('Lu Cewe kan')
        
    def getGender(self):
        return self.setGender()

orang = Human("Aditya", False)
orang.getName()
orang.getAge()
orang.getGender()