class Kubus:
    def __init__(self, lebar, tinggi, panjang):
        self.lebar = lebar
        self.tinggi = tinggi
        self.panjang = panjang
        self.massa = None
        self.massaJenis = None
        
    def setMassa(self, massa):
        self.massa = massa
        
    def setLebar(self, lebar):
        self.lebar = lebar
        
    def setTinggi(self, tinggi):
        self.tinggi = tinggi
        
    def setPanjang(self, panjang):
        self.panjang = panjang
        
    def getMassaJenis(self):
        self.massaJenis = (self.massa)/(self.lebar * self.tinggi * self.panjang)
        return self.massaJenis

lebar = float(input())
tinggi = float(input())
panjang = float(input())
massa = float(input())

kubus = Kubus(lebar, tinggi, panjang)

kubus.setMassa(massa)
print("Massa Jenis =", kubus.getMassaJenis())

kubus.setMassa(massa*2)
print("Massa Jenis =", kubus.getMassaJenis())