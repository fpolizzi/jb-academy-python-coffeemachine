class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello, I am {}!".format(self.name))


input_name = str(input())
person = Person(input_name)
person.greet()

