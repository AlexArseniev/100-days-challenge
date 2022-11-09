name_1 = input("Enter first name: ")
name_2 = input("Enter second name: ")
true_word = {"T": 0, "R": 0, "U": 0, "E": 0}
love_word = {"L": 0, "O": 0, "V": 0, "E": 0}


def check_character(current_char):
    if current_char in true_word.keys():
        true_word[current_char] += 1

    if current_char in love_word.keys():
        love_word[current_char] += 1


for character in name_1:
    check_character(character.upper())

for character in name_2:
    check_character(character.upper())

total_score = int(str(sum(true_word.values())) + str(sum(love_word.values())))

if total_score < 10 or total_score > 90:
    print(f"Your score is {total_score}, you go together like coke and mentos.")
elif 40 < total_score < 50:
    print(f"Your score is {total_score}, you are alright together.")
else:
    print(f"Your score is {total_score}.")

