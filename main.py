a = int(input("Enter 1, 2 or 3 : "))
if a == 1:
    number = input('Enter Number: ')
    number2 = input('Enter Number: ')
    measure_of_time = input('Enter Measure of time: ')
    mode_of_transportation = input('Enter Mode of Transportation: ')
    adjective = input('Enter Adjective: ')
    adjective2 = input('Enter Adjective: ')
    adjective3 = input('Enter Adjective: ')
    noun = input('Enter Noun: ')
    noun2 = input('Enter Noun: ')
    noun3 = input('Enter Noun: ')
    noun4 = input('Enter Noun: ')
    color = input('Enter Color: ')
    part_of_the_body = input('Enter Part of the body : ')
    part_of_the_body2 = input('Enter Part of the body : ')
    verb = input('Enter Verb : ')
    silly_word = input('Enter Silly Word: ')
    print(f"It was about {number} {measure_of_time} ago when I arrived at the hospital in a {mode_of_transportation}. The hospital is a/an {adjective} place, there are a lot of {adjective2} {noun} here. There are nurses here who have {color} {part_of_the_body}. If someone wants to come into my room I told them that they have to {verb} first. I’ve decorated my room with {number2} {noun2}. Today I talked to a doctor and they were wearing a {noun3} on their {part_of_the_body2}. I heard that all doctors {verb} {noun4} every day for breakfast. The most {adjective3} thing about being in the hospital is the {silly_word} {noun}")
elif a == 2:
    name = input('Proper Noun (Person’s Name): ')
    noun = input('Enter Noun: ')
    noun2 = input('Enter Noun: ')
    adjective = input('Enter Adjective (Feeling): ')
    adjective2 = input('Enter Adjective (Feeling): ')
    verb = input('Enter Verb :')
    verb2 = input('Enter Verb :')
    verb3 = input('Enter Verb + ing: ')
    animal = input('Enter Animal: ')
    color = input('Enter Color: ')
    adverb = input('Enter Adverb + ly: ')
    number = input('Enter Number: ')
    measure_of_time = input('Enter Measure of time: ')
    silly_word = input('Enter Silly Word: ')
    print(f"This weekend I am going camping with {name}. I packed my lantern, sleeping bag, and {noun}. I am so {adjective} to {verb} in a tent. I am {adjective2} we might see a(n) {animal}, I hear they’re kind of dangerous. While we’re camping, we are going to hike, fish, and {verb2}. I have heard that the {color} lake is great for {verb3}. Then we will {adverb} hike through the forest for {number} {measure_of_time}. If I see a {color} {animal} while hiking, I am going to bring it home as a pet! At night we will tell {number} {silly_word} stories and roast {noun2} around the campfire!!")
elif a == 3:
    name = input('Proper Noun (Person’s Name): ')
    adjective = input('Enter Adjective: ')
    adjective2 = input('Enter Adjective: ')
    adjective3 = input('Enter Adjective: ')
    adjective4 = input('Enter Adjective: ')
    adjective5 = input('Enter Adjective: ')
    color = input('Enter Color: ')
    animal = input('Enter Animal: ')
    place = input('Enter Place: ')
    magical_creature = ('Enter Magical Creature (Plural): ')
    magical_creature2 = ('Enter Magical Creature (Plural): ')
    room_in_a_house = ('Enter Room in a House: ')
    noun = input('Enter Noun: ')
    noun2 = input('Enter Noun: ')
    noun3 = input('Enter Noun (Plural): ')
    noun4 = input('Enter Noun (Plural): ')
    noun5 = input('Enter Noun: ')
    number = input('Enter Number: ')
    measure_of_time = input('Enter Measure of time: ')
    verb = input('Enter Verb +ing : ')
    print(f"Dear {name}, I am writing to you from a {adjective} castle in an enchanted forest. I found myself here one day after going for a ride on a {color} {animal} in {place}. There are {adjective2} {magical_creature} and {adjective3} {magical_creature2} here! In the {room_in_a_house} there is a pool full of {noun}. I fall asleep each night on a {noun2} of {noun3} and dream of {adjective4} {noun4}. It feels as though I have lived here for {number} {measure_of_time}. I hope one day you can visit, although the only way to get here now is {verb} on a {adjective5} {noun5}!!")
else:
    print("You entered enother number")