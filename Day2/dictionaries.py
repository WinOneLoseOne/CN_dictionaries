# animals = {
#     "Lion" : "Cub",
#     "Cat" : "Kitten",
#     "Dog" : "Puppy",
#     "Horse" : "Foal"
# }

# print(animals["Dog"])

# animals["Dog"] = "Hatchling"

# print (animals["Dog"])

# print(animals.keys())

#challenge 1 and stretch

# favourite_songs = {  #create dictionary of favourite songs
#     "Pink Floyd" : "Pigs",
#     "Rammstein" : "Deutchsland",
#     "Metallica" : "Fade to Black",
#     "Claptone" : "No Eyes",
#     "Eminem" : "Superman"
# }

# favourite_songs.setdefault("Polyphia", "Playing God") #add item to dictionary
# favourite_songs.setdefault("Chris Stapleton", "Tennessee Whiskey") #add item to dictionary

# for key, value in favourite_songs.items(): #uses for loop to print song list from dictionary
#     print(key, ':', value)


#challenge 2

#using the two lists, create a dictionary where country is the key and language is the value

# countries = ["England", "Spain", "Ethiopia", "Iran"] #list of countries

# languages = ["English", "Spanish", "Amharic", "Farsi"] #list of associated languages

# countries_languages = {                 #create a dictionary for each country and associated language
#     countries[0] : languages[0],
#     countries[1] : languages[1],
#     countries[2] : languages[2],
#     countries[3] : languages[3]
# }

# print (countries_languages)

#using your dictionary of animals, create a program which allows a user to search for an animal to see the corresponding young name
#if the animal does not exist in the dictionary, return a suitable message

# animal_input = input("Type in the name of an animal: ")   #input an animal name
# animals = {
#     "Lion" : "Cub",
#     "Cat" : "Kitten",
#     "Dog" : "Puppy",
#     "Horse" : "Foal"
# }

# print(animals.get(animal_input, "This animal is not in the list")) #if the animal is in the list print the name of the baby, else, print the message

#using your dictionary of animals, create a program which allows a user to submit an animal name and baby name 
#if the animal already exists, return the exisiting baby name
#if the animal doesn't exist, add it to the dictionary

animals = {
    "Lion" : "Cub",
    "Cat" : "Kitten",
    "Dog" : "Puppy",
    "Horse" : "Foal"
}

animal_name = input("Enter an animal name: ").capitalize()

if animal_name in animals:
    print(f"The baby of an {animal_name} is a " + animals.get(animal_name))
else:
    baby_name = input("This animal is not in the list. Enter the baby name: ")
    animals.setdefault(animal_name, baby_name)
    print(f"The baby of an {animal_name} is a " + animals.get(animal_name))