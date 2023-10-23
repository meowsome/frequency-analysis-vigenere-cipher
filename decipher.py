from collections import Counter

# TODO change way of getting ascii number from letter based on canvas comment

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

    alphabet = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25}

    # Get letter by number instead of the other way around 
    def reverse_alphabet(letter_index):
        return list(alphabet.keys())[list(alphabet.values()).index(letter_index)]
    
    # Figure out what the key is 
    key = []
    for cipher_letters in most_common_cipher_letters:
        # Get the most common plaintext character and the most common ciphertext charater for each set
        first_letter = alphabet[list(cipher_letters.keys())[0]] 
        cipher_letter = alphabet[most_common_english_letters[0]]
        
        # Find the difference between these to get this letter of the key belonging to this set
        key_index = (first_letter - cipher_letter) % 26
        key_letter = reverse_alphabet(key_index)
        key.append(key_letter)

    # Decypher each set separately
    for i in range(keylength):
        for j, letter in enumerate(sets[i]):
            sets[i][j] = reverse_alphabet((alphabet[sets[i][j]] - alphabet[key[i]]) % 26)

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

    return ''.join(str_list)