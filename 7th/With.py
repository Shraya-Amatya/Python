with open("D:\\VS Code\Python\\7th\\test.txt","r")as f:
    data = f.read()
    print(data)


with open("D:\\VS Code\Python\\7th\\test.txt","w")as f:
    data = f.write("Gandey chak")
    print(data)