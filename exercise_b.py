def display(words):
    for word in words:
        print(word)

def exercise_b():
    words = [input("Enter a word: ") for i in range(5)]

    filename = input("Enter a filename with .txt extension: ")

    while not filename.endswith(".txt"):
        print("Please enter a valid filename with .txt extension")
        filename = input("Enter a filename with .txt extension: ")

    with open(filename, "w") as file:
        for word in words:
            file.write(word + "\n")

    with open(filename, "r") as file:
        loaded_words = [line.strip() for line in file]

        display(loaded_words)

exercise_b()