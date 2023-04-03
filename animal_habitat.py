animals = {"lion": "savannah", "polar bear": "Arctic", "panda": "bamboo forests", "toucan": "rainforest"}

animal = input("Enter an animal: ")
if animal.lower() in animals:
    habitat = animals[animal.lower()]
    print("The", animal.lower(), "lives in the", habitat)
else:
    print("Sorry, I don't know where that animal lives.")
