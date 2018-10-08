import string

def createDictionary(textFile):
    # i = first letter of word
    # j = last letter of word
    for i in string.ascii_lowercase:
        for j in string.ascii_lowercase:
            with open(textFile,'r') as ins:
                array = []
                for line in ins:
                    #only write entry if it starts and ends with correct letter
                   # if (line.startswith(i) and line.endswith(j+"\n") and len(line)>= 6):
                   array.append(line)
            f = open(i+j+".txt","w")
            f.writelines(array)
            f.close()
            ins.close()
    print("-done creating dictionary-")

def searchDictionary(inputString):
    array = []
    with open(inputString[0]+inputString[len(inputString)-1]+".txt",'r') as ins: #opens "qn.txt" for example if input string is "QIEIN". Its the organized dictionary from above
        for line in ins:
            temporaryInputString = inputString
            place = 0
            letterCount = 1
            doubleLetterUsed = 0
            for letter in line:
                if place >= 0: #place will be -1 if it is unable to find it
                    place = temporaryInputString.find(letter)
                    if doubleLetterUsed == 2:
                        temporaryInputString = temporaryInputString[place+1:]
                    else:
                        temporaryInputString = temporaryInputString[place:]
                        if place == 0:
                            doubleLetterUsed = doubleLetterUsed +1
                    letterCount = letterCount + 1
                    if letterCount == len(line): #effectively ignores the newline text at end...
                        array.append(line)
    print(array)
    return array

createDictionary("dictionnaire.txt")
searchDictionary('resoetp')