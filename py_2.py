"""
Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)

You can find some examples in the test fixtures.
"""
def make_readable(seconds):
    hr = seconds // 3600
    seconds = seconds % 3600
    minute = seconds // 60
    second = seconds % 60

    return f"{hr:02}:{minute:02}:{second:02}"

# print(make_readable(359999))


"""
The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result should be {'a': 2, 'b': 1}.
What if the string is empty? Then the result should be empty object literal, {}.

"""
def count(s):
    dct = {}
    for i in s:
        if i not in dct.keys():
            dct[i] = 1
        else:
            dct[i] += 1
    return dct

# count('aabbc')

"""
In this kata you are required to, given a string, replace every letter with its position in the alphabet.
If anything in the text isn't a letter, ignore it and don't return it.
"a" = 1, "b" = 2, etc.
"""

def alphabet_position(text):
    newString = ""

    for i in range(len(text)):
        if text[i].isalpha():
            newString += str(ord(text[i].lower()) - 96) + " "

    return newString.strip()

# print(alphabet_position("The sunset sets at twelve o' clock."))


"""
You live in the city of Cartesia where all roads are laid out in a perfect grid. You arrived ten minutes too early to an appointment, so you decided to take the opportunity to go for a short walk. The city provides its citizens with a Walk Generating App on their phones -- everytime you press the button it sends you an array of one-letter strings representing directions to walk (eg. ['n', 's', 'w', 'e']). You always walk only a single block for each letter (direction) and you know it takes you one minute to traverse one city block, so create a function that will return true if the walk the app gives you will take you exactly ten minutes (you don't want to be early or late!) and will, of course, return you to your starting point. Return false otherwise.

Note: you will always receive a valid array containing a random assortment of direction letters ('n', 's', 'e', or 'w' only). It will never give you an empty array (that's not a walk, that's standing still!).

1 step = 1 minute => 10 step last (jodi)
"""

def is_valid_walk(walk):
    if len(walk) != 10:
        return False

    north = walk.count('n')
    south = walk.count('s')
    east = walk.count('e')
    west = walk.count('w')

    return north == south and east == west

# print(is_valid_walk(['w','e','w','e','w','e','w','e']))


"""
ind the missing letter
Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.

You will always get an valid array. And it will be always exactly one letter be missing. The length of the array will always be at least 2.
The array will always contain letters in only one case.

Example:

['a','b','c','d','f'] -> 'e'
['O','Q','R','S'] -> 'P'
"""

def find_missing_letter(chars):
    start = ord(chars[0])

    for i in range(len(chars)):
        if ord(chars[i]) != start + i:
            return chr(start + i)

# print(find_missing_letter(['b','d']))


"""
Greed is a dice game played with five six-sided dice. Your mission, should you choose to accept it, is to score a throw according to these rules. You will always be given an array with five six-sided dice values.

 Three 1's => 1000 points
 Three 6's =>  600 points
 Three 5's =>  500 points
 Three 4's =>  400 points
 Three 3's =>  300 points
 Three 2's =>  200 points
 One   1   =>  100 points
 One   5   =>   50 point
Each of 5 dice can only be counted once in each roll. For example, a given "5" can only count as part of a triplet (contributing to the 500 points) or as a single 50 points, but not both in the same roll.

Example scoring

 Throw       Score
 ---------   ------------------
 5 1 3 4 1   250:  50 (for the 5) + 2 * 100 (for the 1s)
 1 1 1 3 1   1100: 1000 (for three 1s) + 100 (for the other 1)
 2 4 4 5 4   450:  400 (for three 4s) + 50 (for the 5)
Note: your solution must not modify the input list.

"""

def score(dice):
    countdct = {}

    for i in dice:
        countdct[i] = countdct.get(i, 0) + 1

    total = 0

    for number, count in countdct.items():

        if number == 1:
            if count >= 3:
                total += 1000
                total += (count - 3) * 100
            else:
                total += count * 100

        elif number == 5:
            if count >= 3:
                total += 500
                total += (count - 3) * 50
            else:
                total += count * 50

        else:
            if count >= 3:
                total += number * 100

    return total

print(score( [5, 1, 3, 4, 1] ))