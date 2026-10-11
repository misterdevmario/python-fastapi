class computer:
    brand = "Papu Robot"      
 
    def __init__(self, cpu,ram, ssd):
        self.cpu = cpu
        self.ram = ram
        self.ssd = ssd
    def config(self):
        print("config: ", self.cpu, self.ram, self.ssd)
 
    @classmethod    
    def brand_info(cls):
        return cls.brand  

    @staticmethod
    def gb_to_bytes(gb):
        return  gb* (1024 ** 3)

com1 = computer("i7", "96GB", "2TB")
com2 = computer("i5", "64GB", "1TB")

com1.config()
com2.config()

print(com1.ram)