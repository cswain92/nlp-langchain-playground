with open("example.txt", "w+") as file:
    file.write("Hello world\n")
    file.write("This is a new line\n")

    file.seek(0)

    content = file.read()
    print(content)
