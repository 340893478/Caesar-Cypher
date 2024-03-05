# Johnny Huang (340893478)
def caesar_encrypt(word, shiftInterval):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    new_text = ""

    # Make it so that when letter is h then it shifts 3 interval to k and then this cycle repeats to all the letters shifting other 3 words aka h --> k
    for i in range(len(word)):
        for j in range(len(alphabet)):
            if word[i] == alphabet[j]:
                swap_index = j + int(shift_interval)
                new_text += alphabet[swap_index]
                # print(j, word[i], swap_index, alphabet[swap_index])
    return new_text

word = input("Enter word: ")
shift_interval = input("Enter shift interval: ")

caesar = caesar_encrypt(word, shift_interval)
print(caesar)