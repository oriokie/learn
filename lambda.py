people = [
    {"Name": "Edwin", "Town": "Kahawa"},
    {"Name": "Alex", "Town": "Maguna"},
    {"Name": "Nelson", "Town": "Wendani"},
    {"Name": "ALbert", "Town": "Kisii"}
]

people.sort(key=lambda person: person['Name'])

print (people)