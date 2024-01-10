import sys

def encrypt(message, k):
    alphalist = []
    for l in message:
        n = ord(l)
        numr = n + k 
        if numr > 123:
            barrier = numr - 123 
            newnumr = 96 + barrier
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
        if numr < 93:
            barrier = 93 - numr
            newnumr = 123 - barrier
            alpha = chr(newnumr)
            alphalist.append(alpha)
        else:
            alpha = chr(numr)
            alphalist.append(alpha)
    return alphalist


if __name__ == "__main__":
    # take in first arg as word
    #message = sys.argv[1]
    # take in second arg as int key
    #key = int(sys.argv[2])
    message = "testing"
    key = 10

    # encrypt your word
    encrypted = encrypt(message, key)

    # decrypt your encrypted word
    decrypted = decrypt(encrypted, key)

    print("Your encrypted word is", encrypted)
    print("Your decrypted word is", decrypted)