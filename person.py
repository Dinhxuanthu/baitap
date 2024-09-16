class person:
        def __init__(self,name,age):
                self.name=name
                self.age=age
class child(person):
        def __init__(self, name, age):
                super().__init__(name, age)

person = person("Peter", 25)
child = child("Peter Junior", 5)
print(person.name)
print(person.age)
print(child.__class__.__bases__[0].__name__)
