try:
    with open("nonexistent.txt","r") as file:
        content = file.read()
except FileNotFoundError:
    print("The file was not found.")

    # this function here attemps to read a file and handels the case where the file doesn't exist
    # by catching a FileNotFoundError