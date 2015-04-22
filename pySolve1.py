#----------------------Helper.py--------------------------
from random import randint

from glob import iglob
import shutil
from os import listdir
import os


#print fourWords, fiveWords, sixWords

# Cows and Bulls
# Computer will guess a random (fixed-length) word from the dictionary
# user should be able to guess the word in 10 attempts
# Rules are simple
# User guesses one word for each attempt
# for each letter in correct position, computer will shout "Bull"
# for each letter but in wrong position, computer will shout "Cow"
# word has to have unique letters (ex: book, will - not allowed)


# TODO
# TODO
# TODO
# TODO
# TODO

# given a lengthy text file get words of different lengths and group them
# remove special characters, symbols etc. first

PATH = r'/Users/pavanv/Desktop/sampleTextFile.txt'
textfile = open(PATH, "rw")

possibilities = []
impossibilities = []

words = []

# given a list, remove words with repeated letters
def removeRepeatedLetteredWords(list):
    for each in list:
        for c in each:
            if each.count(c) > 1:
                list.pop(list.index(each))
                break
    return list


# group words from a text file
def groupWords(file):
    for line in file:
        for word in line.split(" "):
            if len(word) >=4 and len(word) <= 6:
                if word.isalpha():
                    words.append(word.lower()) #, len(word))

# get a random word given the length of the word
def getRandomWord(length):
    puzzle = ""
    while len(puzzle) != length:
        puzzle = words[randint(0, len(words)-1)]
    return puzzle

groupWords(textfile)
removeRepeatedLetteredWords(words)
#removeRepeatedLetteredWords(fiveWords)
#removeRepeatedLetteredWords(sixWords)

def isCowOrBull(keyword, answer):
    cows = 0
    bulls = 0
    if len(keyword) == len(answer):
        for i in range(len(keyword)):
            if answer[i] in keyword and not answer[i] == keyword[i]:
                cows += 1
            elif answer[i] == keyword[i]:
                bulls += 1
    else:
        print "please enter %d lettered word only" % len(keyword)

    print "You have %d cows and %d bulls" % (cows, bulls)

def startGame(word):
    
    attempts = 10

    while attempts > 0:
        newWord = getRandomWord(len(word))
        print newWord, word
        isCowOrBull(newWord, word)
        attempts -= 1

startGame("poised")

#-----------------------------------------------------------------------#

# print string combinations given multiple strings
# example ["abc", "def", "ghi"], output should be adg, adh, adi, aeg, aeh, aei, ...

givenList = ["abc", "def", "ghi"]

output = []

def printCombos(list):
    global output
    if len(list) == 0:
        print output
    else:
        for i in list[0]:
            output += i
            printCombos(list[1:])
            output.pop()

#printCombos(givenList)

# list files in given dir and its sub dirs

#PATH = r'/Users/pavanv/g4tcmclient/google3/googlemac/iPhone/GmailHybrid/Tests/Automation'
PATH = r'/Users/pavanv/Documents'
fileList = []
DIRS = [PATH]

def getSubDir(ROOT):

    for filename in listdir(ROOT):
        if not os.path.isfile(os.path.join(ROOT, filename)):#"." not in filename:
            DIRS.append(ROOT+"/"+filename)
            getSubDir(ROOT+"/"+filename)
    print len(DIRS)
    return

def getFilesList(dirList, extension):
    for dir in dirList:
        for filename in iglob(os.path.join(dir, extension)):
            fileList.append(filename)
    print len(fileList), fileList
    return

#getSubDir(PATH)
#getFilesList(DIRS, "*.pdf")

# Shuffle string such that no character appears twice in a row, return false if not possible

testString = "asdflijviwenfodvnweabbccddeeefffaaaaaeeedvnoeinsdvinaeeasdknsifnsadvlkndfvinwerfsdkfnasdoinwefoianflkdnivxv"

repeats = {}
result = []

for c in testString:
    repeats[c] = 0

for c in testString:
    repeats[c] += 1

AllZero = False

while not AllZero:
    for each in repeats:
        if repeats[each] > 0:
            AllZero = False
            result.append(each)
            repeats[each] -= 1
        else:
            AllZero = True


#print result
#print repeats

# Play rock/paper/scissors

#Outcome = ["Rock", "Paper", "Scissors"]

def playRPS(Player1, Player2):

    Outcome = ["Rock", "Paper", "Scissors"]
    Player1 = Outcome[randint(0,2)]
    Player2 = Outcome[randint(0,2)]

    print "Player1: %s, Player2: %s" % (Player1, Player2)
    if Player1 == Player2:
        print "Its a tie since both players got %s" % (Player2)
    elif (Player1 == "Rock" and Player2 == "Scissors") or \
        (Player1 == "Scissors" and Player2 == "Paper") or \
        (Player1 == "Paper" and Player2 == "Rock"):
        print "Player1 wins since %s beats %s" % (Player1, Player2)
    else:
        print "Player2 wins since %s beats %s" % (Player2, Player1)

# music file concatenator

from glob import iglob
import shutil
from os import listdir
import os

root = r'/Users/pavanv/Downloads/Veda Classes/Veda Classes'
#PATH = r'/Users/pavanv/Downloads/Veda Classes/Veda Classes/Achidram'
#DEST = r'/Users/pavanv/Downloads/Veda Classes/'


def getSubDir(ROOT):

    folderList = []
    for filename in listdir(ROOT):
        if not "." in filename:
            folderList.append(filename)
    return folderList

# merge all (music) files in a given folder
def mergeMusic(PATH):

    destination = open(PATH.split("/")[len(PATH.split("/"))-2]+".mp3", "wb")
    for filename in iglob(os.path.join(PATH, "*.mp3")):
        shutil.copyfileobj(open(filename, "rb"), destination)
    destination.close()
    return

# merge all subfolders into
def startMerge(ROOT):
    
    folderList = getSubDir(ROOT)
    for each in folderList:
        mergeMusic(ROOT+"/"+each+"/")

#startMerge(root)

# given a binary convert it to decimal, (vice-versa?)

def binToDec(binaryNum):

    if checkIfBinary(binaryNum):
        pos = 0
        dec = 0
        for c in str(binaryNum)[::-1]:
            dec += 2**pos*int(c)
            pos += 1
    return dec

def checkIfBinary(binaryNum):
    
    strNum = str(binaryNum)
    for c in strNum:
        if c == "0" or c == "1":
            pass
        else:
            print "Not a binary"
            return False
        return True

#print binToDec(1100)

# given a sorted array, randomize the same

sortedArray = [171, 230, 307, 404, 504, 582, 625, 660, 764, 950, 1032, 1152, 1198, 1319, 1414, 1610, 1667, 1726, 1734, 1921, 1976, 2023, 2305, 2374, 2410, 2415, 2422, 2574, 2576, 2749, 3003, 3123, 3216, 3357, 3496, 3535, 3579, 3609, 3822, 3888, 4044, 4237, 4404, 4454, 4546, 4561, 4698, 4709, 4721, 4750, 4777, 4921, 4977, 5183, 5361, 5566, 5568, 5938, 5960, 5978, 6040, 6081, 6213, 6225, 6347, 6457, 6480, 6517, 6659, 6700, 6851, 6987, 6994, 7094, 7314, 7489, 7515, 7552, 7760, 7794, 7909, 8097, 8300, 8508, 8653, 8659, 8830, 8847, 8861, 8870, 8976, 9080, 9207, 9437, 9445, 9456, 9518, 9564, 9679, 9852]

randomized = []

# given a sorted or unsorted array, randomize elements and return the list
def randomizeList(list):
    
    for each in uniqueRandList(len(list)-1):
        randomized.append(sortedArray[each])
    return randomized

# return list of unique random numbers given the range
def uniqueRandList(length):

    tempList = []
    while not len(tempList) == length:
        temp = randint(0, length)
        if temp not in tempList:
            tempList.append(temp)
    return tempList

#print randomizeList(sortedArray)



# Given array of numbers, find a pair whose sum is closest to zero

nums = [5647, 9297, 7792, 6469, 4860, 3649, 4020, 443, 7170, 2241, 2133, 927, 1942, 8883, 8083, 8805, 3355, 9785, 3642, 2052, 7585, 4043, 5809, 4085, 1508, 7457, 7107, 4401, 7045, 4558, 7452, 1310, 913, 4157, 550, 918, 1542, 7336, 9812, 3445, 8374, 4357, 2739, 8217, 7677, 9595, 6454, 7991, 2075, 7229, 3411, 5551, 2464, 3360, 9772, 4871, 2918, 5183, 8759, 9010, 9350, 1311, 4650, 754, 1952, 6651, 6356, 9015, 2790, 9059, 2330, 9294, 5831, 7193, 9381, 8236, 5888, 4512, 1691, 6094, 8824, 7059, 1605, 1482, 8030, 7865, 8523, 1275, 8877, 9940, 8521, 7418, 4160, 8153, 4385, 7578, 4585, 8674, 554, 8722]

minsum = nums[0]+nums[1]
min1 = 0
min2 = 0

for i in range(len(nums)):
    for j in range(len(nums)):
        if not i == j:
            if nums[i]+nums[j] < minsum:
                minsum = nums[i]+nums[j]
                min1 = nums[i]
                min2 = nums[j]

#print minsum, min1, min2



# Given an employee-manager dictionary, return number of employees per manager
# Employee : Manager
EmpDir = {
    "Hye" : "Sad",
    "She" : "Sad",
    "Sad" : "Gar",
    "Pav" : "Hye",
    "Nis" : "Hye",
    "Arv" : "Hye",
    "Hem" : "Hye",
    "Avn" : "Hye",
    "Yur" : "She",
    "Nic" : "She",
    "Dmi" : "She",
    "Get" : "She",
    "Mal" : "She",
    "Pri" : "She"
}

NewDir = {}

for each in EmpDir:
    NewDir[each] = 0
    NewDir[EmpDir[each]] = 0

for each in EmpDir:
    NewDir[EmpDir[each]] += 1

#print NewDir

# urllib, urllib2 et al

import urllib, urllib2, json

#print dir(json)

versionFile = open("/users/pavanv/Desktop/Test Product/PyPractice/data/ChromeHistory.txt", "r")
currentVersions = open("/users/pavanv/Desktop/Test Product/PyPractice/data/CurrentVersions.json", "r")

win = []
mac = []

for line in versionFile:
    tempList = line.split(",")
    if tempList[0] == "win":
        win.append(tempList[1:])
    if tempList[0] == "mac":
        mac.append(tempList[1:])

#print len(win), len(mac)

#print win[100]
#win.sort(key=lambda x: x[2])
#print win[100]



# An attempt at Snakes and Ladders game

from random import randrange

WinningScore = 100

Snakes = {"25" : 10, "48" :  23, "62" : 35, "84" : 17, "95" : 2}
Ladders = {"4" : 28, "30" : 66, "55" : 90, "67" : 89}

Num_Players = 5
Num_Rounds = 4

Players = []
Scores = []

def createPlayers(Num):
    global Players
    global Scores
    Players = []
    Scores = []
    
    for i in range(Num):
        Players.append("Player"+str(i+1))
    for i in range(Num):
        Scores.append(0)

def rollDice():
    return randrange(1, 6)

def snakeFall(start):
    return Snakes[start]

def ladderClimb(start):
    return Ladders[start]

def playTurn(Player, CurrentScore):
    
    TurnScore=rollDice()
    print "Player %s's turn @%d" % (Player, CurrentScore)
    TurnScore = rollDice()
    if CurrentScore+TurnScore > 100:
        pass
    else:
        CurrentScore += TurnScore
        if CurrentScore == 100:
            print "Winner is Player %s" % Player
            return CurrentScore
        elif str(CurrentScore) in Snakes:
            print "You have been bitten by a snake, you fall %d places" % (CurrentScore-Snakes[str(CurrentScore)])
            CurrentScore = Snakes[str(CurrentScore)]
        elif str(CurrentScore) in Ladders:
            print "Congratulations !! you found a ladder, you climb %d places" % (Ladders[str(CurrentScore)]-CurrentScore)
            CurrentScore = Ladders[str(CurrentScore)]
    return CurrentScore

def playGame(count, rounds):
    for r in range(rounds):
        createPlayers(count)
        Turn = Players[0]
        i = 0
        while True:
            if 100 in Scores:
                print "The final scores are: "
                print Players
                print Scores #(for i in range(len(Players): print Players[i[, Scores[i]]]))
                break
            Scores[i] = playTurn(Players[i], Scores[i])
            if i == len(Players)-1:
                i = 0
            else:
                i += 1
        print "End of Round %d " % (r+1)

#playGame(Num_Players, Num_Rounds)


#-----------------All helper functions listed below--------

# print maze

from random import randint

row = 25

def printLine():
    
    line = ""
    for i in range(100):
        j = randint(1, 100)
        if j % 2 == 0:
            line += "+"
        else:
            line += " "
    print line

for i in range(row):
    pass
    #print "+"*100
    #printLine()
    #print "+", " "*96, "+"
    #print "+", " "*96, "+"

# given the time get the angle between hour and minute hands

def calcAngle(hour, min):
    
    return abs(hour*30 - min*6)

#print calcAngle(3, 27)


# binary search an element in a given array

numList = [125, 143, 146, 154, 160, 161, 219, 237, 242, 242, 248, 255, 264, 270, 289, 313, 313, 322, 323, 339, 354, 361, 362, 376, 378, 382, 385, 394, 404, 413, 414, 442, 462, 470, 491, 491, 497, 498, 498, 510, 511, 529, 535, 543, 544, 564, 570, 573, 579, 582, 592, 605, 616, 620, 622, 642, 674, 696, 729, 735, 738, 739, 739, 743, 746, 757, 769, 769, 774, 775, 786, 790, 793, 799, 802, 844, 848, 856, 870, 875, 877, 910, 920, 925, 960, 960, 984, 990, 995]

def binSearch(list, num):

    firstHalf = list[0:len(list)/2]
    secondHalf = list[len(firstHalf):len(list)+1]
    
    #print len(firstHalf), len(secondHalf)
    #print firstHalf, secondHalf
    
    if len(list) < 2:
        if len(firstHalf) > 0:
            print firstHalf
        else:
            print secondHalf
        return
    if num in firstHalf:
        print "The key is in first half between %d and %d" % (firstHalf[0], firstHalf[len(firstHalf)-1])
        binSearch(firstHalf, num)
    else:
        print "The key is in second half between %d and %d" % (secondHalf[0], secondHalf[len(secondHalf)-1])
        binSearch(secondHalf, num)

#binSearch(numList, 799)

# Sort a given string based on order of chars in another string
from random import randint
import re
import itertools

testString = "I am not a nanny but a manny"
sortString = "ybnI"

charlist= {}

resultString = ""

for k in sortString:
    charlist[k] = ""

for c in testString:
    if c not in sortString:
        resultString += c
    else:
        charlist[c] += c

for c in sortString:
    resultString += charlist[c]

#print resultString

#check whether a given string has a palindrome

my_str1 = "I am not a nanny but a manny"
my_str2 = "malamnavanmaram"
my_newStr = ""

strArray = []

def checkPalindrome(my_str):
    global my_newStr
    #print "Given string is: " + my_str
    my_newStr = my_str[::-1]
    if my_str == my_newStr:
        return True
    else:
        return False

newStr = ""
for i in range(len(my_str2)):
    sliceStr = my_str2[i:len(my_str2)]
    for c in sliceStr:
        newStr += c
        if len(newStr) > 2:
            if checkPalindrome(newStr):
                strArray.append(newStr)
    newStr = ""

#print strArray


# return in order of occurences for a list

testArray = [0,0,100, 3, 5, 4, 6, 4, 2, 100, 2, 100]

Topper = 0
TopElement = 0
Second = 0
SecondElement = 0
count = 0

for i in range(len(testArray)):
    for j in range(len(testArray)):
        if testArray[i] == testArray[j]:
            count += 1
    if count > Topper:
        Topper = count
        TopElement = testArray[i]
    if count < Topper and Second < count:
        Second = count
        SecondElement = testArray[i]
    count = 0

#print TopElement, Topper, SecondElement, Second

# return max diff of a given list

def retMax(list):
    
    maxDiff = 0
    maxi = 0
    maxj = 0
    
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if (abs(list[i] - list[j])) > maxDiff:
                maxDiff = abs(list[i]-list[j])
                maxi = i
                maxj = j
    return list[maxi], list[maxj], maxDiff

list = [85, 55, 100, 85, 84, 95, 100, 82, 96, 94, 88, 99]

sell = retMax(list)

"""
if sell[0] > sell[1]:
    print "Short sell", sell
else:
    print "Normal sell", sell
"""
# funciton that returns a given number's factorial

factorial = 1


def fact(number):
    global factorial
    if number > 0:
        factorial *= number
        fact(number-1)

    return factorial

# funciton that returns a unique hashed list
    
def hashList(prevList, list):
    
    tempPrev = prevList[:]
    returnList = []
    
    for i in range(len(list)):

        index = randint(0, len(list)-1)
        returnList.append(list[index])
        list.pop(index)

        i += 1

    if returnList == tempPrev:
        hashList(tempPrev, returnList)
    else:
        return returnList

# Generate anagrams of a given word

def getAnagrams(word):

    wordList = []

    for c in word:
        wordList.append(c)
    
    hash = []
    tempList = []

    for i in range(fact(len(word))):
        temp = wordList[:]
        tempList = hashList(tempList, temp)
        if not tempList in hash and not len(tempList) == 0:
            #hash.append([i])
            print "".join(tempList)
            hash.append(tempList)

    print len(hash)
        
# Generate anagrams using itertools

def getAnagramsWithIterTools(string):
    
    permutations = ["".join(outcome) for outcome in itertools.permutations(string)]

    print permutations

# check if a word is anagram of another word

def isAnagram(word1, word2):
    temp = word2
    if len(word1) == len(word2):
        print "Thank God, at least they are of same length"
        i = 0
        for c in word1:
            i += 1
            if c in word2:
                word2 = word2.replace(c, "", 1)
                if len(word2) == 0:
                    print "Yup, these two words: %s and %s are anagrams" % (word1, temp)
                    break
            else:
                print "No Way are these words anagrams of each other"
                break
    else:
        print "Given words are as different as chalk and cheese, leave alone being anagrams"

# Return number of days in a calendar until the given date

monthlyDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def numDays(givenDate):
    # Date has to be in YYYY-MM-DD format only
    dateList = givenDate.split("-")
    print dateList
    
    if int(dateList[0]) % 4 == 0 and int(dateList[1]) > 2 :
        totalDays = 1
    else:
        totalDays = 0

    for i in range(int(dateList[1])-1):
        totalDays += monthlyDays[i]

    return totalDays+int(dateList[2])


#print numDays("2015-3-1")

# Print a pattern where every integer is added to its next integer and added to list


def printPattern(start, end, list):

    if start == end:
        return

    newList = [1]
    newList.insert(len(newList), 1)

    for i in range(len(list)-1):
        newList.insert(i+1, list[i]+list[i+1])

    print list
    start += 1

    printPattern(start, end, newList)


list = [1]
#print printPattern(0, 10, list)

# Print number of atoms given the chemical formula

def printAtoms(chemicalFormula):
    
    print chemicalFormula
    atomList = {}
    count = 0
    
    for c in chemicalFormula:
        if c.isalpha():
            atomList[c] = 0

    for c in chemicalFormula:
        if c.isalpha():
            atom = c
            atomList[c] += 1
        else:
            atomList[atom] += int(c)-1

    print atomList

#printAtoms("NH3OH2CH2")




