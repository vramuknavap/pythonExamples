
import helper
import sys, time, os
from random import randint, randrange

# input a long sentence with several words. output words ranked by number of occurances.
# if more than one word appears same number of times, sort them alphabetically

longSentence = "Google is an American multinational corporation specializing in Internet-related services and products. These include online advertising technologies, search, cloud computing, and software.[8] Most of its profits are derived from AdWords,[9][10] an online advertising service that places advertising near the list of search results. Google was founded by Larry Page and Sergey Brin while they were Ph.D. students at Stanford University. Together they own about 14 percent of its shares but control 56 percent of the stockholder voting power through supervoting stock. They incorporated Google as a privately held company on September 4, 1998. An initial public offering followed on August 19, 2004. Its mission statement from the outset was to organize the world's information and make it universally accessible and useful,[11] and its unofficial slogan was Don't be evil.[12][13] In 2004, Google moved to its new headquarters in Mountain View, California, nicknamed the Googleplex.[14] Rapid growth since incorporation has triggered a chain of products, acquisitions and partnerships beyond Google's core search engine. It offers online productivity software including email (Gmail), a cloud storage service (Google Drive), an office suite (Google Docs) and a social networking service (Google+). Desktop products include applications for web browsing, organizing and editing photos, and instant messaging. The company leads the development of the Android mobile operating system and the browser-only Chrome OS[15] for a netbook known as a Chromebook. Google has moved increasingly into communications hardware: it partners with major electronics manufacturers[16] in the production of its high-quality low-cost[17] Nexus devices and acquired Motorola Mobility in May 2012.[18] In 2012, a fiber-optic infrastructure was installed in Kansas City to facilitate a Google Fiber broadband service.[19] The corporation has been estimated to run more than one million servers in data centers around the world (as of 2007);[20] and to process over one billion search requests,[21] and about 24 petabytes of user-generated data, each day (as of 2009).[22][23][24][25] In December 2013 Alexa listed google.com as the most visited website in the world. Numerous Google sites in other languages figure in the top one hundred, as do several other Google-owned sites such as YouTube and Blogger.[26] Its market dominance has led to prominent media coverage, including criticism of the company over issues such as search neutrality, copyright, censorship, and privacy.[27][28]"


words = longSentence.split(" ")
for word in words:
    if "[" in word:
        words.pop(words.index(word))

wordList = {}

for word in words:
    wordList[word.upper()] = 0

for word in words:
    wordList[word.upper()] += 1

print wordList

# given a 2d array, display the transpose

def addZeros(list):
    maxRow = 0
    minRow = len(list[0])
    
    for row in list:
        if len(row) > maxRow:
            maxRow = len(row)
        if len(row) < minRow:
            minRow = len(row)

    for row in list:
        if len(row) < maxRow:
            for i in range(maxRow-len(row)):
                row.append(0)

    return list


list = [[1, 2, 3, 4],
        [5, 6, 7, 8, 9],
        [9, 10, 11, 12],
        [13, 14, 15, 16],
        [1],
        [2, 3],
        ["a", "b", "c", "d", "e", "f", "g", "i", "k", "l"]]

cols = len(list)
rows = len(max(list))

print "Original matrix is"
for each in list:
    print each

addZeros(list)

print "Adjusted Matrix is"
for each in list:
    print each

newRow = []
newList = []

for i in range(rows):
    for j in range(cols):
        newRow.append(list[j][i])
    newList.append(newRow)
    newRow = []

print "Transposed matrix is"
for each in newList:
    print each

# Given the 2d list, print combinations

"""
    example: [[1,5], [2], [3,4,6]]
    output: [1, 2, 3] [1, 2, 4] [1, 2, 6] [5, 2, 3] [5, 2, 4] [5,2, 6]
"""

list = [[1], [2,3,4,5,6,7,8,9], [3,4], [1,2,3] ,[4,5,6,7]]

to_print = []

def printCombos(list):
    if len(list) == 0:
        print to_print
    else:
        for i in list[0]:
            to_print.append(i)
            printCombos(list[1:])
            to_print.pop()

#printCombos(list)

# chess board cells

Columns = ["A", "B", "C", "D", "E", "F", "G", "H"]
Rows = ["1", "2", "3", "4", "5", "6", "7", "8"]

eachLine = []
chessBoard = []

for c in Columns:
    for r in Rows:
        eachLine.append(c+r)
    chessBoard.append(eachLine)
    eachLine = []

#for row in chessBoard:
#    print row

# bunch of list helper functions

def getRandomList(startRange=0, endRange = 100, listSize = 100):
    return ([randrange(startRange, endRange) for x in range(listSize)])

def removeDupes(list):
    tempList = []
    for i in range(len(list)):
        if list[i] not in tempList:
            tempList.append(list[i])

    return sorted(tempList)

#print removeDupes(getRandomList(100, 200, 300))

# check if two given strings are Anagrams

first = "secudre"
second = "rescdue"


def sortString(string):
    tempStr = []
    for s in string:
        if not s == " ":
            tempStr.append(s.lower())
    tempStr.sort()
    return "".join(tempStr)

def areAnagrams(first, second):
    if sortString(first) == sortString(second):
        print "Yes"
    else:
        print "No"

#areAnagrams(first, second)

# A game where both players start with a score of 100. Each dice roll value is deducted from their scores.
# Who reaches 0 first will be the winner.


def playGame():

    PlayerA = 100
    PlayerB = 100

    Turn = "A"


    while True:
        
        #print PlayerA, PlayerB

        if Turn == "A":
            tempScore = PlayerA
            PlayerA -= randint(1, 6)
            if PlayerA < 0:
                print "you can't hit below 0"
                PlayerA = tempScore
            Turn = "B"
        if Turn == "B":
            tempScore = PlayerB
            PlayerB -= randint(1, 6)
            if PlayerB < 0:
                print "you can't hit below 0"
                PlayerB = tempScore
            Turn = "A"
        
        if PlayerA == 0:
            print "The winner is Player A"
            break
        if PlayerB == 0:
            print "The winner is Player B"
            break

#playGame()

# Find second most repeating number in an array

numArray = [randrange(100, 110) for x in range (1000)]

countDict = {}

for n in range(len(numArray)):
    countDict[numArray[n]] = numArray.count(numArray[n])

counts = removeDupes(countDict.values())
#print counts[len(counts)-2]

# Take alphanumeric as input and show sum of digits as output
"""
    example: "asdf900sdf22sdfsef23sdfsdf2sdf9sfd9sdf9"
    output: 9+22+23+2+9+9+9
"""

givenStr = "asdf900sdf2a2sdfsef222baaa333sdfsdf2sdf9sfd9sdf9"
numbers = ["1","2","3","4","5","6","7","8","9","0"]

sum = 0
prev = ""
i = 0

for c in givenStr:
    i += 1
    if c in numbers:
        prev += c
    if (not c in numbers or i == len(givenStr)) and not prev == "":
        sum += int(prev)
        prev = ""

#print sum

# Given an array, print range of numbers
"""
    example: [1,2,3,9,10, 14, 22, 23, 40, 41, 42]
    output should be "1-3, 9-10, 14, 22-23, 40-42"
"""

#numList = [1,2,3,9,10, 14, 22, 23, 40, 41, 42]
numList = [125, 143, 146, 154, 160, 161, 219, 237, 238, 239, 242, 248, 255, 264, 270, 289, 313, 322, 323, 324, 325,  339, 354, 361, 362, 376, 378, 382, 385, 394, 404, 413, 414, 442, 462, 470, 491, 491, 497, 498, 498, 510, 511, 529, 535, 543, 544, 564, 570, 573, 579, 582, 592, 605, 616, 620, 622, 642, 674, 696, 729, 735, 738, 739, 740, 741, 742, 743, 746, 757, 769, 769, 774, 775, 786, 790, 793, 799, 802, 844, 848, 856, 870, 875, 877, 910, 920, 925, 960, 960, 984, 990, 995]

result = []
rangeStr = ""
temp = None

result.append(str(numList[0]))

for i in range(len(numList)-1):
    if numList[i]+1 == numList[i+1]:
        temp = numList[i+1]
    if (i+1 == len(numList)-1 or not numList[i]+1 == numList[i+1]) and not temp == None:
        result += "-"
        result += str(temp)
        temp = None
    if not numList[i]+1 == numList[i+1] and temp == None:
        result += ","
        result += str(numList[i+1])

#print " ".join(result)

# A tial to see if a mathematical expression can be put into a tree

expression = "(3+(4*5))"

numbers = ["0","1","2","3","4","5","6","7","8","9"]
operators = ["+", "-", "*", "/"]

list = []

for c in expression:
    if c == "(":
        list.insert(0, c)
    if c == ")":
        list.insert(len(list), c)
    if c in numbers:
        list.append(c)
    if c in operators:
        list.append(c)

#print list


#-------------using sys, os commands-----------------------
# note that no actual backup has been implemented----------
"""
    
backup_from = ['/Users/pavanv/Desktop/']
backup_to = '/Users/pavanv/bkDesktop'

target_dir = backup_to + "_" + time.strftime('%Y%m%d%H%M%S') + ".zip"

if not os.path.exists(target_dir):
    os.mkdir(target_dir)

dir_command = "ls -latr"


if os.system(dir_command) == 0:
    print "Ran \"{}\" command successfully".format(dir_command)
else:
    print "Failed to run this command {}",format(dir_command)

"""
#------just call helper function to get anagrams of a given string-----
"""

helper.isAnagram("Paven", "navaP")
helper.getAnagramsWithIterTools("Pavan")

"""
#-----------------another dir example--------------------------------------
"""

i = 0
subCommands = []

def direct(command):
    global subCommands
    for each in dir(command):
        subCommands.append(command.__name__+ "." + str(each))
    return subCommands

print direct(re)
"""
#--------get words from a sentence and change their case------------------
"""
import re

def getWords(sentence):

    wordList = re.split("\W+", sentence)
    newWord = []

    for word in wordList:
        for c in word:
            if c.islower():
                newWord.append(c.upper())
            else:
                newWord.append(c.lower())
        print word, ''.join(newWord)
        newWord = []

    return wordList

print getWords("This IS a vERY lOnG stRiNG With LoT oF words in it for testing purposes")
"""
#-------Tree traversals----------------
"""
from TreeClass import Node

AnimaList = ["Animalia", "Chordate", "Arthropoda", "Mammal", "Insect", "Primate", "Carnivora", "Diptera", "Hominidae", "Pongidae", "Felidae", "Muscidae", "Homosapiens", "Pan", "Felis", "Musca", "Sapiens", "Troglodytes", "Domestica", "Leo", "Domestica", "Human", "Chimpanzee", "House Cat", "Lion", "Housefly"]

HTMList = ["html", "head", "meta", "title", "body", "ul", "li", "h1", "h2", "p", "a", "div"]

Expression = "(7+3)*(5-2)"

left = "("
operators = [1,2,3,4,5,6,7,8,9,0]
operands = ["+", "-", "/", "*"]
right = ")"

Tree = []

root  = Node("root")
for each in Expression:
    if each == left:
        root.addLeft(each)
    if each == right:
        root.addRight(each)
    if each in operands:
        root.addRight(root)
        root.setRootName(str(each))
    if each in operands:
        root.setRootName(str(each))
"""

#-------parse Tree (mathematical expression)---------
"""
left = "("
operators = [1,2,3,4,5,6,7,8,9,0]
operands = ["+", "-", "/", "*"]
right = ")"

emptyTree = []

"""

#--------circular list - hot potato-----------------
"""
passList = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

i = 0
count = 3

while len(passList) > 1:
    for j in range(count):
        temp = passList[0]
        passList.remove(passList[0])
        passList.append(temp)
        
        j += 1
        
        if j == count:
            passList.remove(passList[0])


    print passList
    i += 1
    if i == len(passList)-1:
        i = 0
"""
#-------hot potato---------------------
"""
def hotPotato(list, count):

    while len(list) > 1:
        temp = None

        for i in range(count):

            temp = list[0]
            list.remove(list[0])
            list.append(temp)
            
            
            if i == count:
                list.remove(list[i])
            i += 1

        list.remove(list[0])

        print list

        hotPotato(list, count)

passList = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

hotPotato(passList, 7)
"""
#-------print a tree-----------
"""
myTree = ['a', ['b', ['d',[],[]], ['e',[],[]] ], ['c', ['f',[],[]], []] ]

print(myTree)

"""

#-----reverse the vowels--------------
"""
Vowels = [ 'a', 'e', 'i', 'o', 'u']
GivenString = "This is a cat with a hat and sleeping"
strToArray = []
indices = []
chars = []


for i in range(len(GivenString)):
    strToArray.append(GivenString[i])
    if GivenString[i] in Vowels:
        indices.append(i)
        chars.append(GivenString[i])

j = len(chars)-1
for i in indices:
    strToArray[i] = chars[j]
    j -= 1

print "".join(strToArray)

"""
#--------Big O - simple example-----------
"""
import thread
import time
from random import randrange
    
def findMinLong(aList):
    start = time.time()
    smallest = aList[0]
    for i in aList:
        foundSmallest = True
        for j in aList:
            if i > j:
                foundSmallest = False
        if foundSmallest:
            smallest = i
    end = time.time()
    print "findMinLong... " + str(smallest) + "," +  str(end-start)


def findMinShort(aList):
    start = time.time()
    smallest = aList[0]
    for i in aList:
        if i < smallest:
            smallest = i
    end = time.time()
    print "findMinShort... " + str(smallest) + "," +  str(end-start)


for listSize in range(1000, 10001, 1000):
    aList = [randrange(10000, 100000) for x in range(listSize)]
    try:
     thread.start_new_thread(findMinShort, (aList,))
    #thread.start_new_thread(findMinShort, (aList, ))
    except:
        print "Error: couldn't create thread"
#print ("size: %d time: %f" % (listSize, end-start))
    
"""

#--------------bubble sort------------------------
"""
    my_list = [100, 99, 22, 102, 88, 124, 97, 7, 72, 56, 43, 53, 36]
    
    def bubbleSort(my_list):
    for i in range(len(my_list)-1):
    for j in range(len(my_list)-1):
    if my_list[j] > my_list[j+1]:
    temp = my_list[j]
    my_list[j] = my_list[j+1]
    my_list[j+1] = temp
    return my_list
    
    print bubbleSort(my_list)
"""
#-------------utilities--------------------
"""
import sys, os, urllib, unittest

# path, filename, dirlist etc.
for each in os.listdir("../"):
    pass
    #print os.path.dirname(os.path.abspath(each))
    #print os.path.basename(each)
    #print os.path.abspath(each)

# urllib - urlopen(url)
print dir(urllib.urlopen)
google = open("GoogleHomePage.html", "w+")

webfile = urllib.urlopen("http://www.google.com")
print webfile.info()
print webfile.geturl()

# unittest
print dir(unittest.TestCase)
"""
#--------regex - 2------------------------
"""
import re, sys

try:
    newF = open("/ussers/pavanv/Desktop/Test Product/NewNames.txt", "r")
#raise IOError
except:
    e = sys.exc_info()
    print "...in except block..."
    print e[0]
    print "Seems like the file doesn't exist"
else:
    print "....executing actual code...."
    for line in newF:
        if re.findall("(\$\w+\@)", line):
            print line
finally:
    print "....in finally...."

"""
#--------regex - 1 ------------------------
"""
from random import randint
import re

f = open("names.txt", "r+")
newF = open("/users/pavanv/Desktop/Test Product/NewNames.txt", "w+")
newNames = []

specialChars = ["#", "$", "%", "^", "&", "*", "@", "123", "456", " "]

for line in f:
    names = line.split(",")

for name in names:
    print name

for line in names:
    newName = ""
    for c in line:
        newName += c
        if len(newName) < len(line):
            newName += specialChars[randint(0, len(specialChars)-1)]
    newNames.append(newName)
    newF.write(newName)
    newF.write("\n")

#for each in newNames:
#    print each

f.close()
newF.close()
newF = open("/users/pavanv/Desktop/Test Product/NewNames.txt", "r")

for line in newF:
    if re.search("\@", line):
        print line
"""
#-----------Dict object ----------------
"""
eleDict = {'food1': [['name', 'Strawberry Belgian Waffles'], ['price', '$7.95'], ['description', 'Light Belgian waffles covered with strawberries and whipped cream'], ['calories', '900']], 'food0': [['name', 'Belgian Waffles'], ['price', '$5.95'], ['description', 'Two of our famous Belgian Waffles with plenty of real maple syrup'], ['calories', '650']], 'food3': [['name', 'French Toast'], ['price', '$4.50'], ['description', 'Thick slices made from our homemade sourdough bread'], ['calories', '600']], 'food2': [['name', 'Berry-Berry Belgian Waffles'], ['price', '$8.95'], ['description', 'Light Belgian waffles covered with an assortment of fresh berries and whipped cream'], ['calories', '900']], 'food4': [['name', 'Homestyle Breakfast'], ['price', '$6.95'], ['description', 'Two eggs, bacon or sausage, toast, and our ever-popular hash browns'], ['calories', '950']]}

i = 0
j = 0
for element in eleDict:
    for i in range(len(eleDict[element])):
        for j in range(len(eleDict[element][i])):
            print eleDict[element][i][j]

    print "###########################"

print map(hash, eleDict)

"""
#---xml practice, ignore--------
"""
from xml.dom import minidom
import xml.etree.ElementTree as ET

tree = ET.parse('/Users/pavanv/Desktop/simple.xml')

root = tree.getroot()

print root.tag

for item in root:
    for i in item:
        pass #print i.tag, i.attrib, i.text

#print dir(root)

xmldoc = minidom.parse('/Users/pavanv/Desktop/simple.xml')
itemlist = xmldoc.getElementsByTagName('food')



for i in itemlist:
    print i.findall("name")
    break

#print i.attributes.keys.__dict__)

"""
#--------OS and forking---------------
"""
import os

def child():
    print 'A new child ',  os.getpid( )
    os._exit(0)

def parent():
    i = 0
    while i < 10:
        newpid = os.fork()
        if newpid == 0:
            child()
        else:
            pids = (os.getpid(), newpid)
            print "parent: %d, child: %d" % pids
        i += 1


parent()
"""
#------Factorial--------------
"""
total = 1

def fact(number):
    global total
    if number > 0:
        #print "till now.. " + str(number) + " * " + str(total) + " = "
        total *= number
        print "*"*number
        fact(number-1)

fact(10)

def printStar(number):
    for i in range(1, number):
        print " "*(number/i) + "*"*i + " "*(number/i)

printStar(10)
"""
#------Towers of Hanoi and recursion--------------
"""
firstPole = sorted([8,7,4,2,1,9,6,3,5], reverse=True)
secondPole = []
thirdPole = []

print firstPole, secondPole, thirdPole



def switch(n, source, helper, target):
    #check if source has any pegs at all first
    if n > 0:
        #move tower of size n-1 to helper
        switch(n-1, source, target, helper)
        #move largest/last disc from source to target
        if source:
            target.append(source.pop())
        #move tower of size n-1 from helper to target
        switch(n-1, helper, source, target)

switch(len(firstPole), firstPole, secondPole, thirdPole)

print firstPole, secondPole, thirdPole

"""

#-------import modules-------
"""

#from classWork import Stack, SpecialStack

import re

print dir(re)

freshStack = Stack()
print freshStack.items
print dir(freshStack)

freshStack = SpecialStack()
print freshStack.items
print dir(freshStack)

name = open("names.txt", "r")
names = name.read().split(",")

newNames = open("NewNames.txt", "r+")

for each in names:
    print re.sub("[A-Z]", "*", each.lower())
    newNames.write(each.lower())
    newNames.write("\n")

for line in newNames:
    print line

print newNames.mode
print newNames.name
print name.name
print newNames.closed
print name.closed

newNames.close()
name.close()
    """

#-------------------------------------------
"""
list = [1,2,3,4,5,6,7,8,9,0]

class MyList:

    def __init__(self, list):
        self.myList = list

    def __pop__(self, item):
        print item

newList = MyList(list)
newList.__pop__(list)

list.pop(0)

print list
    

"""
#--------special matrix ------------
# 1st row and column should have 1, rest are different
"""
Matrix = []

for i in range(10):
    Matrix.append([])
    for j in range(10):
        if i == 0 or j == 0:
            Matrix[i].append(1)
        else:
            Matrix[i].append((i-1)*j + i*(j-1))


for row in Matrix:
    print row

#------------two arrays of different sizes------------
from random import randint

Gard = []
Grid = []

for i in range(0, 20):
    Grid.append([])
    for j in range(0, 20):
        Grid[i].append(randint(10, 99))

for row in Grid:
    print row

for i in range(0, 25):
    Gard.append([])
    for j in range(0, 25):
        Gard[i].append(randint(100,999))

for each in Gard:
    print each

"""
#-----------------------grid-top-left-to-bottom-right-------------------
"""
from random import randint
    
Grid = []
TopLeft = [0,0]
TopRight = [0, 20]
BottomLeft = [20, 0]
BottomRight = [20, 20]
    
for i in range(0, 20):
    Grid.append([])
    for j in range(0, 20):
        Grid[i].append(randint(10, 99))
    
for row in Grid:
    print row
    
"""
#--------logging in python------------------
"""
import logging

#print  dir(logging)

logger = logging.getLogger("In logging module")
logger.setLevel(logging.WARN)

stream = logging.StreamHandler()
stream.setLevel(logging.WARN)
formatter = logging.Formatter(\
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s")

stream.setFormatter(formatter)
logger.addHandler(stream)

logger.debug("debug message")
logger.info("info message")
logger.warn("warn message")
logger.error("error message")
logger.critical("critical message")

"""
#-------Get primes below 1000--------------
"""
Prime = [2]

for i in range(3, 1000):
    for j in range(2, 999):
        if i % j == 0:
            break
        elif j == i-1:
            Prime.append(i)

for each in prime:
    for c in str(each):

"""
#--------factorial equals sum of digit factorials---------
"""
def fact(number):
    product = 1
    for i in range(number, 1, -1):
        product *= i
    return product

def factDigits(number):
    sum = 0
    for c in str(number):
        sum += fact(int(c))
    return sum

for i in range(3, 100000):
    if factDigits(i) == i:
        print i

print fact(4)+fact(5)*2+fact(8)+fact(0)
"""
#----------sum of power of 5s----------------------
"""
sum = 0
foundList = []

for i in range(2, 1000000):
    for digit in str(i):
        sum +=  (int(digit)**5)
    if sum == i:
        foundList.append(i)
    sum = 0

print foundList
print (5**5+4**5+7**5+8**5+4**5)
"""
#----------remove duplicates-----------------------
"""
numbers = [43, 37, 28, 54, 71, 27, 99, 82, 87, 33, 18, 81, 63, 18, 41, 65, 12, 84, 57, 11, 10, 36, 18, 27, 98, 21, 93, 86, 87, 78, 54, 33, 38, 88, 58, 13, 56, 96, 97, 11, 97, 39, 15, 23, 87, 86, 40, 55, 69, 25, 69, 96, 71, 83, 64, 24, 82, 51, 60, 58, 66, 94, 47, 18, 89, 42, 50, 27, 75, 37, 90, 42, 40, 54, 90, 15, 16, 47, 71, 44, 82, 22, 39, 83, 97, 24, 89, 74, 20, 92, 65, 63, 61, 20, 24, 21, 96, 49, 20, 54]

temp = []
duplicates = []

for i in range(len(numbers)):
    if not numbers[i] in temp:
        temp.append(numbers[i])
    else:
        if not numbers[i] in duplicates:
            duplicates.append(numbers[i])

print numbers
print temp

print str((len(numbers)-len(temp))) + " duplicates found and those are:"
print duplicates

"""
#-----------------1000 digit Fibonnaci------------------------
"""
Fib = [0,1]
i = 2
while (len(str(Fib[len(Fib)-1])) < 1000):
    i += 1
    Fib.append(Fib[i-2]+Fib[i-3])

print Fib[len(Fib)-1]
"""
#------------lexicographic order------------------------
"""
from random import randint
number = [0,1,2,3,4,5,6,7,8,9]
temporary = []
temp = []
count = 0
string = ""

while count < 100000:
    count += 1
    while len(temp) < 10:
        j = number[randint(0,9)]
        if j not in temp:
            temp.append(j)
    for i in temp:
        string += str(i)
    temporary.append(string)
    temp = []
    string = ""

print temporary
"""
#--------------------Perfect/abundant/deficient numbers---------------
"""
def getDivisors(number):
    divisors = []
    for i in range(1, number-1):
        if number % i == 0:
            divisors.append(i)
    return divisors

divisorList = getDivisors(28)

def isPerfect(number):
    sum = 0
    divisorList = getDivisors(28)
    for i in divisorList:
        sum += i
    if sum == number:
        print "Perfect Number"
    elif sum > number:
        print "Deficient"
    elif sum < number:
        print "Abundant"

isPerfect(12)
"""
#--------------alphabet-score---------------------
"""
from random import randint

Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

AlphaValues = {}

for i in range(len(Alphabet)):
    AlphaValues[Alphabet[i]]  = i+1

print AlphaValues.keys(), AlphaValues.values()

totalSum = 0
def getTotal(sno, name):
    global totalSum
    if not "\"" in name:
        print name
        sum = 0
        for c in (name).upper():
            #print c, AlphaValues[c]
            sum += AlphaValues[c]

        print name, sum*sno
        totalSum += sum*sno

name = open("names.txt", "r+")

names = name.read().split(",")


i = 0
for each in names:
    i += 1
    getTotal(i, each.strip("\""))

print totalSum

name.close()
"""
#-------sum of digits in 100 factorial-------------
"""
product = 1
sum = 0

for i in range(100, 1, -1):
    product *= i

for c in str(product):
    sum += int(c)

print product
print sum
"""
#----------sum of digits from 2 to the power of 1000-------------
"""
number = str(2**1000)
Total = 0

for c in number:
    Total += int(c)

print Total
"""

#---------------sum of 1st 10 numbers of sum of the below list-----------
"""
numbers = {
37107287533902102798797998220837590246510135740250,
46376937677490009712648124896970078050417018260538,
74324986199524741059474233309513058123726617309629,
91942213363574161572522430563301811072406154908250,
23067588207539346171171980310421047513778063246676,
89261670696623633820136378418383684178734361726757,
28112879812849979408065481931592621691275889832738,
44274228917432520321923589422876796487670272189318,
47451445736001306439091167216856844588711603153276,
70386486105843025439939619828917593665686757934951,
62176457141856560629502157223196586755079324193331,
64906352462741904929101432445813822663347944758178,
92575867718337217661963751590579239728245598838407,
58203565325359399008402633568948830189458628227828,
80181199384826282014278194139940567587151170094390,
35398664372827112653829987240784473053190104293586,
86515506006295864861532075273371959191420517255829,
71693888707715466499115593487603532921714970056938,
54370070576826684624621495650076471787294438377604,
53282654108756828443191190634694037855217779295145,
36123272525000296071075082563815656710885258350721,
45876576172410976447339110607218265236877223636045,
17423706905851860660448207621209813287860733969412,
81142660418086830619328460811191061556940512689692,
51934325451728388641918047049293215058642563049483,
62467221648435076201727918039944693004732956340691,
15732444386908125794514089057706229429197107928209,
55037687525678773091862540744969844508330393682126,
18336384825330154686196124348767681297534375946515,
80386287592878490201521685554828717201219257766954,
78182833757993103614740356856449095527097864797581,
16726320100436897842553539920931837441497806860984,
48403098129077791799088218795327364475675590848030,
87086987551392711854517078544161852424320693150332,
59959406895756536782107074926966537676326235447210,
69793950679652694742597709739166693763042633987085,
41052684708299085211399427365734116182760315001271,
65378607361501080857009149939512557028198746004375,
35829035317434717326932123578154982629742552737307,
94953759765105305946966067683156574377167401875275,
88902802571733229619176668713819931811048770190271,
25267680276078003013678680992525463401061632866526,
36270218540497705585629946580636237993140746255962,
24074486908231174977792365466257246923322810917141,
91430288197103288597806669760892938638285025333403 }

new =  sorted(numbers)

sum = 0
for n in new:
    sum = sum+n

print str(sum)
count = 10
total = 0

for c in str(sum):
    total += int(c)
    count -= 1
    if count == 0:
        break

print total

"""
#------------Print triangle numbers--------------------------------
"""
sum = 1

triangle = []
for i in range(1, 100):
    for j in range(1, i):
        sum += j
    triangle.append(sum)
    sum = 0
print triangle
"""
#------Generate 20x20 grid-----------------------------------------
"""
from random import randint

grid = []

for i in range(22):
    grid.append([])
    for j in range(22):
        grid[i].append(randint(10,99))

for row in grid:
    print row
"""

#----------Pythagorean triplet for which a + b + c = 1000-----------------------------

"""
singles = []

for i in range(1000):
    singles.append(i)

for i in singles:
    for j in singles:
        for k in singles:
            if i < j and j < k:
                if i+j+k == 1000:
                    if (i*i + j*j) == k*k:
                        print i, j, k
print 200*200, 375*375, 425*425

"""


#---------------------------------------
#Prime numbers below 10000
"""
Prime = [2]

for i in range(3, 10000):
    for j in range(2, 9999):
        if i % j == 0:
            break
        elif j == i-1:
            Prime.append(i)

print Prime
print len(Prime)

"""

#-----------Palindrome-------------------------
#check whether a given string is a palindrome
"""
my_str1 = "I am not a nanny but a manny"
my_str2 = "malayalam"
my_newStr = ""

def checkPalindrome(my_str):
    global my_newStr
    print "Given string is: " + my_str
    my_newStr = my_str[::-1]
    if my_str == my_newStr:
        print "Palindrome"
    else:
        print "Nope"

checkPalindrome(my_str1)
checkPalindrome(my_str2)
"""
#------------------Other data structures-----------------

#---------------multiples of 3 and 5 in 1000 numbers-------
"""
numbers =[]
sum = 0

for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        numbers.append(i)

for i in numbers:
    sum += i

print numbers
print sum
"""
#------------------------------------------------------------

#---------------Fibonacci------------------
"""
sequence = 12
fib = []
sum = 0

for i in range(100):
    if i == 0 or i ==1:
        fib.append(i)
    else:
        fib.append(fib[i-2] + fib[i-1])


for j in fib:
    print j
    sum += j

print sum
"""
#-------------------------------------------
#-------largest prime factor----------------
"""
number = 600851475143
maxFactor = number

factors = []


for i in range(2, 10000000):
    if maxFactor % i == 0:
        print "factor found"
        factors.append(i)
        maxFactor = number/i
        print maxFactor

print factors
"""
#------------------------------------------
"""
palindromes = []

for i in range(100, 500):
    for j in range(501, 999):
        num = str(i*j)
        if num == num[::-1]:
            palindromes.append(num)
        else:
            pass

print palindromes[len(palindromes)-1]
"""
#---------------------------------------
""" smallest number divisible by 1-20
num = 20
found = True

while found:
    num += 1
    for i in range(2, 21):
        if(num % i == 0):
            #print num, i
            pass
        else:
            break

        if (i == 20):
            print num
            found = False
            break            
"""
