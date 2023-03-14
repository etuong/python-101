def get_freq_counts(encrypted_message: str):
    """
    :param encrypted_message: the encrypted message
    :return: a dictionary that maps each character to the number of times it occurs.
    """
    dictionary = dict()
    # Loop through each character
    for s in encrypted_message:
        # And add to dictionary
        if not s in dictionary:
            dictionary[s] = 1
        # Or increment the counter
        else:
            dictionary[s] += 1
    return dictionary


if __name__ == '__main__':
    # ciphertext.txt contains the encrypted secret message
    with open('ciphertext.txt', 'r') as f:
        message = f.readline()

    dictionary = get_freq_counts(message)
    frequencies = dict()

    # freq.txt contains the frequency count for each character in the decrypted message
    with open('freq.txt', 'r') as f:
        for line in f:
            (key, val) = line.split(":")
            frequencies[key] = val.strip()

    # Decrypt
    decrypted_message = []
    for c in message:
        # Get frequency of the character
        f = dictionary[c]
        for character, count in frequencies.items():
            # Break out as soon as first occurrence happens
            if f == int(count):
                decrypted_message.append(character)
                break

    # Print the decrypted message in one single line
    print(*decrypted_message, sep='')
