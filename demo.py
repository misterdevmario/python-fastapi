my_int_1 = -4.798
my_int_2 = 4.253

rounded_int_1 = round(my_int_1)
rounded_int_2 = round(my_int_2, 2)



result_1 = pow(2.5, 3)  # Equivalent to 2 ** 3
#print(result_1)  # 8

result_2 = pow(2, 3, 5)  # (2 ** 3) % 5
#print(result_2)  # 3


#print(5//2)

is_citizen = True
age = 18

if is_citizen:
    if age >= 18:
        print('You are eligible to vote') # You are eligible to vote
else:
    print('You are not eligible to vote')
age = 19
is_employed = True

#print(age > 19 or is_employed) # 19


distance_mi = 0
is_raining = False
has_bike = True
has_car = True
has_ride_share_app = True

if is_raining == True and has_bike == False:
    print("Better use the car")
elif has_bike == True:
    print("Enjoy the ride in your amazing bike")    


if not distance_mi:
    print("False") 