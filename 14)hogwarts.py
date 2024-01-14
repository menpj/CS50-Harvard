students = ["Hermione","Harry","Ron"]

for student in students:
    print(student)

students=[{"name": "Hermione", "house": "Grffindor","patronus":"Otter"},
{"name": "Harry", "house": "Gryffindor","patronus":"Jack Russell terrie"},
{"name": "Ron","house": "Gryffindor","patronus":"Jack Russell terrie"} ,
{"name":"Draco", "house": "Slutherin","patronus": None}]

for student in students:
    print(student["name"],student["house"],student["patronus"],sep=",")
