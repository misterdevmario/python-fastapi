class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name.upper()} says woof woof! I'm {self.age} years old!")


dog_1 = Dog("Jack", 3)
dog_2 = Dog("Thatcher", 5)

# Call the bark method
dog_1.bark()  # JACK says woof woof! I'm 3 years old!
dog_2.bark()  # THATCHER says woof woof! I'm 5 years old!


# When using classes, the magic methods __dunder__(self) should be defined inside the body
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __len__(self):
        return self.pages

    def __str__(self):
        return f"'{self.title}' has {self.pages} pages"

    def __eq__(self, other):
        return self.pages == other.pages


book1 = Book("Built Wealth Like a Boss", 420)
book2 = Book("Be Your Own Start", 420)

print(len(book1))  # 420
print(len(book2))  # 420
print(str(book1))  # 'Built Wealth Like a Boss' has 420 pages
print(str(book2))  # 'Be Your Own Start' has 420 pages
print(book1 == book2)  # True


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person = Person("John Doe", 30)

# Loop through all attributes of the person object with dir() function
for attr in dir(person):
    # Ignore dunder methods like __init__ or __str__ and regular methods
    if not attr.startswith("__") and not callable(getattr(person, attr)):
        value = getattr(person, attr)
        print(f"{attr}: {value}")

# Output
# age: 30
# name: John Doe
