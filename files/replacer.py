#! /usr/bin/env python3

# read in file, store text in string variable, print on screen

#problem - will replace substrings part of words too. Ex VERB in ADVERB - solved using reokace_diff function
#problem - cannot pinpoint specific occurence of word and replace it  

# return occurences of word in text
def occurences(text,word):
    count = 0
    for yo in text.split():
        if yo == word:
            count += 1
    return count





def replace_diff(text,word,replacement,diff=1):
    
    count = 0
    spl=text.split()
    for yo in spl:
        if yo == word:
            spl[spl.index(yo)] = replacement
            if diff == 1:
                break
    print(spl)
    return ' '.join(spl)

    








path1 = input("Provide path of file to be read in ")
mlFile = open(path1)
mlContent = mlFile.read()
print('Text from the file is:\n' + mlContent)

mlContent = mlContent.replace("."," .")

while True:
    k = input("Which word would you like to replace?\n")
    occ = occurences(mlContent, k)
    print("There were " + str(occ) + " occurences found in the text")
    y = input("Would you like to replace all the occurences with different words? (y/n)\n")
    if is.lower(y) == 'n':
        rep = input("What would you like to replace it with?\n")
        mlContent = replace_diff(mlContent,k,rep,0)
    else:
        for i in range(occ):
            lo = input("Enter replacement for occurence "+ str(i+1) + " of " + k + "\n")
            
            mlContent = replace_diff(mlContent,k,lo,i+1)

    y1=input("Would you like to replace more words? (y/n)\n")
    if is.lower(y1) == 'n':
        break

mlContent = mlContent.replace(" .", ".")

print("The result is")
print(mlContent)

