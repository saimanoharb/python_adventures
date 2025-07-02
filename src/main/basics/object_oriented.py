class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

# Dog inherits from Animal
class Dog(Animal):
    def speak(self):
        return f"{self.name} barks."

dog = Dog("Buddy")
print(dog.speak())  # Output: Buddy barks.

import __future__
print(__future__.all_feature_names)
