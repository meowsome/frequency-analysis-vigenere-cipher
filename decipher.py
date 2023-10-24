from collections import Counter
from spellchecker import SpellChecker

def validate_input(ciphertext, keylength, auto):
    auto = auto == "true"
    print(auto, keylength)
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

def decrypt_given_keylength(ciphertext, keylength):
    sets = [[] for _ in range(keylength)]

    str_list = list(ciphertext.upper())

    # Remove newline, space
    str_list = [chara for chara in str_list if chara not in ["\n", "\r", " "]]

    # Separate out into separate lists for each section of the key
    for i in range(keylength):
        sets[i] = str_list[i::keylength]

    most_common_english_letters = ['E','A','R','I','O','T','N','S','L','C','U','D','P','M','H','G','B','F','Y','W','K','V','X','Z','J','Q']

    most_common_cipher_letters = []

    for i in range(keylength):
        most_common_cipher_letters.append(dict(Counter(sets[i]))) # Get num of times each letter appears in this set

        most_common_cipher_letters[i] = {letter: most_common_cipher_letters[i][letter] / len(sets[i]) for letter in most_common_cipher_letters[i].keys()} # Convert the counts into percentages out of total letters for each set
        most_common_cipher_letters[i] = dict(reversed(sorted(most_common_cipher_letters[i].items(), key=lambda item: item[1]))) # Sort for easier reading

    # Figure out what the key is 
    key = []
    for cipher_letters in most_common_cipher_letters:
        # Get the most common plaintext character and the most common ciphertext charater for each set
        first_letter = ord(list(cipher_letters.keys())[0])
        cipher_letter = ord(most_common_english_letters[0])
        
        # Find the difference between these to get this letter of the key belonging to this set
        key_index = (first_letter - cipher_letter) % 26 + 65 # Need to add 65 bc ascii A starts at 65
        key_letter = chr(key_index)
        key.append(key_letter)

    # Decypher each set separately
    for i in range(keylength):
        for j, letter in enumerate(sets[i]):
            sets[i][j] = chr((ord(sets[i][j]) - ord(key[i])) % 26 + 65) # Need to add 65 bc ascii A starts at 65

    # Re-combine decyphered sets into final plaintext
    final = []
    for i in range(len(sets[0])):
        for j in range(keylength):
            if i < len(sets[j]):
                final.append(sets[j][i])

    str_list = list(ciphertext)

    # Add spaces and newlines back where they used to be 
    for i in range(len(str_list)):
        chara = str_list[i]
        if chara not in ["\n", "\r", " "]:
            str_list[i] = final.pop(0)

    plaintext = ''.join(str_list)
    key = ''.join(key)

    return (plaintext, key)

#Iterate thru the 2nd and 3rd most common english letters, calculating and comparing the score of each and returning the one with the highest score 
def decrypt_range_keylength(ciphertext):
    keylengths = list(range(1, len(ciphertext)))
    for keylength in keylengths:
        plaintext, key = decrypt_given_keylength(ciphertext, keylength)
        score = get_score(plaintext)
        print(plaintext, key, keylength, score)
        if score > 85:
            return (plaintext, key)

    return ("", "")