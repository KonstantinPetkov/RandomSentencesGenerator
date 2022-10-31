import random


def random_words_func(words):
    return random.choice(words)


names = ["Peter", "Michell", "Jane", "Steve"]
places = ["Sofia", "Plovdiv", "Varna", "Burgas"]
verbs = ["eats", "holds", "sees", "plays with", "brings"]
nouns = ["stones", "cake", "apple", "laptop", "bikes"]
adverbs = ["slowly", "diligently", "warmly", "sadly", "rapidly"]
details = ["near the river", "at home", "in the park"]

print("Hello, this is your first random sentence:")

while True:
    random_name = random_words_func(names)
    random_place = random_words_func(places)
    random_verb = random_words_func(verbs)
    random_noun = random_words_func(nouns)
    random_adverb = random_words_func(adverbs)
    random_detail = random_words_func(details)

    print(f"{random_name} from {random_place} {random_adverb} {random_verb} {random_noun} {random_detail}")
    print("Click [enter] to generate a new one.")
    command = input()