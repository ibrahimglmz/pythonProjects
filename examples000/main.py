with open("newFile2.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)
    print(file.tell())

