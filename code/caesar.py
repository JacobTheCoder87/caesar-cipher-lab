import sys

def encrypt(message, k):
    for l in message:
        n = ord(l)
        numr = n + k 
        if numr > 123:
            barrier = numr - 123 
            newnumr = 96 + barrier
    alpha = chr(n)
    return alpha


def decrypt(message, k):
    for l in message:
        n = ord(l)
        numr = n - k
        if numr  < 
    return alpha


if __name__ == "__main__":
    # take in first arg as word
    message = sys.argv[1]
    # take in second arg as int key
    key = int(sys.argv[2])

    # encrypt your word
    encrypted = encrypt(message, key)

    # decrypt your encrypted word
    decrypted = decrypt(encrypted, key)

    print("Your encrypted word is", encrypted)
    print("Your decrypted word is", decrypted)