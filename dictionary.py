igbo_dictionary = {
    "hello": "ndewo",
    "goodbye": "ka omesia",
    "thank you": "biko",
    "yes": "ee",
    "no": "mba",
    "man": "nwoke",
    "woman": "nwanyi",
    "child": "nwa",
    "food": "nri",
    "water": "mmiri",
    "house": "ulo",
    "school": "ulo akwukwo",
    "friend": "enyi",
    "love": "ihunanya",
    "money": "ego",
    "work": "oru",
    "day": "ubochi",
    "night": "abali",
    "book": "akwukwo"
    }

languages = {"igbo":igbo_dictionary}

print("Available languages:")
for language in languages:
        print("-", language.capitalize())

chosen_language = input("choose a language:").lower()

if chosen_language in languages:
        word = input("Enter an English word:").lower()

        dictionary = languages[chosen_language]

        if word in dictionary:
            print("Translation:",dictionary[word])
        else:
                print("Word not found in the dictionary.")
else:
            print("Language not available")