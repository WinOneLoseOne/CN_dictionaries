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

favourite_songs = {  #create dictionary of favourite songs
    "Pink Floyd" : "Pigs",
    "Rammstein" : "Deutchsland",
    "Metallica" : "Fade to Black",
    "Claptone" : "No Eyes",
    "Eminem" : "Superman"
}

favourite_songs.setdefault("Polyphia", "Playing God") #add item to dictionary
favourite_songs.setdefault("Chris Stapleton", "Tennessee Whiskey") #add item to dictionary

for key, value in favourite_songs.items(): #uses for loop to print song list from dictionary
    print(key, ':', value)


#challenge 2


#using the two lists, create a dictionary where country is the key and language is the value

#using your dictionary of animals, create a program which allows a user to search for an animal to see the corresponding young name

#if the animal does not exist in the dictionary, return a suitable message

#using your dictionary of animals, create a program which allows a user to submit an animal name and baby name 
#if the animal already exists, return the exisiting baby name
#if the animal doesn't exist, add it to the dictionary

