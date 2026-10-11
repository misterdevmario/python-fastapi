class Planet:
    def __init__(self, name, planet_type, star):
       if not all(isinstance(val, str) for val in (name, planet_type, star)):
         raise TypeError("name, planet type, and star must be strings")
       elif any(len(val) == 0 for val in (name, planet_type, star)):
               raise ValueError("name, planet_type, and star must be non-empty strings")
       self.name = name
       self.planet_type = planet_type
       self.star = star    
    def __str__(self):
         return f"Planet: {self.name} | Type: {self.planet_type} | Star: {self.star}"  
     
    def orbit(self):
        return f"{self.name} is orbiting around {self.star}..."      
           
planet_1 = Planet("Mars", "Red","Sun")
planet_2 = Planet("Earth", "Blue","Sun")
planet_3 = Planet("Jupiter", "Gray","Sun")

print(planet_1)
print(planet_2)
print(planet_3)

print(planet_1.orbit())
print(planet_2.orbit())
print(planet_3.orbit())
           