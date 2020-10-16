


#Import ciphertext
encoding = "utf-8"
f = open('Group9_ciphertext-1.txt', encoding=encoding)
file = f.readlines()

#Clean up imported data
binList = []
hexList = []
for line in file:
    chunks = line.split("|")                                    #List of each 8-term hex segment
chunks = [term.strip(" ") for term in chunks]
for hexTerm in chunks:
    hexTerms = hexTerm.split(" ")
    for term in hexTerms:
        hexList.append(term)                                    #List of each term in hex
        binList.append(bin(int(term, 16)).zfill(8)[2:])         #List of each term in binary



