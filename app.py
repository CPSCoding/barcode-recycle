import binascii

plaintext = raw_input("Enter message: ")
key = raw_input("Enter key: ")

plaintextArray = []
plaintextvalues = []

#convert plaintext into binary
for letter in plaintext:
    plaintextArray.append(bin(int(binascii.hexlify(letter), 16)))

#gives plaintext ascii value
for item in plaintextArray:
    plaintextvalues.append(int(item,2))


keyArray = []
threekeyArray = []
keyValues=[]

#turns binary into an array
number = 0
for letter in key:
    keyArray.append(bin(int(binascii.hexlify(letter), 16)))
    twokeyArray = []
    for x in keyArray[number]:
        if x != "b":
            twokeyArray.append(x)
    number += 1
    threekeyArray.append(twokeyArray)

#adds the value of bits depending on location
for array in threekeyArray:
    total = 0
    num = 8
    for place in array:
        place = int(place)
        if place == 1:
            total += num
        num -= 1
    keyValues.append(total)


keylength = len(key)
plaintextlength = len(plaintext)

cipherArray = []
keycounter = 0
plaintextcounter = 0

#gives us the ciphertext
for i in plaintextvalues:
    while plaintextcounter < plaintextlength:
        popo = plaintextvalues[plaintextcounter]
        if keycounter >= keylength:
            keycounter = 0
        j = keyValues[keycounter]
        j = int(j)
        keycounter += 1
        plaintextcounter += 1
        cipherArray.append(popo + j - 19)

for i in cipherArray:
    i = int(i)


#prints the ciphertext
cipherString = ""
for char in cipherArray:
    if char < 32:
        char += 32
        char = chr(char)
        cipherString += ("abcde%s" %char)
    else:
        cipherString += chr(char)

print ("Ciphertext: %s" %cipherString)
