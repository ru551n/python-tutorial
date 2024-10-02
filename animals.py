
from typing import List


class Animal:
    def __init__(self, type: str, sound: str):
        self._type = type
        self._sound = sound
        
    def __str__(self):
        verse: List[str] = []
        verse.append("Old MacDonald had a farm, E-I-E-I-O")
        verse.append(f"And on that farm he had a {self._type}, E-I-E-I-O")
        verse.append(f"With a {self._sound}-{self._sound} here and a {self._sound}-{self._sound} there")
        verse.append(f"Here a {self._sound}, there a {self._sound}, everywhere a {self._sound}-{self._sound}")
        
        return "\n".join(verse)
        

types = ["pig", "cow", "dog", "drunk"]
sounds = ["oink", "moo", "woof", "burp"]

animals: List[Animal] = []
for type, sound in zip(types, sounds):
    animals.append(Animal(type, sound))
    

for animal in animals:
    print(animal)
    print("\n")