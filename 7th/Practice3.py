def finder():
    with open("D:\\VS Code\\Python\\7th\\practice.txt","r")as f:
        data=f.read()
        if (data.find("learning")!=-1):
            print("found")
        else:
            print("not found")

finder()