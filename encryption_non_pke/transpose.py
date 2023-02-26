from math import ceil
import random

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def key_order(kwd: str):
    kwd = kwd.upper()
    sorted = list(kwd)
    sorted.sort()
    indices = []
    for char in sorted:
        indices.append(kwd.index(char))
    return indices


def encrypt(message: str, kwd: str):
    """Encrypt a message using columnar transposition.
    
    Non-alphabetic characters will be stripped.
    All letters will be converted to caps.
    Blanks in the grid will be filled by random letters.
    The message will be grouped 5 chars at a time for readability.

    Keyword arguments:
    message (str): the message to encrypt
    kwd (str): the keyword by which to reorder the columns
    """
    text = ""
    message = message.upper()
    for char in message:
        if char in alpha:
            text = text + char
    
    # create empty grid for transposition
    cols = len(kwd)
    rows = ceil(len(text) / cols)
    grid = [[" "]*len(kwd) for i in range(rows)]

    # fill grid with message
    n = 0
    for i in range(rows):
        for j in range(cols):
            if n < len(text):
                grid[i][j] = text[n]
                n += 1
            else:
                grid[i][j] = random.choice(alpha)
    
    # select cols in keyword order to create encrypted message
    encrypted = ""
    count = 0
    for col in key_order(kwd):
        for row in range(rows):
            encrypted = encrypted + grid[row][col]
            count += 1
            if count == 5:
                encrypted = encrypted + " "
                count = 0
            
    return encrypted


def decrypt(message: str, kwd: str):
    """Decrypt messages using columnar transposition by a given key."""

    # remove spaces and create grid
    message = message.replace(" ", "")
    cols = len(kwd)
    rows = len(message) // cols
    grid = [[" "] * cols for i in range(rows)]

    # fill grid
    n = 0
    col_order = key_order(kwd)
    for j in col_order:
        for i in range(rows):
            grid[i][j] = message[n]
            n += 1
    
    # select cols in keyword order to create decrypted message
    decrypted = ""
    for i in range(rows):
        for j in range(cols):
            decrypted = decrypted + grid[i][j]
    
    return decrypted
    


encrypted = encrypt("The quick brown fox jumped over the lazy dog.", "code")
print(encrypted)
decrypted = decrypt(encrypted, "code")
print(decrypted)


