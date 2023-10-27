PATH_TO_FILE = './books/frankenstein.txt'


def count_words(text):
    return len(text.split())


def split_text_to_words(text):
    return text.split()


def make_word_lower_case(word):
    return word.lower()


def split_word_to_letters(word):
    return ([*word])


def flatten_letter_array(array_of_letters):
    result = []
    for letter_array in array_of_letters:
        for letter in letter_array:
            result.append(letter)
    return result


def print_report(word_count, letter_hash_map):
    print(f"--- Begin report of {PATH_TO_FILE} ---")
    print(f"{word_count} words found in the document")
    print("")
    for letter in letter_hash_map:
        print(f"The '{letter}' was found {letter_hash_map[letter]} times")
    print("--- End report ---")


def process_text(text):
    letter_array = []
    letter_hash_map = {}
    word_array = split_text_to_words(text)
    for word in word_array:
        letter_array.append(split_word_to_letters(make_word_lower_case(word)))
    flattened_letter_array = flatten_letter_array(letter_array)
    for letter in flattened_letter_array:
        if (letter.isalpha()):
            if (letter in letter_hash_map.keys()):
                letter_hash_map[letter] += 1
            else:
                letter_hash_map[letter] = 1
    sorted_letter_hash_map = dict(sorted(letter_hash_map.items()))
    return (sorted_letter_hash_map)


with open(PATH_TO_FILE) as f:
    file_contents = f.read()
    word_count = count_words(file_contents)
    letter_hash_map = process_text(file_contents)
    print_report(word_count, letter_hash_map)
