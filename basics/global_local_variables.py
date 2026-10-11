a = 10
print("Global init: ", a)
def something():
    a = "Papu"
    print("Inside: ",a)

    globals()["a"] = "Robot"

something()

print("Outside: ", a)