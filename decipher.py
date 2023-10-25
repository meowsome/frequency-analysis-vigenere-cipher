from collections import Counter
from spellchecker import SpellChecker
from itertools import product

invalid_characters = ["\n", "\r", " ", ".", "!", "’", "'" ",", ";", ":"]
correctness_threshold = 75

def validate_input(ciphertext, keylength, auto):
    auto = auto == "true"
    if not isinstance(ciphertext, str): return "Ciphertext must be a string"
    elif not auto and not keylength.isdigit(): return "Keylength must be an integer"
    elif not auto and int(keylength) <= 0: return "Keylength must be >= 0"
    elif not auto and int(keylength) > len(ciphertext): return "Keylength must be <= ciphertext length"
    return None

def get_score(plaintext):
    spell = SpellChecker()
    known_word_count = len(spell.known(plaintext.split()))
    total_word_count = len(list(set(plaintext.split())))
    if known_word_count == 0 or total_word_count == 0:
        return 0
    else:
        return round(known_word_count / total_word_count * 100, 2)

def decipher(sets, ciphertext, key):
    # Decypher each set separately
    for i in range(len(key)):
        for j, letter in enumerate(sets[i]):
            sets[i][j] = chr((ord(sets[i][j]) - ord(key[i])) % 26 + 65) # Need to add 65 bc ascii A starts at 65

    # Re-combine decyphered sets into final plaintext
    final = []
    for i in range(len(sets[0])):
        for j in range(len(key)):
            if i < len(sets[j]):
                final.append(sets[j][i])

    str_list = list(ciphertext)

    # Add spaces and newlines back where they used to be 
    for i in range(len(str_list)):
        chara = str_list[i]
        if chara not in invalid_characters:
            str_list[i] = final.pop(0)

    plaintext = ''.join(str_list)
    return plaintext

def remove_dupes(k):
    new_k = []
    for elem in k:
        if elem not in new_k:
            new_k.append(elem)
    return new_k

def decrypt_given_keylength(ciphertext, keylength):
    print(f"Trying keylength {keylength}")
    sets = [[] for _ in range(keylength)]

    str_list = list(ciphertext.upper())

    # Remove newline, space
    str_list = [chara for chara in str_list if chara not in invalid_characters]

    # Separate out into separate lists for each section of the key
    for i in range(keylength):
        sets[i] = str_list[i::keylength]

    most_common_english_letters = ['E', 'T', 'A', 'O', 'I', 'N', 'S', 'R', 'H']
    most_common_cipher_letters = []

    # Fill the most_common_cipher_letters list
    for i in range(keylength):
        most_common_cipher_letters.append(dict(Counter(sets[i]))) # Get num of times each letter appears in this set

        most_common_cipher_letters[i] = {letter: most_common_cipher_letters[i][letter] / len(sets[i]) for letter in most_common_cipher_letters[i].keys()} # Convert the counts into percentages out of total letters for each set
        most_common_cipher_letters[i] = dict(reversed(sorted(most_common_cipher_letters[i].items(), key=lambda item: item[1]))) # Sort for easier reading

    # Generate all possible keys to try
    all_possible_keys = []
    common_english_letter_permutations = list(product(most_common_english_letters, repeat=keylength)) # Create combination of every most common english letter of keylength size
    for common_english_letters_of_keylength in common_english_letter_permutations:
        for common_english_letter in common_english_letters_of_keylength:
            # For this combination of most common english letter permutation and 1st most common cipher letter for each set, find key
            key = []
            for cipher_letters in most_common_cipher_letters:
                # Get the most common plaintext character and the most common ciphertext charater for each set
                first_letter = ord(list(cipher_letters.keys())[0])
                cipher_letter = ord(common_english_letter)
                
                # Find the difference between these to get this letter of the key belonging to this set
                key_index = (first_letter - cipher_letter) % 26 + 65 # Need to add 65 bc ascii A starts at 65
                key_letter = chr(key_index)
                key.append(key_letter)
            all_possible_keys.append(key)

    # Remove duplicates from list of lists of keys
    unique_data = remove_dupes(all_possible_keys)

    # Figure out what the key is 
    results = []
    for this_key in unique_data:
        plaintext = decipher(sets, ciphertext, this_key)
        final_key = ''.join(this_key)
        score = get_score(plaintext)
        results.append({'score': score, 'plaintext': plaintext, 'key': final_key})
        print(this_key, score)
        # Return early if really good score found
        if score > 70:
            return (plaintext, final_key)

    # If not returned already, return the best score
    best_scoring = max(results, key=lambda x:x['score'])
    return (best_scoring['plaintext'], best_scoring['key'])

#Iterate thru the 2nd and 3rd most common english letters, calculating and comparing the score of each and returning the one with the highest score 
def decrypt_range_keylength(ciphertext):
    keylengths = list(range(1, len(ciphertext)))
    for keylength in keylengths:
        plaintext, key = decrypt_given_keylength(ciphertext, keylength)
        score = get_score(plaintext)
        if score > correctness_threshold:
            return (plaintext, key)

    return ("", "")