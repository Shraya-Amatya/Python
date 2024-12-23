with open("D:\\VS Code\\Python\\7th\\practice.txt","r")as f:
    data = f.read()

new_data=data.replace("Java","Python")
print(new_data)

with open("D:\\VS Code\\Python\\7th\\practice.txt","w")as f:
    data = f.write(new_data)
