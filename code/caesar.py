import sys

def encrypt(message, k):
# Creating a list to store our encoded message
    alphalist = []
    for l in message:
        n = ord(l)
        numr = n + k 
# Using if and else statement in order to build a barrier for our code that allows us to encode
# and decode within the range from 97 through 123 no matter which K value is provided 
# which represents lowercase alphabets from a - z
        if numr > 123:
# Dividing by the remainder will ensure that we will never exceed the limits set by our barrier
            barrier = (numr - 123) % 26
            newnumr = 97 + barrier
            alpha = chr(newnumr)
            alphalist.append(alpha)
        else:
            alpha = chr(numr)
            alphalist.append(alpha)
    return alphalist

def decrypt(message, k):
    alphalist = []
    for l in message:
        n = ord(l)
        numr = n - k
        if numr < 97:
            barrier = (97 - numr) % 26
            newnumr = 123 - barrier
            alpha = chr(newnumr)
            alphalist.append(alpha)
        else:
            alpha = chr(numr)
            alphalist.append(alpha)
    return alphalist


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
