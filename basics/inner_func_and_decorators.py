

# def outer():
#     print("Outer")
#     def inner(num):
#         print("Inner: ", num)

#     return inner

# something = outer()
# something(6)

# def greater_first(func):
#      def wrap(a,b):
#         if a<b:
#          a,b=b,a
#         return func(a,b)
#      return wrap

# @greater_first
# def sub(a,b):
#     return a - b


# def division(a,b):
 
#     return a/b

    

# division = greater_first(division)
# # sub = greater_first(sub)
# result = division(3,9)
# result1 = sub(3,9)

# print(int(result))
# print(int(result1))


def many_parameters(func):
    def wrap(a,b,*args,**kargs ):
        print("Arguments",a,b,args, kargs)
        print("Key Arguments", kargs)
        return func(a,b,args, kargs)
    return wrap    

@many_parameters
def get_args(a,b ,*args, **kargs): # Yo madafaka, si no pones los *(medallas) cuando retires los decoradores el codigo se rompe
    return a,b, args, kargs

get_args("mario","R", 1)

# def many_parameters(func):
#     def wrap(*args, **kwargs):
#         print("Argumentos recibidos en el wrapper:", args, kwargs)
#         # Desempacamos para que lleguen tal cual a la función original
#         return func(*args, **kwargs)
#     return wrap

# @many_parameters
# def get_args(*args, **kwargs):
#     return args, kwargs

# # Ahora funcionará con cualquier combinación
# print(get_args("mario", "R", "Lolly", name="Papu Robot"))