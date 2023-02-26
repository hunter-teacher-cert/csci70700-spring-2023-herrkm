import pyinputplus as pyip
import os


alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alpha_ranked = "EARIOTNSLCUDPMHGBFYWKVXZJQ"

def encrypt(key: int, message: str):
    message = message.upper()
    result = ""

    for letter in message:
        if letter in alpha:
            letter_index = (alpha.index(letter) + key) % len(alpha)
            result = result + alpha[letter_index]
        else:
            result = result + letter
    
    return result

def decrypt(key: int, message: str):
    return encrypt(key, message)

def most_common(message: str):
    """Return the most common alphabetic character in a string."""

    message = message.upper()
    counts = []
    chars = []

    # Create list of alphabetic characters in the message
    for char in set(message):
        if char in alpha:
            chars.append(char)

    # Count alphabetic characters in the message
    for char in chars:
        counts.append(message.count(char))
    max_freq = max(counts)

    # return the char with the highest frequency
    return chars[counts.index(max_freq)]


def decrypt_noshift(message: str):
    """Decrypt a simple shift using letter frequency and user confirmation.
    
    Finds the most common letter in a message and tests a series of shifts
    in order of letter frequency. After each attempt, prints the translated
    message and asks for user confirmation of the translated message.
    The first attempt assumes that the most frequently counted letter is E,
    then A, then R, etc. following the ranked alphabet string alpha_ranked.

    Keyword arguments:
    message (str): The encrypted message to decode.

    Returns:
    If the user confirms a translation, the translated string is returned.
    If no confirmation is found, returns None.
    """

    mode_letter = most_common(message)
    done = False
    count = 0
    # guess shift based on letter frequency
    # allow user to confirm
    while not done:
        # calculate shift between most frequent letter and current guess
        shift = alpha.index(alpha_ranked[count]) - alpha.index(mode_letter)
        print(f"Attempt {count + 1}:")
        translation = decrypt(shift, message)
        print(translation)
        confirm = pyip.inputYesNo("Is this correct?\n")
        if confirm == 'yes':
            done = True
        count += 1
        print()
        # end attempts if the last shift has been reached
        if count == len(alpha_ranked) - 1:
            print("No translation found. This may not be a shift cipher.")
            return
    return translation



def main():
    with open(os.path.join(os.sys.path[0], "message.txt"), encoding="utf8") as file:
        message_test = file.readline()
    decrypted = decrypt_noshift(message_test)



if __name__ == "__main__":
    main()
