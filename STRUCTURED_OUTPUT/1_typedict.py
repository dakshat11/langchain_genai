from typing import TypedDict

class Person(TypedDict):
    
    name: str
    age: int
    
new_person = Person({'name' : "Ravi",'age' : 10} )

print(new_person)