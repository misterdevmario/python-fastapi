#duck typing

class Laptop:

    def build(self):
        print("Builds")
        
class Desktop:

    def build(self):
        print("Beast Building...")
                

class Alien:
    def code(self, machine : Laptop):
        print("Alien Building...") 
        machine.build()


asus_rog = Laptop()
beast = Desktop()

papu_robot = Alien()
papu_robot.code(beast)




