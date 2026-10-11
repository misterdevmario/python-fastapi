

class A:
    def f1(self):
        print("F1 Works Well")
    def f2(self):
        print("F2 Works Well")

class B():
    def f3(self):
        print("F3 Works Well")
    def f4(self):
        print("F4 Works Well")

class C(B):
    def f5(self):
        print("F3\5 Works Well")
    def f6(self):
        print("F6 Works Well")
class D(B,C):
    def f5(self):
        print("F3\5 Works Well")

obj1 = C()
obj1.f1()
obj1.f6()
obj2 = D()
