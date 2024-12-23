def findLine():
    word="learning"
    data=True
    lineno=1
    with open("D:\\VS Code\\Python\\7th\\practice.txt","r")as f:
        while data:
            data=f.readline()
            if(word in data):
                print(lineno)
                return
            lineno+=1
        else:
            return -1

print(findLine())