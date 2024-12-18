student={
    "name":"Dilasha",
    "subjects":{
        "physics":97,
        "chem":10,
        "Computer":"Gand"
    }
}

#Nested Dict
#Dictionary wont have duplicate keys if updated or new key with same name is formed it wont make a duplicate but overwrite it
# print (student["subjects"]["chem"]) #Acess specific key

# print(list(student.values()))#['Dilasha', {'physics': 97, 'chem': 10, 'Computer': 'Gand'}]
# pairs=(list(student.values()))#Dilasha
# print(list(student.items()))#[('name', 'Dilasha'), ('subjects', {'physics': 97, 'chem': 10, 'Computer': 'Gand'})]
# print(pairs[0])
# print(student.get("subjects")) #Better even if error doesnt stop the out put

student.update({"city":"Lalitpur"})
print(student)