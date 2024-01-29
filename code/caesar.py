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
# By using the modulous operator we are returning the remainder of (numr- 123) / 26. This way we
# will ensure that our newnumr will never exceed over 123 when given an arbitarily large key value.
            barrier = (numr - 123) % 26
            newnumr = 97 + barrier
            alpha = chr(newnumr)
            alphalist.append(alpha)
        else:
            alpha = chr(numr)
            alphalist.append(alpha)
# Writing a join function with no spaces to make sure that I am joining each variable of my list together. Ultimately
# we want to input a string and return a string for our output as well
    output_list = ''.join(alphalist)
    return output_list

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
    output_list = ''.join(alphalist)
    return output_list


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
