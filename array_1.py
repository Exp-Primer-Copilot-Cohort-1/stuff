from typing import List
sauces = ["Tomato Sauce", "Brown Sauce", "Pickle Sauce"]

choices: List[str] = []

print("Welcome to the shop!")
print("Our menu today is a cheese sandwich with your selection of four sauces.")
print("Please select four sauces from the following list: ")

for i, sauce in enumerate(sauces):
    print(i, sauce)

while len(choices) < 4:
    try:
        sauce = int(input("Please select a sauce: "))
        choices.append(sauces[sauce])
    except:
        print("Please enter a number between 0 and 2")

print("You have selected: ")
for choice in choices:
    print(choice)